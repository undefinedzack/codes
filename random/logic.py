testCases = int(input())

for i in range(testCases):
    num = int(input())

    if num % 2 == 0: #even
        mul = num / 2
        res = num * mul
        print(int(res))

    else: #odd
        dup = num
        dup += 1
        mul = dup / 2
        res = num * mul
        print(int(res))

