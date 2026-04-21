import random
import pandas as pd
import numpy as np
import math

def generate_data(n=18):
    data = []
    for i in range(1, n+1):
        data.append({
            "zone": i,
            "traffic": random.randint(0, 100),
            "air_quality": random.randint(0, 300),
            "energy": random.randint(0, 500)
        })
    data.append({"zone": 99, "traffic": 0, "air_quality": 50, "energy": 100})
    data.append({"zone": 100, "traffic": 95, "air_quality": 280, "energy": 450})
    data.append({"zone": 101, "traffic": 40, "air_quality": 120, "energy": 480})
    return data

def categorize(record):
    if record["air_quality"] > 200 or record["traffic"] > 80:
        return "High Risk"
    elif record["energy"] > 400:
        return "Energy Critical"
    elif record["traffic"] < 30 and record["air_quality"] < 100:
        return "Safe Zone"
    else:
        return "Moderate"

def calculate_risk(record):
    return (record["air_quality"] * 0.45 +
            record["traffic"] * 0.35 +
            record["energy"] * 0.2)

def bubble_sort(data):
    arr = data[:]
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j]["risk_score"] < arr[j+1]["risk_score"]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def detect_patterns(df):
    threshold = df["risk_score"].mean()
    high_risk = df[(df["risk_score"] > threshold) & (df["air_quality"] > df["air_quality"].shift(1))]
    stability = df["traffic"].var() < 500
    clusters = []
    temp = []
    for _, row in df.iterrows():
        if row["risk_score"] > threshold:
            temp.append(row["zone"])
        else:
            if len(temp) > 1:
                clusters.append(temp)
            temp = []
    if len(temp) > 1:
        clusters.append(temp)
    return high_risk, stability, clusters

roll_number = 23
data = generate_data()

if roll_number % 3 == 0:
    random.shuffle(data)
else:
    data = sorted(data, key=lambda x: x["traffic"])

for d in data:
    d["category"] = categorize(d)
    d["risk_score"] = calculate_risk(d)

df = pd.DataFrame(data)
np_array = df[["traffic", "air_quality", "energy"]].values
means = np.mean(np_array, axis=0)
df["sqrt_risk"] = df["risk_score"].apply(lambda x: math.sqrt(x))

sorted_data = bubble_sort(data)
top3 = sorted_data[:3]

risk_tuple = (
    df["risk_score"].max(),
    df["risk_score"].mean(),
    df["risk_score"].min()
)

unique_categories = set(df["category"])
high_risk, stability, clusters = detect_patterns(df)

avg = risk_tuple[1]
if avg < 100:
    decision = "City Stable"
elif avg < 180:
    decision = "Moderate Risk"
elif avg < 250:
    decision = "High Alert"
else:
    decision = "Critical Emergency"

print("\n--- DataFrame ---")
print(df)
print("\n--- Mean Values ---")
print(means)
print("\n--- Top 3 Risk Zones ---")
for z in top3:
    print(z)
print("\n--- Risk Tuple ---")
print(risk_tuple)
print("\n--- Unique Categories (Set) ---")
print(unique_categories)
print("\n--- Pattern Detection ---")
print("High Risk Zones:\n", high_risk)
print("Stability:", stability)
print("Clusters:", clusters)
print("\n--- Final Decision ---")
print(decision)
print("\n--- Smart City Insight ---")
print("A smart city is one where pollution is controlled, traffic is stable,")
print("and risks are predictable rather than reactive.")