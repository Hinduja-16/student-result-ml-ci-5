import json
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# Generate dummy training data
data = {
    "attendance": [90, 50, 85, 40, 95, 60, 80, 45, 88, 52],
    "internal_marks": [85, 30, 80, 25, 90, 40, 75, 35, 82, 38],
    "assignment_marks": [88, 40, 85, 30, 92, 45, 80, 38, 86, 42],
    "previous_score": [80, 35, 78, 30, 88, 50, 72, 40, 84, 45],
    "result": [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
}

df = pd.DataFrame(data)

X = df[["attendance", "internal_marks", "assignment_marks", "previous_score"]]
y = df["result"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

# Save the trained model artifact
joblib.dump(model, "student_result_model.pkl")

# Save evaluation metrics
metrics = {"accuracy": float(accuracy)}
with open("metrics.json", "w") as f:
    json.dump(metrics, f, indent=4)

print(f"Model training complete. Test Accuracy: {accuracy:.2f}")
