import json
import sys

with open("metrics.json") as f:
    metrics = json.load(f)

accuracy = metrics.get("accuracy", 0.0)
print(f"Model Accuracy: {accuracy:.2f}")

if accuracy < 0.70:
    print("Quality gate failed: Accuracy is below 0.70 threshold")
    sys.exit(1)

print("Quality gate passed!")
