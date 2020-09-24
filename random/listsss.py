l = str(input('Enter list\n'))
l = list(map(int,l.split(" ")))

lPositive = []

for i in range(len(l)):
    if l[i] > 0:
        lPositive.append(l[i])

#Printing positive numbers
print('List with positive numbers:\n')
print(list(lPositive))