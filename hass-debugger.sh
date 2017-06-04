#!/bin/bash

cd /home/homeassistant/.homeassistant
source /srv/homeassistant/homeassistant_venv/bin/activate
hass --script check_config

# If you want to allow homeasistant to restart the service add line below to '/etc/sudoers' file
# homeassistant	ALL=(ALL) NOPASSWD: /bin/systemctl restart home-assistant.service

read -r -p "Do you wish to restart home-assistant.service? [Y/n]" response
response=${response,,}    # tolower
if [[ "$response" =~ ^(yes|y)$ ]]
then
    echo "No Restart"
else
    echo "Restarting HASS"
    echo "================================================================================" >> home-assistant.log
    sudo systemctl restart home-assistant.service
    tail -f home-assistant.log
fi

exit
