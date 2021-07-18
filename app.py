from gpiozero import PWMLED
from time import sleep
import requests
import json

controlLed = PWMLED(17)

jsonData = {
    "username": "rohit",
    "targetDevice": "Rohit's Humidifier"
}

firstTime = 1
currentVal = 0

while True:
    pollres = requests.post("https://iot-backend-dev-dev-rohit-karthik.cloud.okteto.net/iot-poll", json=jsonData)

    if firstTime == 1:
        firstTime = 0
        dictResponse = json.loads(pollres.content)
        currentVal = dictResponse['intensity']
        controlLed.value = currentVal/100
    else:
        dictResponse = json.loads(pollres.content)
        if currentVal != dictResponse['intensity']:
            currentVal = dictResponse['intensity']
            controlLed.value = currentVal/100  

    sleep(0.5)
    
    
