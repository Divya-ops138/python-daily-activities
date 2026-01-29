full_name = input("Enter your name")
email = input("Enter your email")
mobile = input("Enter your mobile number")
age = int(input("Enter your age"))
valid = True
if full_name.startswith(" ") or full_name.endswith(" "):
    valid = False
elif full_name.count(" ") < 1:
    valid = False

elif email.count("@") != 1 or email.count(".") < 1:
    valid = False
elif email.startswith("@"):
    valid = False
elif len(mobile) != 10:
    valid = False
elif not mobile.isdigit():
    valid = False
elif mobile.startswith("0"):
    valid = False
elif age < 18 or age > 60:
    valid = False
if valid:
    print("User Profile is VALID")
else:
    print("User Profile is INVALID")
