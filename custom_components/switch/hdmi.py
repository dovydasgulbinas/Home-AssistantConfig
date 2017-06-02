
# https://home-assistant.io/developers/creating_components/
# https://home-assistant.io/cookbook/#custom-python-component-examples

# refer to rpi_rf.py

import logging
import time
import voluptuous as vol

from homeassistant.components.switch import SwitchDevice, PLATFORM_SCHEMA
from homeassistant.const import (
    CONF_NAME, CONF_SWITCHES, EVENT_HOMEASSISTANT_STOP)
from homeassistant.components import rpi_gpio as gpio

REQUIREMENTS = ['RPi.GPIO==0.6.1']

_LOGGER = logging.getLogger(__name__)

def setup_platform(hass, config, add_devices, discovery_info=None):
    import RPi.GPIO as GPIO
    hdmi_devices = []

    state_pins = [12,20,21]
    pull_down=True
    # will initialize pins in input mode
    # for pin in state_pins:
    #     GPIO.setup(pin, GPIO.IN, GPIO.PUD_DOWN if pull_down else GPIO.PUD_UP)


    hdmi_devices.append(HDMISwitch(hass, config, 'HDMI Channel 1', GPIO, 0, state_pins))
    hdmi_devices.append(HDMISwitch(hass, config, 'HDMI Channel 2', GPIO, 1, state_pins))
    hdmi_devices.append(HDMISwitch(hass, config, 'HDMI Channel 3', GPIO, 2, state_pins))
    # appends with a list of HASS python class objects
    add_devices(hdmi_devices)

    hass.bus.listen_once(EVENT_HOMEASSISTANT_STOP, lambda event: GPIO.cleanup())


class HDMISwitch(SwitchDevice):
    """Representation of a GPIO RF switch."""

    def __init__(self, hass, config, name, GPIO, index, state_pins):
        """Initialize the switch."""
        self._hass = hass
        self._name = name
        self._state = False
        # TODO: Add proper pin resolustion
        self._switching_pin = 16
        self._state_pins = state_pins
        self._falling_edge = True
        self._GPIO=GPIO
        self._init_gpio(hass, config)
        self._state_pin = state_pins[index]

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
        self._activate_channel()
        self._state = True
        self.schedule_update_ha_state()

    def turn_off(self):
        """Turn the switch off."""
        self._write_output(True)
        self._state = False
        self.schedule_update_ha_state()

    def _init_gpio(self, hass, config):
        """Set up the Raspberry PI GPIO component."""
        self._GPIO.setmode(self._GPIO.BCM)
        self._setup_output()
        self._setup_input()

    def _write_output(self, value):
        """Write a value to a GPIO."""
        self._GPIO.output(self._switching_pin, value)

    def _setup_output(self):
        """Set up a GPIO as output."""
        # TODO: optimize to or export to a static method
        self._GPIO.setup(self._switching_pin, self._GPIO.OUT)
        self._write_output(self._falling_edge)

    def _setup_input(self, pull_down=True):
        self._GPIO.setup(self._state_pin, self._GPIO.IN, self._GPIO.PUD_DOWN if pull_down else self._GPIO.PUD_UP)

    def _read_input(self, pin):
        return self.GPIO.input(pin)

    def _switch_position(self):
        _LOGGER.debug(">>> Changing source")
        self._write_output(self._falling_edge)
        time.sleep(0.05)
        self._write_output(not self._falling_edge)
        time.sleep(0.05)
        self._write_output(self._falling_edge)

    def _activate_channel():
        # FIXME: add channel selector!
        self._switch_position()
