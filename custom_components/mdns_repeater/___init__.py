"""The mDNS Repeater integration."""
import logging
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

_LOGGER = logging.getLogger(__name__)

DOMAIN = "mdns_repeater"

async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the mDNS Repeater component."""
    _LOGGER.info("Setting up mDNS Repeater")
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up mDNS Repeater from a config entry."""
    _LOGGER.info("Setting up mDNS Repeater from config entry")
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Unload a config entry."""
    _LOGGER.info("Unloading mDNS Repeater config entry")
    return True