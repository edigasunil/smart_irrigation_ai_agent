# data_ingestion.py
# This file simulates reading IoT sensor data + weather API

def read_soil_moisture():
    # simulate sensor value
    return 40  # example: 40% moisture

def read_weather_forecast():
    # simulate weather API
    return {"rain_expected": False, "temperature": 32}

if __name__ == "__main__":
    print("Soil moisture:", read_soil_moisture())
    print("Weather forecast:", read_weather_forecast())
