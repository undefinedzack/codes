ties = int(input())
scarves = int(input())
vests = int(input())
jackets = int(input())

costOfType1 = int(input())
costOfType2 = int(input())

knt = 0
maxCost = 0
if costOfType2 > costOfType1:
    while scarves > 0 and vests > 0 and jackets > 0:
        scarves -= 1
        vests -= 1
        jackets -= 1
        knt += 1
    maxCost += (knt * costOfType2)

    knt = 0

    while ties > 0 and jackets > 0:
        ties -= 1
        jackets -= 1
        knt += 1
    maxCost += (knt * costOfType1)
    print(maxCost)
else:
    while ties > 0 and jackets > 0:
        ties -= 1
        jackets -= 1
        knt += 1
    maxCost += (knt * costOfType1)

    knt = 0

    while scarves > 0 and vests > 0 and jackets > 0:
        scarves -= 1
        vests -= 1
        jackets -= 1
        knt += 1
    maxCost += (knt * costOfType2)
    print(maxCost)