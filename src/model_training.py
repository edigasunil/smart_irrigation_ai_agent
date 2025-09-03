# model_training.py
# A simple ML-like rule (not real training for simplicity)

from data_ingestion import read_soil_moisture, read_weather_forecast

def train_model():
    # In real AI, you'd train with data
    # Here we just return a simple rule model
    model = {
        "moisture_threshold": 30,   # irrigation needed if below 30%
        "temperature_threshold": 35
    }
    return model

if __name__ == "__main__":
    model = train_model()
    print("Trained model:", model)
