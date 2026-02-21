reg_no = input("Enter registration number: ")
n = int(input("Enter number of seconds: "))
lst = []
for i in range(n):
    duration = int(input("Enter durations: "))
    if duration <= 0:
        print("Invalid Playlist")
        exit()
    lst.append(duration)
total = sum(lst)
songs = len(lst)
repetitive = False
for d in lst:
    if lst.count(d) > 1:
        repetitive = True
        break
variation = max(lst) - min(lst)

#PERSONALIZATION USING REG NO
num = int(reg_no[-1])
if num % 2 == 0:
    style = "Calm Listener"
else:
    style = "Energetic Listener"
if total < 300:
    category = "Too Short Playlist"
    recommendation = "Add more songs"
elif total > 3600:
    category = "Too Long Playlist"
    recommendation = "Reduce playlist"
elif repetitive:
    category = "Repetitive Playlist"
    recommendation = "Add variety"
else:
    if variation <= 300:
        category = "Balanced Playlist"
        recommendation = "Good listening session"
    else:
        category = "Irregular Playlist"
        recommendation = "Adjust playlist"


print("\nReg No:", reg_no)
print("Listening Style:", style)
print("\nTotal Duration:", total, "seconds")
print("Songs:", songs)
print("Category:", category)
print("Recommendation:", recommendation)