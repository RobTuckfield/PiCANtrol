# PiCANtrol

**PiCANtrol** is an open-source, modular interface platform that connects a Raspberry Pi to your car's CAN bus via an OBD-II adapter. It provides a lightweight API-like layer for sending and receiving CAN messages, with support for vehicle-specific profiles and safe remote control.

---

## What It Does

- Provides a general-purpose way to interact with your car's CAN bus
- Uses MQTT for remote command/control (ideal for mobile apps, dashboards, automations)
- Reads and writes CAN messages based on declarative YAML vehicle profiles
- Extensible to any car with community-contributed profiles
- Starts with support for the 2017 Chevy Volt

---

## Goals

- **Modular**: Vehicle support is defined through YAML profiles - no coding required
- **Flexible Transport**: Supports CAN over SocketCAN, USB-CAN adapters, or Bluetooth OBD-II dongles
- **Remote Friendly**: MQTT-based control lets you trigger actions from a mobile app or the cloud
- **Safety First**: Movement-related actions (e.g. throttle, steering) are prohibited by policy
- **Open Source**: Built to encourage community learning and contribution

---

## Current Status

This project is currently *NON-FUNCTIONAL*. Initial build-out is being performed currently. 

---

## Project Structure

PiCANtrol/
├── core/ # Core logic for CAN and MQTT
├── vehicles/ # YAML profiles for each supported vehicle
├── utils/ # Helpers for decoding and config
├── config/ # MQTT and system configuration
├── cli/ # Optional local test runner
├── tests/ # Unit tests
└── README.md

---

## Planned Minimum Viable Product (MVP)

The planned MVP is to allow reading basic stats from a 2017 Chevy Volt and post these stats to a defined MQTT server. Additionally, the program should be able to successfully send a remote start command to the same 2017 Chevy Volt.

---

## Disclaimers and Safety

> **WARNING:** This software interacts with your vehicle's internal communication systems. Use at your own risk. You could damage your car, void warranties, or cause unsafe conditions if misused.

- **NEVER** send commands that affect motion (e.g. steering, acceleration, braking)
- Commands that affect vehicle movement are **not allowed** in this project
- For security, always encrypt MQTT traffic and authenticate clients

---

## Getting Started

Coming Soon.

## Supported Vehicles

The Gen2 Chevy Volt is the first vehicle planned to be supported. More can be added by defining the CAN codes used. Adding and testing these codes is a great way to contribute.

---

## Contributing

We welcome contributions! You can:

Add a new vehicle profile under vehicles/<make_model_year>/profile.yaml

Improve the documentation or error handling

Help build out new transport layers or dashboards