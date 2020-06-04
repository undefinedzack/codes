import math

testCases = int(input())
for i in range(testCases):
    noOfItems = int(input())

    itemPrices = list(map(int,input().split(" ")))

    sumOfPrices = sum(itemPrices)
    #print(sumOfPrices)

    feasible = sumOfPrices/noOfItems
    afterDecimal , beforeDecimal = math.modf(feasible)
    #print(beforeDecimal,afterDecimal)
    if afterDecimal == 0:
        print(int(feasible))
    else:
        print(int(feasible)+1)