testCases = int(input())

def remSame(l):
    k = len(l)
    knt = 0
    for i in range(k-1):
        print(i,k)
        if l[i-knt] == l[i+1-knt]:
            l.pop(i)
            knt += 1
    return l

for i in range(testCases):
    ranksANDmaxMatches = list(map(int,input().split(" ")))

    ranks = ranksANDmaxMatches[0]
    maxMatchesToBePlayed = ranksANDmaxMatches[1]

    rankList= list(map(int,input().split(" ")))

    rankList = remSame(rankList)
    print(rankList)