"""Random-cycle switch for Hombli Christmas Lights."""

from __future__ import annotations

from collections.abc import Callable
from datetime import datetime, timedelta

from homeassistant.components.switch import SwitchEntity
from homeassistant.const import STATE_OFF
from homeassistant.core import Event, HomeAssistant, callback
from homeassistant.exceptions import HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback
from homeassistant.helpers.event import (
    async_track_state_change_event,
    async_track_time_interval,
)

from . import HombliConfigEntry
from .const import RANDOM_CYCLE_INTERVAL_SECONDS
from .entity import HombliChristmasLightsEntity


async def async_setup_entry(
    hass: HomeAssistant,
    entry: HombliConfigEntry,
    async_add_entities: AddConfigEntryEntitiesCallback,
) -> None:
    """Set up the random-cycle switch."""
    async_add_entities([HombliRandomCycleSwitch(entry)])


class HombliRandomCycleSwitch(HombliChristmasLightsEntity, SwitchEntity):
    """Select a different random scene every 30 seconds."""

    _attr_icon = "mdi:shuffle-variant"
    _attr_translation_key = "random_cycle"

    def __init__(self, entry: HombliConfigEntry) -> None:
        """Initialize the switch."""
        super().__init__(entry, entry.runtime_data, "random_cycle")
        self._attr_is_on = False
        self._light_entity_id: str | None = None
        self._remove_interval: Callable[[], None] | None = None

    async def async_added_to_hass(self) -> None:
        """Stop cycling whenever the matching LocalTuya light turns off."""
        await super().async_added_to_hass()
        self._light_entity_id = self._controller.localtuya_light_entity_id()
        if self._light_entity_id is not None:
            self.async_on_remove(
                async_track_state_change_event(
                    self.hass,
                    [self._light_entity_id],
                    self._async_light_state_changed,
                )
            )

    async def async_turn_on(self, **kwargs: object) -> None:
        """Start random scene cycling and select the first scene immediately."""
        self._attr_is_on = True
        self.async_write_ha_state()
        try:
            await self._controller.async_select_random_scene()
        except HomeAssistantError:
            self._attr_is_on = False
            self.async_write_ha_state()
            raise
        self._start_interval()

    async def async_turn_off(self, **kwargs: object) -> None:
        """Stop random scene cycling."""
        self._attr_is_on = False
        self._stop_interval()
        self.async_write_ha_state()

    async def async_will_remove_from_hass(self) -> None:
        """Cancel the timer when the entity is removed."""
        self._stop_interval()
        await super().async_will_remove_from_hass()

    @callback
    def _start_interval(self) -> None:
        self._stop_interval()
        self._remove_interval = async_track_time_interval(
            self.hass,
            self._async_next_scene,
            timedelta(seconds=RANDOM_CYCLE_INTERVAL_SECONDS),
        )

    @callback
    def _stop_interval(self) -> None:
        if self._remove_interval is not None:
            self._remove_interval()
            self._remove_interval = None

    async def _async_next_scene(self, now: datetime) -> None:
        if not self._attr_is_on:
            return
        if self._light_entity_id is None:
            # The registry entry can appear after this integration during
            # startup. Resolve it again before a scheduled scene is allowed to
            # power the string on.
            self._light_entity_id = self._controller.localtuya_light_entity_id()
        if self._light_entity_id is not None and self.hass.states.is_state(
            self._light_entity_id, STATE_OFF
        ):
            await self.async_turn_off()
            return
        await self._controller.async_select_random_scene()

    async def _async_light_state_changed(self, event: Event) -> None:
        """Disable random cycling when the physical light is switched off."""
        new_state = event.data.get("new_state")
        if (
            self._attr_is_on
            and new_state is not None
            and new_state.state == STATE_OFF
        ):
            await self.async_turn_off()
            # If a scene command was already holding the controller lock when
            # the user switched the string off, send power-off once more after
            # that command finishes. This makes the user's off action win the
            # race without making the random-cycle switch itself turn off the
            # lights when it is toggled normally.
            await self._controller.async_ensure_power_off()
