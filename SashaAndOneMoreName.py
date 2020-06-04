s = str(input())

def chkPalin(s):
    f = s[::-1]
    if s == f:
        return 1
    else:
        return 0

#even
if len(s)%2 == 0:
    if s[0] != s[ int((len(s)/2) - 1)]:
        print(1)
    else:
        t = int(len(s)/2)
        #print(s[:t])
        while chkPalin(s[:t]) != 0:
            t = int(t/2)
            if len(s[:t]) == 1:
                print('Impossible')
                break
            else:
                print(1)

#odd
else:
    t = int(len(s)/2)
    if chkPalin(s[:t]) != 1:
        print(2)
    else:
        while chkPalin(s[:t]) != 0:
            t = int(t / 2)
            if len(s[:t]) == 1:
                print('Impossible')
                break
            else:
                print(2)