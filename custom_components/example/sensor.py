"""Platform for Example sensor integration."""

import asyncio
import logging

from homeassistant.const import TEMP_CELSIUS
from homeassistant.helpers.entity import Entity

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(hass, config_entry, async_add_entities):
    """Add a weather entity from a config_entry."""
    
    coordinator = hass.data[DOMAIN][config_entry.entry_id]

    # Example: async_add_entities([MetWeather(config_entry.data, hass.config.units.is_metric)])
    async_add_entities([ExampleSensor(config_entry, coordinator, "Confused")])


class ExampleSensor(Entity):
    """Representation an example temperature sensor."""

    def __init__(self, arg1_config, coordinator, dazed):
        """Initialize the sensor."""
        #self._name = arg1_config.title +' Example'
        self._config = arg1_config
        self.coordinator = coordinator
        self._name = coordinator.data['sensor_name']

        self._dazed = dazed
        self._state = 0
        self._count = 0
    
    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement."""
        return TEMP_CELSIUS

    @property
    def unique_id(self):
        return self._config.entry_id + '-cpu'

    @property
    def state_attributes(self):
        """Return the state attributes of the sun."""
        return {
            "count": self._count,
            "dazed": self._dazed,
            # see it, to help me understand it
            "config_entry": self._config,
        }

    @property
    def available(self):
        """Return True if entity is available."""
        return self.coordinator.last_update_success

    @property
    def entity_registry_enabled_default(self):
        """Return if the entity should be enabled when first added to the entity registry."""
        return True

    async def async_update(self):
        """Fetch new state data for the sensor."""
        _LOGGER.debug("updating example sensor")
        #await self.coordinator.async_request_refresh()
        self._count = self.coordinator.data['count']
        self._state = self.coordinator.data['cpu_temp']
