total = int(input())

l =  list(map(int,input().split(" ")))

l.sort()
knt = 0
for i in range(len(l)-1):
    if l[i+1] - l[i] == 1:
        continue
    else:
        add = l[i+1] - l[i] - 1
        knt += add

print(knt)