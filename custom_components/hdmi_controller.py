
# https://home-assistant.io/developers/creating_components/
# https://home-assistant.io/cookbook/#custom-python-component-examples




# thing we define in configuration.yaml
DOMAIN = 'hdmi_controller'

def setup(hass, config):
    hass.states.set('hello.world', 'Paulus')

    return True
