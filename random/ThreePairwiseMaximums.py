testCases = int(input())
def check(a,b,c):
    knt = 0
    x,y,z = a,b,c
    while 1:
        if max(a, b) == x:
            knt += 1
        else:
            if a == b:
                break
            temp = min(a, b)
            a = temp
            b = temp
            knt = 0
            continue
        if max(b, c) == y:
            knt += 1
        else:
            if a == b:
                break
            temp = min(b, c)
            b = temp
            c = temp
            knt = 0
            continue
        if max(c, a) == z:
            knt += 1
        else:
            if a == b:
                break
            temp = min(c, a)
            c = temp
            a = temp
            knt = 0
            continue
        break
    l = [a,b,c]
    if knt == 3:
        return l
    else:
        return False

for i in range(testCases):
    x,y,z = map(int,input().split(" "))

    a,b,c = x,y,z

    if check(a,b,c) == False:
        print('NO')
    else:
        print('YES')
        l = check(a,b,c)
        print(l[0],l[1],l[2])