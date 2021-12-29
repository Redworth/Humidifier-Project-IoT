# Humidifier-Project-IoT

This git repository contains the code for the IoT device of the IoT Humidifier project.

## Environment Setup
Prerequisites:
- Python 3 (any version) and pip3 installed on IoT device
- Access to raspberry pi IoT device

Clone the git repository (https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository) on the device. Then create a feature branch (https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging) to work on the code.

Install the below dependencies using `pip3`.
- `requests`
- `flask`

The environment is now ready for development.

## Usage
Prerequisites:
- Environment is setup (see above)

Run `python3 wifi_connect.py` to begin a development server that can recieve Wi-Fi credentials from the mobile app. This will keep a web server running that can receive Wi-Fi credentials in JSON format when run as a Linux service. 

Similarly, run `python3 main_loop.py` to begin a development server that can run the main process of requesting data.