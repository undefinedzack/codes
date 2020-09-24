testCases = int(input())

for i in range(testCases):
    sides = list(map(int,input().split(" ")))
    sides.sort()
    a = sides[0]
    b=sides[1]

    if (2*a) < b:
        min = pow(b,2)
        print(min)
    else:
        min = pow(2*a,2)
        print(min)

