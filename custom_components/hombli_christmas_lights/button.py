"""Buttons for Hombli Christmas Lights."""

from __future__ import annotations

from homeassistant.components.button import ButtonEntity
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback

from . import HombliConfigEntry
from .entity import HombliChristmasLightsEntity


async def async_setup_entry(
    hass: HomeAssistant,
    entry: HombliConfigEntry,
    async_add_entities: AddConfigEntryEntitiesCallback,
) -> None:
    """Set up the random-scene button."""
    async_add_entities([HombliRandomSceneButton(entry)])


class HombliRandomSceneButton(HombliChristmasLightsEntity, ButtonEntity):
    """Select one random scene."""

    _attr_icon = "mdi:shuffle-variant"
    _attr_translation_key = "random_scene"

    def __init__(self, entry: HombliConfigEntry) -> None:
        """Initialize the button."""
        super().__init__(entry, entry.runtime_data, "random_scene")

    async def async_press(self) -> None:
        """Select a random scene."""
        await self._controller.async_select_random_scene()
