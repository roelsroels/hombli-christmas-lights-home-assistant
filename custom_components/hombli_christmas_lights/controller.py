"""LocalTuya-backed controller for Hombli Christmas Lights."""

from __future__ import annotations

import asyncio
import secrets
from collections.abc import Callable

from homeassistant.core import HomeAssistant, callback
from homeassistant.exceptions import HomeAssistantError
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers import entity_registry as er

from .const import (
    DP_BRIGHTNESS,
    DP_MODE,
    DP_POWER,
    DP_SCENE,
    DP_SPEED,
    MODE_SCENE,
    SCENE_CODES,
    SCENES,
)

LOCALTUYA_DOMAIN = "localtuya"
LOCALTUYA_SET_DP = "set_dp"
TUYA_DOMAIN = "tuya"


class HombliChristmasLightsController:
    """Send validated commands through LocalTuya's public set_dp action."""

    def __init__(self, hass: HomeAssistant, device_id: str) -> None:
        """Initialize the controller."""
        self.hass = hass
        self.device_id = device_id
        self.active_scene: str | None = None
        self.speed = 50
        self.brightness = 100
        self._listeners: set[Callable[[], None]] = set()
        self._command_lock = asyncio.Lock()

    @callback
    def async_add_listener(self, listener: Callable[[], None]) -> Callable[[], None]:
        """Register a state listener and return its unsubscribe callback."""
        self._listeners.add(listener)

        @callback
        def remove_listener() -> None:
            self._listeners.discard(listener)

        return remove_listener

    @callback
    def _notify_listeners(self) -> None:
        for listener in tuple(self._listeners):
            listener()

    @callback
    def power_light_entity_id(self) -> str | None:
        """Return the power light entity for this physical controller."""
        device_registry = dr.async_get(self.hass)
        entity_registry = er.async_get(self.hass)
        identifiers = {
            (LOCALTUYA_DOMAIN, self.device_id),
            (LOCALTUYA_DOMAIN, f"local_{self.device_id}"),
        }

        device_ids = {
            device.id
            for device in device_registry.devices.values()
            if device.identifiers & identifiers
        }
        localtuya_entries = [
            entity
            for device_id in device_ids
            for entity in er.async_entries_for_device(entity_registry, device_id)
            if entity.domain == "light"
            and entity.platform == LOCALTUYA_DOMAIN
            and entity.disabled_by is None
        ]
        # Some installations use LocalTuya for the scene datapoints but expose
        # the dashboard's power light through Home Assistant's standard Tuya
        # integration. Tuya entity unique IDs include the same physical device
        # ID, so match that exact prefix as a reliable cross-integration link.
        tuya_entries = [
            entity
            for entity in entity_registry.entities.values()
            if entity.domain == "light"
            and entity.platform == TUYA_DOMAIN
            and entity.disabled_by is None
            and entity.unique_id.startswith(f"{TUYA_DOMAIN}.{self.device_id}")
        ]
        light_entries = tuya_entries or localtuya_entries
        if not light_entries:
            return None

        light_entries.sort(
            key=lambda entity: (
                not entity.unique_id.endswith(f"_{DP_POWER}"),
                entity.entity_id,
            )
        )
        return light_entries[0].entity_id

    async def async_set_scene(self, scene_name: str) -> None:
        """Power on the string and select a captured scene."""
        scene_code = SCENE_CODES.get(scene_name)
        if scene_code is None:
            raise HomeAssistantError(f"Unknown Hombli scene: {scene_name}")

        async with self._command_lock:
            await self._async_set_dp(DP_POWER, True)
            await self._async_set_dp(DP_MODE, MODE_SCENE)
            await asyncio.sleep(0.15)
            await self._async_set_dp(DP_SCENE, scene_code)

        self.active_scene = scene_name
        self._notify_listeners()

    async def async_set_speed(self, value: int) -> None:
        """Set animation speed."""
        value = self._validate_percentage(value)
        async with self._command_lock:
            await self._async_set_dp(DP_SPEED, value)
        self.speed = value
        self._notify_listeners()

    async def async_set_brightness(self, value: int) -> None:
        """Set scene brightness."""
        value = self._validate_percentage(value)
        async with self._command_lock:
            await self._async_set_dp(DP_BRIGHTNESS, value)
        self.brightness = value
        self._notify_listeners()

    async def async_select_random_scene(self) -> None:
        """Select a scene different from the currently active scene."""
        choices = tuple(scene for scene in SCENES if scene != self.active_scene)
        await self.async_set_scene(secrets.choice(choices))

    async def async_ensure_power_off(self) -> None:
        """Make an observed manual power-off authoritative over queued commands."""
        async with self._command_lock:
            await self._async_set_dp(DP_POWER, False)

    async def _async_set_dp(self, dp: int, value: object) -> None:
        if not self.hass.services.has_service(LOCALTUYA_DOMAIN, LOCALTUYA_SET_DP):
            raise HomeAssistantError(
                "LocalTuya is not ready; ensure it is installed and configured"
            )

        await self.hass.services.async_call(
            LOCALTUYA_DOMAIN,
            LOCALTUYA_SET_DP,
            {"device_id": self.device_id, "dp": dp, "value": value},
            blocking=True,
        )

    @staticmethod
    def _validate_percentage(value: int) -> int:
        value = int(value)
        if not 1 <= value <= 100:
            raise HomeAssistantError("Value must be between 1 and 100")
        return value
