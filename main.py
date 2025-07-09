import os
import re
import yaml
from pathlib import Path
from core.can_interface import send_frame
from core.mqtt_client import MQTTClient


CONFIG_DIR = Path("config")
MQTT_CONFIG_FILE = CONFIG_DIR / "mqtt_config.yaml"
SYSTEM_CONFIG_FILE = CONFIG_DIR / "system_config.yaml"


def prompt_mqtt_config():
    print("\n--- MQTT Configuration ---")
    broker = input("MQTT Broker (e.g., mqtt.example.com): ")
    port = input("MQTT Port [1883]: ") or "1883"
    username = input("MQTT Username (optional): ")
    password = input("MQTT Password (optional): ")

    config = {
        'broker': broker,
        'port': int(port),
        'username': username or None,
        'password': password or None,
        'topic_prefix': 'picantrol',
        'use_tls': 'true',
        'insecure_tls': 'true'
    }

    CONFIG_DIR.mkdir(exist_ok=True)
    with open(MQTT_CONFIG_FILE, 'w') as f:
        yaml.dump(config, f)
    print("Saved MQTT configuration.")


def prompt_system_config():
    print("\n--- System Configuration ---")
    vehicle = input("Enter your vehicle profile name (e.g., chevy_volt_2017): ")
    vehicle_id = input("Enter a unique vehicle ID for this Pi (e.g., volt2017-rob, or your license plate) Must be unique per MQTT server: ")
    vehicle_id = slugify(vehicle_id)
    config = {'vehicle_profile': vehicle,
              'vehicle_id': vehicle_id}

    CONFIG_DIR.mkdir(exist_ok=True)
    with open(SYSTEM_CONFIG_FILE, 'w') as f:
        yaml.dump(config, f)
    print("Saved system configuration.")

def slugify(value):
    return re.sub(r'[^a-zA-Z0-9_-]', '-', value.lower())


def check_and_setup():
    if not MQTT_CONFIG_FILE.exists():
        print("MQTT configuration not found.")
        prompt_mqtt_config()

    if not SYSTEM_CONFIG_FILE.exists():
        print("System configuration not found.")
        prompt_system_config()
    print("\nConfiguration complete. Ready to begin.")


def main():
    print("\nWelcome to PiCANtrol")
    check_and_setup()

    mqtt = MQTTClient(SYSTEM_CONFIG_FILE, MQTT_CONFIG_FILE)
    mqtt.connect()

    input("\nMQTT listener running. Press Enter to exit.\n")

    # TODO - load profile and initialize main service loop here


if __name__ == '__main__':
    main()
