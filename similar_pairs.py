testCases = int(input())

for i in range(testCases):
    limit = int(input())
    arr = list(map(int,input().split(" ")))

    odd = []
    even = []

    for item in arr:
        if item % 2 == 0:
            even.append(item)
        else:
            odd.append(item)

    if len(odd) % 2 == 0 and len(even) % 2 == 0:
        print('YES')
    else:
        flag = 0
        for h in odd:
            for k in even:
                if abs(h-k) == 1:
                    print('YES')
                    flag = 1
                    break
        if flag == 0:
            print('NO')
