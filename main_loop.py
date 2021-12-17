import json
import requests
import time
import RPi.GPIO as GPIO
import sys

GPIO.setmode(GPIO.BOARD)

GPIO.setup(40, GPIO.OUT)

currentValue = 0
ledPin = GPIO.PWM(40, 1000)

ledPin.start(currentValue)

usernameFile = open("dev_username", "r")
deviceFile = open("/etc/hostname", "r")

username = usernameFile.readline().strip()
deviceName = deviceFile.readline().strip()

try:
	while True:
	    try:
	        res = requests.head("https://www.example.com", timeout = 1)
	        data = json.dumps({
	            "username": username,
	            "targetDevice": deviceName
	        })

	        headers = {
	            'Content-Type': 'application/json'
	        }

	        url = "http://gitpod-machine.eastus.cloudapp.azure.com:8000/iot-poll"
	        response = requests.request("POST", url, headers=headers, data=data)

	        jsonRes = response.json()

	        if (jsonRes['intensity'] != currentValue):
	            currentValue = jsonRes['intensity']
	            ledPin.ChangeDutyCycle(currentValue)
	            print(jsonRes['intensity'])

	    except KeyboardInterrupt:
	        GPIO.cleanup()
	        sys.exit()
	    except:
	        print("No internet available.")

	    time.sleep(1)
except:
	GPIO.cleanup()
	sys.exit()
