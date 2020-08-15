import logging
from datetime import datetime, timedelta

import requests
from requests import get

_LOGGER = logging.getLogger(__name__)

class HelloWorld():
  def __init__(self, host, api_key):
    self.data = {}
    self._host = host
    self._api_key = api_key

  def refresh_data(self):  # pylint:disable=too-many-branches
    """Update data from printer."""

    data = {
      "sensor_name": "Hello World Sensor",
      "sensor_host": self._host,
      "sensor_api_key": self._api_key,
      "device_class": "temperature",
      "unit_of_measurement": '°C',
      "cpu_temp": 23,
      "count": self.timestamp()
      }
    
    self.data = data

  def timestamp(self):
    """ return epoch timestamp """
    now = datetime.now()
    return round(datetime.timestamp(now))

  @property
  def available(self):
      """Return True is data is available."""
      return bool(self.data)
