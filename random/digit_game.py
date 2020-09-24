testCases = int(input())

for _ in range(testCases):
    n = int(input())
    number = str(input())

    even = []
    odd = []
    if len(number)%2 == 0:
        print(2)


    if len(even) > len(odd):
        print(2)
    elif len(odd) > len(even):
        print(1)
    else:
        print(2)

