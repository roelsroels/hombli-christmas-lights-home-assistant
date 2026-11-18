"""Base entity for Hombli Christmas Lights."""

from __future__ import annotations

from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.entity import Entity

from . import HombliConfigEntry
from .const import DOMAIN
from .controller import HombliChristmasLightsController


class HombliChristmasLightsEntity(Entity):
    """Base class for integration entities."""

    _attr_has_entity_name = True

    def __init__(
        self,
        entry: HombliConfigEntry,
        controller: HombliChristmasLightsController,
        key: str,
    ) -> None:
        """Initialize a Hombli entity."""
        self._controller = controller
        self._attr_unique_id = f"{controller.device_id}_{key}"
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, controller.device_id)},
            manufacturer="Hombli",
            model="Smart Christmas Light RGB",
            name=entry.title,
        )

    async def async_added_to_hass(self) -> None:
        """Subscribe to controller updates."""
        await super().async_added_to_hass()
        self.async_on_remove(
            self._controller.async_add_listener(self.async_write_ha_state)
        )
