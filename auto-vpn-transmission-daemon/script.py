#!/usr/bin/env python

import json
import netifaces as ni
import os

config = {
    "transmission_configuration": "/etc/transmission-daemon/settings.json",
    "vpn_interface": "tun0",
}

"""
Automatic VPN for Transmission Daemon

This script was created in conjunction with OpenVPN to automatically reconfigure the interface that torrenting will occur on.
Please configure your settings.json beforehand, as this script only makes changes to the bound ipv4 address\
"""

def get_transmission_config():
    global config
    return json.load(open(config["transmission_configuration"]))

def write_transmission_config(transmission_config):
    global config
    with open(config["transmission_configuration"], 'w') as out: json.dump(transmission_config, out)

def get_interface_address():
    global config
    return ni.ifaddresses(config["vpn_interface"])[ni.AF_INET][0]['addr']

if __name__ == "__main__":
    os.system("service transmission-daemon stop")
    transmission = get_transmission_config()
    transmission["bind-address-ipv4"] = get_interface_address()
    write_transmission_config(transmission)
    os.system("service_transmission-daemon start")
    exit()
