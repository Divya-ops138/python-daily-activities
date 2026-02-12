data = [10, "Python", "", 25, "Loop", 40]
number_list = []
string_list = []
num_count = 0
str_count = 0
for item in data:
    if type(item) == int:
        number_list.append(item)
        num_count += 1
    elif type(item) == str:
        if item != "":
            string_list.append(item)
            str_count += 1

# Personalization Option B
# Name Length Logic
name = "Divya Jyothi"
if len(name) % 2 == 0:
    if len(number_list) > 0:
        number_list.pop(0)
    if len(string_list) > 0:
        string_list.pop(0)
else:
    if len(number_list) > 0:
        number_list.pop()
    if len(string_list) > 0:
        string_list.pop()
print("Numbers List:", number_list)
print("Strings List:", string_list)
print("Total Numbers:", num_count)
print("Total Strings:", str_count)
