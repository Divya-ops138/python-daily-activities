import copy

# Step 1: Generate Data
def generate_data():
    return [
        {"id": 1, "data": {"files": ["a.txt", "b.txt"], "usage": 500}},
        {"id": 2, "data": {"files": ["c.txt"], "usage": 300}}
    ]


# Step 2: Replication (assignment, shallow, deep)
def replicate_data(original):
    assigned = original                      # Assignment (same reference)
    shallow = copy.copy(original)            # Shallow copy (outer only)
    deep = copy.deepcopy(original)           # Deep copy (full copy)

    # Show memory difference
    print("\n--- MEMORY CHECK ---")

    print("Outer List IDs:")
    print("Original:", id(original))
    print("Assigned:", id(assigned))
    print("Shallow :", id(shallow))
    print("Deep    :", id(deep))

    print("\nInner List IDs (files of first user):")
    print("Original:", id(original[0]["data"]["files"]))
    print("Assigned:", id(assigned[0]["data"]["files"]))
    print("Shallow :", id(shallow[0]["data"]["files"]))
    print("Deep    :", id(deep[0]["data"]["files"]))

    return assigned, shallow, deep


# Step 3: Modify Data (Personalized Logic)
def modify_data(data, roll_number):
    is_even = int(roll_number[-1]) % 2 == 0

    for user in data:
        if is_even:
            user["data"]["files"].append("new.txt")   # EVEN
        else:
            if user["data"]["files"]:
                user["data"]["files"].pop()           # ODD

        user["data"]["usage"] += 100


# Step 4: Integrity Check
def check_integrity(original_before, original_after, shallow, deep):
    leakage_count = 0
    safe_count = 0
    overlap_count = 0

    for i in range(len(original_before)):

        # 🔴 Data Leakage (original changed unexpectedly)
        if original_before[i]["data"] != original_after[i]["data"]:
            leakage_count += 1

        # 🟢 Deep Copy Safety
        if deep[i]["data"] != original_after[i]["data"]:
            safe_count += 1

        # 🔁 Overlap Detection using SET
        orig_files = set(original_after[i]["data"]["files"])
        shallow_files = set(shallow[i]["data"]["files"])
        overlap = orig_files.intersection(shallow_files)
        overlap_count += len(overlap)

    return (leakage_count, safe_count, overlap_count)




roll_number = "AP24110011717"   # ODD → delete file

# BEFORE
original = generate_data()
original_before = copy.deepcopy(original)

print("BEFORE MODIFICATION:")
print("Original:", original)

# Replication
assigned, shallow, deep = replicate_data(original)

# Modify ONLY shallow (to show leakage clearly)
modify_data(shallow, roll_number)

# AFTER
print("\nAFTER MODIFICATION:")
print("Original (affected due to shallow):", original)
print("Assigned (same reference):", assigned)
print("Shallow Copy:", shallow)
print("Deep Copy (safe):", deep)

# Integrity Report
report = check_integrity(original_before, original, shallow, deep)

print("\nINTEGRITY REPORT:")
print("Leakage Count:", report[0])
print("Safe Count:", report[1])
print("Overlap Count:", report[2])

print("\nFinal Tuple:", report)