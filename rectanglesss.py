noOfRectangles = int(input())
p = []
for i in range(noOfRectangles):
    l = []
    landb = list(map(int,input().split(" ")))
    l.append(landb[0])
    l.append(landb[1])
    l.sort()
    p.append(l)
knt = 0
highest = p[0][1]
for i in range(1,noOfRectangles):
    if p[i][1] <= highest:
        knt += 1
        highest = p[i][1]
        continue
    else:

        p[i].reverse()
        #print(list(p))
        if p[i][1] <= highest:
            knt += 1
            highest = p[i][1]
            continue
        else:
            break

if knt == noOfRectangles-1:
    print('YES')
else:
    print('NO')