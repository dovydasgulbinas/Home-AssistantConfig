#!/bin/bash

cd /home/homeassistant/.homeassistant
source /srv/homeassistant/homeassistant_venv/bin/activate
hass --script check_config

# If you want to allow homeasistant to restart the service add line below to '/etc/sudoers' file
# homeassistant	ALL=(ALL) NOPASSWD: /bin/systemctl restart home-assistant.service

read -r -p "Do you wish to restart home-assistant.service? [y/N]" response
response=${response,,}    # tolower
if [[ "$response" =~ ^(yes|y)$ ]]
then
    echo "Restarting HASS"
    sudo systemctl restart home-assistant.service
    tail -f home-assistant.log
else
    echo "No Restart"
fi

# read -r -p "Do you wish to read home assistant log? [y/N]" response
# response=${response,,}    # tolower
# if [[ "$response" =~ ^(yes|y)$ ]]
# then
#     tail -f home-assistant.log
# else
#     echo "No Log"
# fi

exit
