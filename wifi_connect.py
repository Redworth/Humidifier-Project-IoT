#!/usr/bin/sudo /usr/bin/python3

import os
import json
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def rootFunction():
    return "Success"

@app.route('/connect-to-wifi', methods=["POST"])
def wifiConnectRequest():
    req_data = request.get_json()
    name = req_data["SSID"]
    password = req_data["Password"]
    hostname = req_data["Hostname"]
    username = req_data["Username"]
    # establish a wifi connection
    createNewConnection("wlan0", name, password, hostname, username)


# function to establish a new connection
def createNewConnection(name, SSID, password, hostname, username):
    add_to_config_commands = [
      'ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev',
      '\n'
      'update_config=1'
      '\n',
      'country=US',
      'network={',
      '\tssid="{}"'.format(SSID),
      '\tpsk="{}"'.format(password),
      '\tkey_mgmt=WPA-PSK',
      '}'
    ]

    add_to_config = '\n'.join(add_to_config_commands)

    with open("/etc/wpa_supplicant/wpa_supplicant.conf", "w") as wifi_doc:
       wifi_doc.write(add_to_config)

    with open("/etc/hostname", "w") as hostname_doc:
       hostname_doc.write(hostname)

    with open("dev_username", "w") as username_doc:
       username_doc.write(username)

    os.system("sudo reboot")
    print(os.system("ping -c 1 google.com"))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8000', debug=True)
