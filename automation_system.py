import time
import random

class SmartAutomation:
    def __init__(self):
        self.system_status = "Initialized"
        print("[SYSTEM] Smart Automation Core Running...")

    def read_sensors(self):
        # Simulating data extraction from hardware sensors
        temperature = round(random.uniform(20.0, 35.0), 2)
        humidity = round(random.uniform(40.0, 70.0), 2)
        return {"temperature": temperature, "humidity": humidity}

    def process_control_logic(self, data):
        # Automated logic loop for environment control
        if data["temperature"] > 30.0:
            return "Activating Cooling System (Fan/AC)"
        elif data["temperature"] < 22.0:
            return "Activating Heating System"
        else:
            return "Environment Stable - Energy Saving Mode Active"

    def run_dashboard(self):
        try:
            for _ in range(5):
                sensor_data = self.read_sensors()
                action = self.process_control_logic(sensor_data)
                
                print(f"\n--- Monitoring Node ---")
                print(f"Temp: {sensor_data['temperature']}°C | Humidity: {sensor_data['humidity']}%")
                print(f"Action: {action}")
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n[SYSTEM] Automation execution paused safely.")

if __name__ == "__main__":
    app = SmartAutomation()
    app.run_dashboard()
