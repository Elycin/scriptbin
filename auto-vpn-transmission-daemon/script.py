#!/usr/bin/env python

import json
import netifaces
import os
import time


config = {
    "transmission_configuration": "/etc/transmission-daemon/settings.json",
    "vpn_interface": "tun0",
}

"""
Automatic VPN configuration for Transmission Daemon

This script was created in conjunction with OpenVPN to automatically reconfigure the interface that torrenting will occur on.
Please configure your settings.json beforehand, as this script only makes changes to the bound ipv4 address
"""

def get_transmission_config():
    global config
    return json.load(open(config["transmission_configuration"]))

def write_transmission_config(transmission_config):
    global config
    with open(config["transmission_configuration"], 'w') as out: json.dump(transmission_config, out)

def get_interface_address():
    global config
    while True:
        try:
            return netifaces.ifaddresses(config["vpn_interface"])[netifaces.AF_INET][0]['addr']
        except:
            print("interface hasn't connected yet, please wait.")
            time.sleep(1)
        
if __name__ == "__main__":
    # Stop the transmission serivce
    os.system("service transmission-daemon stop")
    
    # Get the configuration
    transmission = get_transmission_config()
    
    # Change the addresses - use ipv4 only
    transmission["bind-address-ipv4"] = get_interface_address()
    transmission["bind-address-ipv6"] = "fe80::"
    
    # Save the configuration
    write_transmission_config(transmission)
    
    # Start the service and exit
    os.system("service transmission-daemon start")
    exit()
