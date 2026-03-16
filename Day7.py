# Smart Campus Energy Monitor
# Name: Divya Jyothi
print("Smart Campus Energy System")
readings = list(map(int, input("Enter energy readings separated by space: ").split()))

usage = {
    "efficient": [],
    "moderate": [],
    "high": [],
    "invalid": []
}
for e in readings:
    if e < 0:
        usage["invalid"].append(e)
    elif e <= 50:
        usage["efficient"].append(e)
    elif e <= 150:
        usage["moderate"].append(e)
    else:
        usage["high"].append(e)

valid = [x for x in readings if x >= 0]

total = sum(valid)
count = len(readings)
summary = (total, count)

if len(usage["high"]) > 3:
    result = "Energy Waste Detected"
elif abs(len(usage["efficient"]) - len(usage["moderate"])) <= 1:
    result = "Efficient Campus"
elif total > 600:
    result = "Energy Waste Detected"
else:
    result = "Moderate Usage"

print("\n--- Energy Report ---")
print("Usage:", usage)
print("Summary:", summary)
print("Final Result:", result)

print("\nThank you for using Smart Campus Monitor")