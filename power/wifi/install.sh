#!/usr/bin/env bash
# Special thanks to SleeplessBeastie
# https://blog.sleeplessbeastie.eu/2016/06/10/how-to-reload-wifi-module-on-resume/

# Execute from this directory
sudo cp pm-wifi-resume.sh /etc/pm/sleep.d/75_wifi-resume
sudo chown root.root /etc/pm/sleep.d/75_wifi-resume
sudo chmod 0755 /etc/pm/sleep.d/75_wifi-resume

sudo cp systemd-wifi-resume.sh /lib/systemd/system-sleep/wifi-resume
sudo chown root.root /lib/systemd/system-sleep/wifi-resume
sudo chmod 0755 /lib/systemd/system-sleep/wifi-resume
