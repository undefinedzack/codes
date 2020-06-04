testCases = int(input())

for i in range(testCases):
    NMXY = list(map(int,input().split(" ")))
    n,m,x,y = NMXY[0],NMXY[1],NMXY[2],NMXY[3]
    l = []
    for j in range(n):
        temp = str(input())
        l.append(temp)
    #print(l)
    cost = 0
    for k in range(n):
        knt = 0
        while knt < len(l[k]):
            if knt+2 <= len(l[k])+1:
                #print(l[k][knt:knt+2])
                if l[k][knt:knt+2] == '..':
                    if y < 2*x:
                        cost += y
                        #print(cost)
                    else :
                        cost += 2*x
                    #print(knt,'*****')
                    knt += 2


            if knt < len(l[k]):
                if l[k][knt] == '*':
                    knt += 1
            if knt+1 < len(l[k]):
                if l[k][knt] == '.' and l[k][knt+1]=='*':
                    cost += x
                    knt += 1
            if len(l[k]) == 1:
                if l[k][knt] == '.':
                    cost += x
                    knt +=1

    print(cost)