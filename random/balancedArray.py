testCases = int(input())

for i in range(testCases):
    sum = int(input())

    evenCount = 0
    oddCount = 0
    even = []
    odd = []
    knt = 0

    j = 0
    while evenSum<sum and oddSum<sum:
        evenCount += 2
        even.append(evenCount)
        oddCount += 1
        knt += 1
        if evenSum == sum:
            break

