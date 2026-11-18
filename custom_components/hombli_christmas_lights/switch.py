"""Random-cycle switch for Hombli Christmas Lights."""

from __future__ import annotations

from collections.abc import Callable
from datetime import datetime, timedelta

from homeassistant.components.switch import SwitchEntity
from homeassistant.core import HomeAssistant, callback
from homeassistant.exceptions import HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback
from homeassistant.helpers.event import async_track_time_interval

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
        self._remove_interval: Callable[[], None] | None = None

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
        if self._attr_is_on:
            await self._controller.async_select_random_scene()
