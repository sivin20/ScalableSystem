import random
from models import Weather
from price.mockData import mockdata
from datetime import datetime
from sklearn.ensemble import RandomForestClassifier
import joblib


def seconds_from_start_of_day():
    try:
        current_time = datetime.now()
        start_of_day = current_time.replace(hour=0, minute=0, second=0, microsecond=0)
        seconds_diff = (current_time - start_of_day).total_seconds()
        return seconds_diff
    except ValueError:
        print("Invalid time format. Please provide a valid format.")



# Load the model from the file

def calculatePrice(start: int, duration: int, distance: int):
    print('Load model')
    rf_classifier:RandomForestClassifier = joblib.load('saved_model.pkl')
    print('start', start)
    print('duration', duration)
    print('distance', distance)
    prediction = rf_classifier.predict([[start, duration, distance]])
    return {"price":float(prediction[0])/100}