"""Hombli Christmas Lights integration."""

from __future__ import annotations

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady

from .const import CONF_DEVICE_ID, PLATFORMS
from .controller import (
    LOCALTUYA_DOMAIN,
    LOCALTUYA_SET_DP,
    HombliChristmasLightsController,
)

type HombliConfigEntry = ConfigEntry[HombliChristmasLightsController]


async def async_setup_entry(hass: HomeAssistant, entry: HombliConfigEntry) -> bool:
    """Set up Hombli Christmas Lights from a config entry."""
    if not hass.services.has_service(LOCALTUYA_DOMAIN, LOCALTUYA_SET_DP):
        raise ConfigEntryNotReady("LocalTuya set_dp action is not available")

    entry.runtime_data = HombliChristmasLightsController(
        hass, entry.data[CONF_DEVICE_ID]
    )
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def async_unload_entry(hass: HomeAssistant, entry: HombliConfigEntry) -> bool:
    """Unload a config entry."""
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
