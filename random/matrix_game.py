testCases = int(input())

for i in range(testCases):
    NM = list(map(int, input().split(" ")))
    n = NM[0]
    m = NM[1]
    l=[]
    for j in range(n):
        listy = list(map(int, input().split(" ")))
        l.append(listy)

    #print(l)
    knt = 0
    for x in range(n):
        for y in range(m):
            if l[x][y] == 0:
                for t in range(m):
                    l[x][t] = 1
                for t in range(n):
                    l[t][y] = 1
                knt += 1
    if knt % 2 == 0:
        print('Vivek')
    else:
        print('Ashish')