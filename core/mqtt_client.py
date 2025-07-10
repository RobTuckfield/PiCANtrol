import os
import yaml
import paho.mqtt.client as mqtt

class MQTTClient:
    def __init__(self, system_config_path, mqtt_config_path):
        with open(system_config_path) as f:
            system_cfg = yaml.safe_load(f)
            self.vehicle_id = system_cfg.get("vehicle_id")
            self.vehicle_profile = system_cfg.get("vehicle_profile")

        with open(mqtt_config_path) as f:
            mqtt_cfg = yaml.safe_load(f)

        self.broker = mqtt_cfg["broker"]
        self.port = mqtt_cfg.get("port", 1883)
        self.username = mqtt_cfg.get("username")
        self.password = mqtt_cfg.get("password")
        self.prefix = mqtt_cfg.get("topic_prefix", "picantrol")

        self.client = mqtt.Client()

        if self.username:
            self.client.username_pw_set(self.username, self.password)
        if mqtt_cfg.get('use_tls'):
            self.client.tls_set()
            if mqtt_cfg.get("insecure_tls"):
                self.client.tls_insecure_set(True)
        
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

        self.profile = self.load_vehicle_profile()
        #print(self.profile)
        
    def load_vehicle_profile(self):
        path = os.path.join("vehicles", self.vehicle_profile, "profile.yaml")
        with open(path) as f:
            return yaml.safe_load(f)
        

    def connect(self):
        print(f"Connecting to MQTT broker at {self.broker}:{self.port}...")
        self.client.connect(self.broker, self.port, 60)
        self.client.loop_start()

    def on_connect(self, client, userdata, flags, rc):
        print("MQTT connected with result code", rc)
        topic = f"{self.prefix}/{self.vehicle_id}/command/#"
        print(f"Subscribing to command topic: {topic}")
        client.subscribe(topic)

    def on_message(self, client, userdata, msg):
        print(f"[MQTT] Received on {msg.topic}: {msg.payload.decode()}")
        command = msg.topic.split('/')[-1]
        print(command)
        command_def = self.profile['commands'].get(command)
        print(command_def)

        if not command_def:
            print(f"[ERROR] Command not valid for this vehicle: {command}")
            return
        
        can_id = command_def['id']
        data = command_def['data']
        # TODO: Hook into message router or command dispatcher