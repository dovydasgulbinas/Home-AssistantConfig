#!/bin/bash

# cd /home/homeassistant/.homeassistant
# source /srv/homeassistant/homeassistant_venv/bin/activate
# hass --script check_config


read -r -p "Do you wish to see git diff? [y/N]" response
response=${response,,}    # tolower
if [[ "$response" =~ ^(yes|y)$ ]]
then
    git diff
else
    "Skipping diff"
fi

echo "========================================"

git add .
git status
echo -n "Enter the Description for the Change: " [Minor Update]
read CHANGE_MSG
git commit -m "${CHANGE_MSG}"
git push origin master

exit
