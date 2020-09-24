string = str(input())

w = 'vv'

def findw(startingVertex, endVertex, string):
    leftVs = 0
    rightVs = 0
    l = []
    for i in range(startingVertex - 1,0,-1):
        if (string[i] + string[i-1]) == w:
            leftVs += 1
    for i in range(endVertex,len(string)-1):
        if (string[i] + string[i + 1]) == w:
            rightVs += 1

    l.append(leftVs)
    l.append(rightVs)
    return l

def findo(string , done):
    startingVertex = -1
    endVertex = -1
    l = []
    for i in range(len(string)):
        if string[i] == 'o' and done[i] == False:
            startingVertex = i
            done[i] = True
        else:
            continue
        i += 1
        if i == len(string):
            i -= 1
        while string[i] == 'o' and done[i] == False:
            done[i] = True
            i += 1
            if i == len(string):
                break
        endVertex = i - 1
        break
    l.append(startingVertex)
    l.append(endVertex)
    return l


done = []
for i in range(len(string)):
    done.append(False)

fin =0

while 1:
    res = list(findo(string,done))
    wSSS = list(findw(res[0] , res[1] , string))
    if res[0] == -1 and res[1] == -1:
        break
    else:
        fin += (res[1] - res[0] + 1) *  wSSS[0] * wSSS[1]

print(fin)
