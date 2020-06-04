testCases = int(input())

for i in range(testCases):
    NMK = list(map(int,input().split(" ")))

    n = NMK[0]
    m = NMK[1]
    k = NMK[2]
    flag = 0
    if m == 0:
        print(0)
        flag = 1
    if flag == 0:
        if n/k > m:
            print(m)
        else:
            l = []
            for i in range(k):
                l.append(0)
            l[0] = int(n/k)
            m -= int(n/k)
            i = 1
            while m>0:
                if i == 0:
                    i += 1
                l[i] += 1
                i = (i + 1)%(k)
                m -= 1
            l.sort(reverse=True)
            print(l[0]-l[1])


