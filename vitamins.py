testCases = int(input())
l = []
for i in range(testCases):
    temp = list(input().split(" "))
    for knt in range(len(temp[1])):
        oof = temp[1][knt]
        temp.append(oof)
    temp.pop(1)
    l.append(temp)
min = 9999999
l.sort(key=lambda x: int(x[0]) )
#print(l)
vit3 = ['ABC','BCA','CAB','ACB','BAC','CBA']
vit2 = ['AB','BA','BC','CB','CA','AC']
vit1 = ['A','B','C']
for h in range(len(l)):
    if int(l[h][0]) < min:
        if ('A' in l[h][1:]) and ('B' in l[h][1:]) and ('C' in l[h][1:]) :
            #print(l[h][1:])
            min = int(l[h][0])
for h in range(len(l)-1):
    for k in range(h+1,len(l)):
        if (int(l[h][0]) + int(l[k][0])) < min:
            if ('A' in (l[h][1:] + l[k][1:])) and ('B' in (l[h][1:] + l[k][1:])) and ('C' in (l[h][1:] + l[k][1:])):
                min = (int(l[h][0]) + int(l[k][0]))

for p in range(len(l)-2):
    for q in range(p+1,len(l)-1):
        for r in range(q+1,len(l)):
            if (int(l[p][0]) + int(l[q][0]) + int(l[r][0])) < min:
                if ('A' and 'B' and 'C') in (l[p][1:] + l[q][1:] + l[r][1:]):
                    min = (int(l[p][0]) + int(l[q][0]) + int(l[r][0]))

if min == 9999999:
    print(-1)
else:
    print(min)

