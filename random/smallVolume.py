testCases = int(input())

for i in range(testCases):
    l = int(input())

    if l == 1:
        print(1)

    else:
        total = pow(l,3)
        left = pow(l-2,3)

        res = total - left
        print(res)