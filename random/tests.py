import random
length = 12
arr = [ [0 for i in range(length)] for j in range(length) ]
for i in range(length):
    for j in range(length):
        if i != j:
            arr[i][j] = random.randint(1,50)
            arr[j][i] = arr[i][j]

for i in range(length):
    for j in range(length):
        print(arr[i][j],end=" ")
    print()