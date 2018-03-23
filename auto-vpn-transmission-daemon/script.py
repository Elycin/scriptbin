import json
import netifaces as ni

config = {
    "transmission_configuration": "/etc/transmission-daemon/settings.json",
    "vpn_interface": "tun0",
}

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
    transmission = get_transmission_config()
    transmission["bind-address-ipv4"] = get_interface_address()
    write_transmission_config(transmission)
    exit()
