import os
import json
from flask import Flask, request
from flask_cors import *

app = Flask(__name__)

CORS(app)


@app.route('/connect-to-wifi', methods=["POST"])
def wifiConnectRequest():
    req_data = request.json()
    name = req_data["SSID"]
    password = req_data["Password"]
    # establish a wifi connection
    createNewConnection(name, name, password)
    # connect to the wifi network
    connect(name, name)


# function to establish a new connection
def createNewConnection(name, SSID, password):
    config = """<?xml version=\"1.0\"?>
        <WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
            <name>"""+name+"""</name>
            <SSIDConfig>
                <SSID>
                    <name>"""+SSID+"""</name>
                </SSID>
            </SSIDConfig>
            <connectionType>ESS</connectionType>
            <connectionMode>auto</connectionMode>
            <MSM>
                <security>
                    <authEncryption>
                        <authentication>WPA2PSK</authentication>
                        <encryption>AES</encryption>
                        <useOneX>false</useOneX>
                    </authEncryption>
                    <sharedKey>
                        <keyType>passPhrase</keyType>
                        <protected>false</protected>
                        <keyMaterial>"""+password+"""</keyMaterial>
                    </sharedKey>
                </security>
            </MSM>
        </WLANProfile>
    """
    command = "netsh wlan add profile filename=\""+name+".xml\""+" interface=Wi-Fi"
    with open(name+".xml", 'w') as file:
        file.write(config)
    os.system(command)

# function to connect to a network


def connect(name, SSID):
    command = "netsh wlan connect name=\""+name + \
        "\" ssid=\""+SSID+"\" interface=Wi-Fi"
    os.system(command)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8000', debug=True)