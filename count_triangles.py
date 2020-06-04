ABCD = list(map(int,input().split(" ")))

a,b,c,d=ABCD[0],ABCD[1],ABCD[2],ABCD[3]

def isTRi(a,b,c):
    cnt = 0
    if a+b>c:
        cnt +=1
    if b+c>a:
        cnt +=1
    if c+a>b:
        cnt +=1
    if cnt == 3:
        return 1
    else:
        return 0
knt = 0
for i in range(a,b+1):
    for j in range(b,c+1):
        for k in range(c,d+1):
            if isTRi(i,j,k) == 1:
                knt += 1

print(knt)