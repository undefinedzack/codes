testCases = int(input())
def same(l):
    diff = 9999999
    for i in range(len(l)-1):
        if l[i] == l[i+1]:
            return -1
        else:
            if abs(l[i+1] - l[i]) < diff:
                diff = abs(l[i+1] - l[i])
    return diff
for i in range(testCases):
    totalAtheletes = int(input())
    strengths = list(map(int,input().split(" ")))

    strengths.sort()
    res = same(strengths)
    if res == -1:
        print(0)
    else:
        print(res)


