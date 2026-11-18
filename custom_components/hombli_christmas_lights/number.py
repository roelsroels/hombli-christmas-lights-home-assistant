"""Number controls for Hombli Christmas Lights."""

from __future__ import annotations

from collections.abc import Awaitable, Callable

from homeassistant.components.number import NumberEntity, NumberMode
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback

from . import HombliConfigEntry
from .entity import HombliChristmasLightsEntity


async def async_setup_entry(
    hass: HomeAssistant,
    entry: HombliConfigEntry,
    async_add_entities: AddConfigEntryEntitiesCallback,
) -> None:
    """Set up speed and brightness controls."""
    async_add_entities(
        [
            HombliNumber(
                entry,
                key="animation_speed",
                translation_key="animation_speed",
                icon="mdi:speedometer",
                value_getter=lambda: entry.runtime_data.speed,
                value_setter=entry.runtime_data.async_set_speed,
            ),
            HombliNumber(
                entry,
                key="scene_brightness",
                translation_key="scene_brightness",
                icon="mdi:brightness-6",
                value_getter=lambda: entry.runtime_data.brightness,
                value_setter=entry.runtime_data.async_set_brightness,
            ),
        ]
    )


class HombliNumber(HombliChristmasLightsEntity, NumberEntity):
    """A LocalTuya-backed percentage control."""

    _attr_native_min_value = 1
    _attr_native_max_value = 100
    _attr_native_step = 1
    _attr_mode = NumberMode.SLIDER

    def __init__(
        self,
        entry: HombliConfigEntry,
        *,
        key: str,
        translation_key: str,
        icon: str,
        value_getter: Callable[[], int],
        value_setter: Callable[[int], Awaitable[None]],
    ) -> None:
        """Initialize the number entity."""
        super().__init__(entry, entry.runtime_data, key)
        self._attr_translation_key = translation_key
        self._attr_icon = icon
        self._value_getter = value_getter
        self._value_setter = value_setter

    @property
    def native_value(self) -> int:
        """Return the current value."""
        return self._value_getter()

    async def async_set_native_value(self, value: float) -> None:
        """Set the value."""
        await self._value_setter(round(value))
