#!/usr/bin/env bash
# Execute from this directory
sudo cp init-monitors.py /etc/lightdm
sudo chown root.root /etc/lightdm/init-monitors.py
sudo chmod 0755 /etc/lightdm/init-monitors.py

sudo cp -r lightdm.conf.d/* /etc/lightdm/lightdm.conf.d/
sudo chown root.root /etc/lightdm/lightdm.conf.d/*
sudo chmod 0644 /etc/lightdm/lightdm.conf.d/*
