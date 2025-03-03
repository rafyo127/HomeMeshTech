"""Sensor platform for mDNS Repeater."""
from homeassistant.helpers.entity import Entity

async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up the mDNS Repeater sensor platform."""
    async_add_entities([MdnsRepeaterSensor()])

class MdnsRepeaterSensor(Entity):
    """Representation of a mDNS Repeater sensor."""

    def __init__(self):
        """Initialize the sensor."""
        self._state = None

    @property
    def name(self):
        """Return the name of the sensor."""
        return "mDNS Repeater"

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    async def async_update(self):
        """Fetch new state data for the sensor."""
        # This is where you would fetch the actual mDNS repeater status
        self._state = "Active"