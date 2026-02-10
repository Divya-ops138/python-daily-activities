name=input("Enter your name:")
n=int(input("Enter number of subjects: "))
marks=[]
for i in range(n):
    m=int(input("Enter marks: "))
    marks.append(m)
valid=0
fail=0
for mark in marks:
     if mark<0 or mark>100:
        result="Invalid"
     else:
        valid+=1
        if mark>=90:
           result="Excellent"
           if len(name)>5:
               result="Excellent "+name
        elif mark>=75:
           result="Very Good"
        elif mark>=60:
           result="Good"
        elif mark>=40:
           result="Average"
        else:
           result="Fail"
           fail += 1
        print(mark,"=",result)
print("Total valid students:",valid)
print("Total failed students:",fail)

