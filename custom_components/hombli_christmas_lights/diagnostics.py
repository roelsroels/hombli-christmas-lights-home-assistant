"""Diagnostics for Hombli Christmas Lights."""

from __future__ import annotations

from typing import Any

from homeassistant.core import HomeAssistant
from homeassistant.helpers.redact import async_redact_data

from . import HombliConfigEntry
from .const import CONF_DEVICE_ID

TO_REDACT = {CONF_DEVICE_ID}


async def async_get_config_entry_diagnostics(
    hass: HomeAssistant, entry: HombliConfigEntry
) -> dict[str, Any]:
    """Return safe diagnostics for a config entry."""
    controller = entry.runtime_data
    return {
        "config_entry": async_redact_data(dict(entry.data), TO_REDACT),
        "state": {
            "active_scene": controller.active_scene,
            "animation_speed": controller.speed,
            "scene_brightness": controller.brightness,
            "power_light_entity": controller.power_light_entity_id(),
        },
    }
