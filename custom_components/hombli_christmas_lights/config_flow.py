"""Config flow for Hombli Christmas Lights."""

from __future__ import annotations

from typing import Any

import voluptuous as vol
from homeassistant.config_entries import ConfigFlow, ConfigFlowResult
from homeassistant.helpers import selector

from .const import CONF_DEVICE_ID, CONF_NAME, DEFAULT_NAME, DOMAIN


class HombliChristmasLightsConfigFlow(ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Hombli Christmas Lights."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Handle the initial setup step."""
        errors: dict[str, str] = {}

        if user_input is not None:
            device_id = user_input[CONF_DEVICE_ID].strip()
            name = user_input[CONF_NAME].strip() or DEFAULT_NAME

            if not device_id:
                errors[CONF_DEVICE_ID] = "required"
            else:
                await self.async_set_unique_id(device_id)
                self._abort_if_unique_id_configured()
                return self.async_create_entry(
                    title=name,
                    data={CONF_DEVICE_ID: device_id, CONF_NAME: name},
                )

        return self.async_show_form(
            step_id="user",
            data_schema=self._setup_schema(),
            errors=errors,
        )

    async def async_step_reconfigure(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Reconfigure an existing entry."""
        entry = self._get_reconfigure_entry()
        errors: dict[str, str] = {}

        if user_input is not None:
            device_id = user_input[CONF_DEVICE_ID].strip()
            name = user_input[CONF_NAME].strip() or DEFAULT_NAME
            if not device_id:
                errors[CONF_DEVICE_ID] = "required"
            else:
                await self.async_set_unique_id(device_id)
                self._abort_if_unique_id_mismatch()
                return self.async_update_reload_and_abort(
                    entry,
                    data_updates={CONF_DEVICE_ID: device_id, CONF_NAME: name},
                    title=name,
                )

        return self.async_show_form(
            step_id="reconfigure",
            data_schema=self.add_suggested_values_to_schema(
                self._setup_schema(), entry.data
            ),
            errors=errors,
        )

    @staticmethod
    def _setup_schema() -> vol.Schema:
        """Return the setup form schema."""
        return vol.Schema(
            {
                vol.Required(CONF_NAME, default=DEFAULT_NAME): selector.TextSelector(),
                vol.Required(CONF_DEVICE_ID): selector.TextSelector(),
            }
        )
