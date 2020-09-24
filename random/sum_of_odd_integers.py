testCases = int(input())

for i in range(testCases):
    NK = list(map(int, input().split(" ")))
    n = NK[0]
    k = NK[1]
    knt = 3
    arr = [1]
    while 1:
        if sum(arr) <= n:
            arr.append(knt)
            knt += 2
        else:
            arr.pop()
            break

    if n>k:
        if n%2 == 0:
            if k%2 == 0 and k <= len(arr):
                print('YES')
            else:
                print('NO')
        else:
            if k%2 != 0 and k <= ((n-1)/2):
                print('YES')
            else:
                print('NO')
    else:
        print('NO')