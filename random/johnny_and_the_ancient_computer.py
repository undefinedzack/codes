testCases = int(input())

for i in range(testCases):
    AB = list(map(int,input().split(" ")))
    AB.sort()
    a = AB[0]
    b = AB[1]
    knt = 0
    flag1 = 0
    flag2 = 0
    while a != b:
        if a == b:
            print(0)
            flag1 = 1
            break
        if b/a % 2 == 0:
            if (b/a) % 8 == 0:
                b /= 8
                knt += 1
            elif (b/a) % 4 == 0:
                b /= 4
                knt += 1
            else:
                b /= 2
                knt += 1
        else:
            print(-1)
            flag2 = 1
            break
    if flag1==0 and flag2==0:
        print(knt)


