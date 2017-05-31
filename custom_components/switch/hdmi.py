
# https://home-assistant.io/developers/creating_components/
# https://home-assistant.io/cookbook/#custom-python-component-examples

# refer to rpi_rf.py

import logging

import voluptuous as vol

from homeassistant.components.switch import SwitchDevice, PLATFORM_SCHEMA
from homeassistant.const import (
    CONF_NAME, CONF_SWITCHES, EVENT_HOMEASSISTANT_STOP)

_LOGGER = logging.getLogger(__name__)

# thing we define in configuration.yaml
# DOMAIN = 'hdmi_controller'


def setup_platform(hass, config, add_devices, discovery_info=None):
    hdmi_devices = []

    hdmi_devices.append(HDMISwitch(hass, 'SEXY SWITCH 1'))
    hdmi_devices.append(HDMISwitch(hass, 'SEXY SWITCH 2'))
    hdmi_devices.append(HDMISwitch(hass, 'SEXY SWITCH 3'))

    # appends with a list of HASS python class objects
    add_devices(hdmi_devices)



class HDMISwitch(SwitchDevice):
    """Representation of a GPIO RF switch."""

    def __init__(self, hass, name):
        """Initialize the switch."""
        self._hass = hass
        self._name = name
        self._state = False

    @property
    def should_poll(self):
        """No polling needed."""
        return False

    @property
    def name(self):
        """Return the name of the switch."""
        return self._name

    @property
    def is_on(self):
        """Return true if device is on."""
        return self._state

    def turn_on(self):
        """Turn the switch on."""
        self._state = True
        self.schedule_update_ha_state()

    def turn_off(self):
        """Turn the switch off."""
        self._state = False
        self.schedule_update_ha_state()
