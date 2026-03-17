# Data handling
import pandas as pd

# Train/test split
from sklearn.model_selection import train_test_split

# Model
from sklearn.ensemble import RandomForestClassifier

# Evaluation
from sklearn.metrics import accuracy_score, confusion_matrix

# Create dataset manually
data = {
    'N': [90, 85, 60, 74, 78, 69, 69, 94, 89, 68],
    'P': [42, 58, 55, 35, 42, 37, 55, 53, 54, 58],
    'K': [43, 41, 44, 40, 42, 38, 44, 40, 38, 40],
    'temperature': [20.8, 22.2, 23.0, 26.5, 24.0, 23.5, 25.0, 21.0, 22.5, 24.5],
    'humidity': [82, 80, 78, 75, 77, 76, 74, 83, 81, 79],
    'ph': [6.5, 6.4, 6.3, 6.7, 6.6, 6.5, 6.4, 6.8, 6.7, 6.6],
    'rainfall': [200, 180, 150, 120, 130, 140, 110, 210, 190, 160],
    'label': ['rice', 'rice', 'maize', 'maize', 'maize',
              'wheat', 'wheat', 'rice', 'rice', 'maize']
}

dataset = pd.DataFrame(data)

print(dataset.head())
# Split dataset into features and target variable
X = dataset.drop(columns=['label'])  # inputs
y = dataset['label']                 # output
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
#create model
model = RandomForestClassifier(n_estimators=100, random_state=42)
# Train the model
model.fit(X_train, y_train)
# make predictions
y_pred = model.predict(X_test)
# Evaluate the model
print("Predictions:", y_pred)
print("Accuracy:", accuracy_score(y_test, y_pred))

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
new_data = [[90, 40, 40, 21, 82, 6.5, 200]]

prediction = model.predict(new_data)

print("Recommended crop:", prediction)