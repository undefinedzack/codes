s = str(input())
t = str(input())

sR = s[::-1]
tR = t[::-1]
#print(sR,tR)
i= 0
knt = 0
while 1:
    if i <= len(sR)-1 and i<= len(tR)-1:
        if sR[i] == tR[i]:
            knt += 1
        else:
            break
    else:
        break
    i += 1

print(len(s)+len(t)-(2*knt))