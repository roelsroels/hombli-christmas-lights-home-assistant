"""Scene selector for Hombli Christmas Lights."""

from __future__ import annotations

from homeassistant.components.select import SelectEntity
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity

from . import HombliConfigEntry
from .const import SCENES
from .entity import HombliChristmasLightsEntity


async def async_setup_entry(
    hass: HomeAssistant,
    entry: HombliConfigEntry,
    async_add_entities: AddConfigEntryEntitiesCallback,
) -> None:
    """Set up the scene selector."""
    async_add_entities([HombliSceneSelect(entry)])


class HombliSceneSelect(HombliChristmasLightsEntity, SelectEntity, RestoreEntity):
    """Select and expose the last successfully commanded scene."""

    _attr_icon = "mdi:string-lights"
    _attr_translation_key = "scene"

    def __init__(self, entry: HombliConfigEntry) -> None:
        """Initialize the selector."""
        super().__init__(entry, entry.runtime_data, "scene")
        self._attr_options = list(SCENES)

    @property
    def current_option(self) -> str | None:
        """Return the current scene."""
        return self._controller.active_scene

    async def async_added_to_hass(self) -> None:
        """Restore the last commanded scene after a restart."""
        await super().async_added_to_hass()
        if self._controller.active_scene is not None:
            return
        last_state = await self.async_get_last_state()
        if last_state is not None and last_state.state in SCENES:
            self._controller.active_scene = last_state.state

    async def async_select_option(self, option: str) -> None:
        """Select a scene."""
        await self._controller.async_set_scene(option)
