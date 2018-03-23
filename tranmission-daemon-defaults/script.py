#!/usr/bin/env python

import json
import netifaces
import os

config = {
    "transmission_configuration": "/etc/transmission-daemon/settings.json",
    "vpn_interface": "tun0",
}

"""
Change default configuration for tranmission daemon

"""

def get_transmission_config():
    global config
    return json.load(open(config["transmission_configuration"]))

def write_transmission_config(transmission_config):
    global config
    with open(config["transmission_configuration"], 'w') as out: json.dump(transmission_config, out)
	
if __name__ == "__main__":
    # Stop the transmission serivce
    os.system("service transmission-daemon stop")
    
    # Get the configuration
    transmission = get_transmission_config()
    
    # Change the settings we want.
    transmission["bind-address-ipv6"] = "fe80::"
    
    # Save the configuration
    write_transmission_config(transmission)
    
    # Start the service and exit
    os.system("service transmission-daemon start")
    exit()
