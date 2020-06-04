temp = list(map(int,input().split(" ")))
noOfWords = temp[0]
delay = temp[1]

secs = list(map(int,input().split(" ")))
knt = 0
for i in range(len(secs)-1):
    if secs[i+1] - secs[i] <= delay:
        knt += 1
    else:
        knt = 0
print(knt + 1)