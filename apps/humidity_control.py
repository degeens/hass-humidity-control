from appdaemon.plugins.hass import Hass
import datetime

class HumidityControl(Hass):
    def initialize(self):
        """Initialize the humidity control app"""
        
        # Get required parameters
        self.temp_sensor = self.args.get("temperature_sensor")
        self.humidity_sensor = self.args.get("humidity_sensor") 
        self.dehumidifier_switch = self.args.get("dehumidifier_switch")
        
        # Validate required parameters
        if not all([self.temp_sensor, self.humidity_sensor, self.dehumidifier_switch]):
            self.log("ERROR: Missing required parameters. Need temperature_sensor, humidity_sensor, and dehumidifier_switch", level="ERROR")
            return
            
        self.log(f"Humidity Control initialized with:")
        self.log(f"  Temperature sensor: {self.temp_sensor}")
        self.log(f"  Humidity sensor: {self.humidity_sensor}")
        self.log(f"  Dehumidifier switch: {self.dehumidifier_switch}")
        
        # Schedule logging every minute
        self.run_every(self.log_sensors, "now", 60)
        
    def log_sensors(self, kwargs):
        """Log the configured sensor and switch IDs"""
        
        # Get current states
        temp_state = self.get_state(self.temp_sensor)
        humidity_state = self.get_state(self.humidity_sensor)
        switch_state = self.get_state(self.dehumidifier_switch)
        
        self.log(f"Temperature sensor ID: {self.temp_sensor} (State: {temp_state})")
        self.log(f"Humidity sensor ID: {self.humidity_sensor} (State: {humidity_state})")
        self.log(f"Dehumidifier switch ID: {self.dehumidifier_switch} (State: {switch_state})")