# decision_engine.py
# Uses model + data to decide irrigation

from data_ingestion import read_soil_moisture, read_weather_forecast
from model_training import train_model

def decide_irrigation():
    model = train_model()
    soil = read_soil_moisture()
    weather = read_weather_forecast()

    if soil < model["moisture_threshold"] and not weather["rain_expected"]:
        return "Irrigation needed 💧"
    else:
        return "No irrigation required ✅"

if __name__ == "__main__":
    decision = decide_irrigation()
    print("Decision:", decision)
