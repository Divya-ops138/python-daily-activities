student_id=input("Enter student number: ")
email=input("Enter email: ")
password=input("Enter password: ")
referral=input("Enter referral: ")
valid=True
if len(student_id)!=7:
   valid=False
elif not student_id.startswith("CSE"):
   valid=False
elif  student_id[3]!="-":
   valid=False
elif not student_id[4:7].isdigit():
   valid=False
elif "@" not in email or "." not in email:
   valid = False
elif email.startswith("@") or email.endswith("@"):
   valid = False
elif not email.endswith(".edu"):
   valid = False
elif len(password) < 8:
   valid = False
elif not password[0].isupper():
   valid = False
elif (
       not password[1].isdigit()
       and not password[2].isdigit()
       and not password[3].isdigit()
       and not password[4].isdigit()
       and not password[5].isdigit()
       and not password[6].isdigit()
       and not password[7].isdigit()
):
   valid = False
elif len(referral) != 6:
   valid = False
elif not referral.startswith("REF"):
   valid = False
elif not referral[3:5].isdigit():
   valid = False
elif not referral.endswith("@"):
   valid = False
if valid:
   print("APPROVED")
else:
   print("REJECTED")


