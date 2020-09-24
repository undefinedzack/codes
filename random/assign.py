
no_of_activities = int(input("Enter total no. of activities"))

class activity:
    pass
temp = activity()
temp.start=[]
temp.end=[]
for i in range(no_of_activities):
    temp.start.append(int(input("Enter starting time of activity {}".format(i+1))))
    temp.end.append(int(input("Enter ending time of activity {}".format(i+1))))

print(temp)
temp.end.sort()
print(temp.start,temp.end)
