import csv

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from datetime import datetime
import joblib

x = [] # 2D array containing featueres
y = [] # array containing results, aka prices

first_skiped = False

def seconds_from_start_of_day(time_str):
    try:
        formatted_time = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S.%f")
        start_of_day = formatted_time.replace(hour=0, minute=0, second=0, microsecond=0)
        seconds_diff = (formatted_time - start_of_day).total_seconds()
        return seconds_diff
    except ValueError:
        print("Invalid time format. Please provide a valid format.")


# features [time_of_day, trip_distance]
def get_specific_entries(file_path):
    try:
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                if len(row) > 4:  # Check if there are enough entries
                    start_time = seconds_from_start_of_day(row[1])
                    duration = seconds_from_start_of_day(row[2])-start_time
                    distance = float(row[4])
                    fare_amount = row[10]
                    x.append([start_time, duration, distance])
                    y.append(int(float(fare_amount)*100))
                else:
                    print("Row doesn't have sufficient entries.")
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")

# Replace 'file_path.csv' with the path to your CSV file
file_path = './example_data.csv'
get_specific_entries(file_path)


rf_classifier = RandomForestClassifier(n_estimators=500, random_state=42)

rf_classifier.fit(x, y)

joblib.dump(rf_classifier, '../backend/saved_model.pkl')


## testing purposes
feature_importance = rf_classifier.feature_importances_

# Print feature importance
for i, importance in enumerate(feature_importance):
    print(f"Feature {i + 1}: Importance - {importance:.4f}")


# Perform cross-validation to get a more robust estimate of model performance
cv_scores = cross_val_score(rf_classifier, x, y, cv=5)  # 5-fold cross-validation
print(f'Cross-Validation Mean Accuracy: {cv_scores.mean():.2f}')
# Optionally, you can also print the individual cross-validation scores
print('Individual Cross-Validation Scores:')
for i, score in enumerate(cv_scores, 1):
    print(f'Fold {i}: {score:.2f}')


# start = seconds_from_start_of_day('2019-01-06 17:40:56.000000')
# duration = seconds_from_start_of_day('2019-01-06 17:47:56.000000')-start
# distance = 1.79

# print(rf_classifier.predict([[start, duration, distance], [start, duration+55, distance+1.2]]))


