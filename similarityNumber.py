testCases = int(input())

for i in range(testCases):
    string = str(input())
    total = 0
    n = len(string)


    while(n != 0):
        temp = string[len(string)-n:]
        t = n
        knt = 0
        while(1):
            if temp[:t] == string[:t]:
                knt += t
                break
            elif temp[0] != string[0]:
                knt += 0
                break
            else:
                t -= 1
        total += knt
        n -= 1

    print(total)