weights = [4, 18, 70, -2, 30, 55, 0]
very_light = []
normal_load = []
heavy_load = []
overload = []
invalid_entries = []
for w in weights:
    if w < 0:
        invalid_entries.append(w)
    elif w <= 5:
        very_light.append(w)
    elif w <= 25:
        normal_load.append(w)
    elif w <= 60:
        heavy_load.append(w)
    else:
        overload.append(w)
# personalization
name = "Divya Jyothi"
L = 0
for ch in name:
    if ch != " ":
        L = L + 1
PLI = L % 3
affected = 0
if PLI == 0:
    for x in overload:
        invalid_entries.append(x)
        affected = affected + 1
    overload = []
elif PLI == 1:
    for x in very_light:
        affected = affected + 1
    very_light = []
else:
    for x in very_light:
        affected = affected + 1
    for x in overload:
        affected = affected + 1
    very_light = []
    overload = []
valid = 0
for x in very_light:
    valid = valid + 1
for x in normal_load:
    valid = valid + 1
for x in heavy_load:
    valid = valid + 1
for x in overload:
    valid = valid + 1
print("L:", L)
print("PLI:", PLI)
if PLI == 0:
    print("Rule A applied")
elif PLI == 1:
    print("Rule B applied")
else:
    print("Rule C applied")
print("Valid weights:", valid)
print("Affected items:", affected)
print("Very Light:", very_light)
print("Normal:", normal_load)
print("Heavy:", heavy_load)
print("Overload:", overload)
print("Invalid:", invalid_entries)
