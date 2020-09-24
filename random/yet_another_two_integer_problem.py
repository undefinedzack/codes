testCases = int(input())

for _ in range(testCases):
    l = list(map(int, input().split(" ")))
    a , b = l[0] , l[1]

    knt = 0

    if a - b < 0:
        diff = b - a
        knt += int(diff/10)
        if diff % 10 != 0:
            knt += 1

    elif a - b > 0:
        diff = a - b
        knt += int(diff / 10)
        if diff % 10 != 0:
            knt += 1

    print(knt)
