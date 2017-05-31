
# https://home-assistant.io/developers/creating_components/
# https://home-assistant.io/cookbook/#custom-python-component-examples


import logging

import voluptuous as vol

# from homeassistant.components.switch import SwitchDevice, PLATFORM_SCHEMA
# from homeassistant.const import (
#     CONF_NAME, CONF_SWITCHES, EVENT_HOMEASSISTANT_STOP)
# import homeassistant.helpers.config_validation as cv

_LOGGER = logging.getLogger(__name__)

# thing we define in configuration.yaml
DOMAIN = 'hdmi_controller'


# CONF_SWITCHING_PIN = 'switching_pin'
# CONF_STATE_PINS = 'state_pins'
#
# DEFAULT_SWITCHING_PIN = 11
# DEFAULT_STATE_PINS = 22
#
# SWITCH_SCHEMA = vol.Schema({
#     vol.Optional(CONF_SWITCHING_PIN, default=DEFAULT_SWITCHING_PIN): cv.positive_int,
# }
#
# # The root config dir
# PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
#     vol.Required(CONF_SWITCHING_PIN): cv.positive_int,
#     vol.Required(CONF_STATE_PINS): vol.Schema({cv.string: SWITCH_SCHEMA}),
# }

def setup(hass, config):
    hass.states.set('hello.world', 'Paulus')




    return True


# def setup_platform(hass, config, add_devices, discovery_info=None):
#
#     # grabs only validated values from global config
#     # switching_pin = config.get(CONF_SWITCHING_PIN)
#     # state_pins = config.get(CONF_STATE_PINS)
#     # _LOGGER.warning("MY PINS {}, {}".format(switching_pin, state_pins))
#
#     # number of individual hdmi channels
#     hdmi_devices = []
#
#     hdmi_devices.append(HDMISwitch(hass, 'SEXY SWITCH 1'))
#     hdmi_devices.append(HDMISwitch(hass, 'SEXY SWITCH 2'))
#     hdmi_devices.append(HDMISwitch(hass, 'SEXY SWITCH 3'))
#
#     # appends with a list of HASS python class objects
#     add_devices(hdmi_devices)
#
#
#
# class HDMISwitch(SwitchDevice):
#     """Representation of a GPIO RF switch."""
#
#     def __init__(self, hass, name):
#         """Initialize the switch."""
#         self._hass = hass
#         self._name = name
#         self._state = False
#
#     @property
#     def should_poll(self):
#         """No polling needed."""
#         return False
#
#     @property
#     def name(self):
#         """Return the name of the switch."""
#         return self._name
#
#     @property
#     def is_on(self):
#         """Return true if device is on."""
#         return self._state
#
#     def turn_on(self):
#         """Turn the switch on."""
#         self._state = True
#         self.schedule_update_ha_state()
#
#     def turn_off(self):
#         """Turn the switch off."""
#         self._state = False
#         self.schedule_update_ha_state()
