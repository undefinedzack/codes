noOfLines = int(input())
noOfBirdsOnEachLine = list(map(int,input().split(" ")))

totalShotsFired = int(input())

for i in range(totalShotsFired):
    temp = list(map(int,input().split(" ")))
    iTHline = temp[0]-1
    birdShotIndex = temp[1]-1
    #print(birdShotIndex)
    if iTHline != 0 and iTHline != noOfLines-1:
        noOfBirdsOnEachLine[iTHline-1] += birdShotIndex
        noOfBirdsOnEachLine[iTHline+1] += (noOfBirdsOnEachLine[iTHline] - (birdShotIndex + 1) )
        noOfBirdsOnEachLine[iTHline] = 0


    elif iTHline == 0:
        if noOfLines != 1:
            noOfBirdsOnEachLine[iTHline + 1] += (noOfBirdsOnEachLine[iTHline] - (birdShotIndex + 1))
            noOfBirdsOnEachLine[iTHline] = 0
        else:
            noOfBirdsOnEachLine[iTHline] = 0

    elif iTHline == noOfLines-1:
        if noOfLines != 1:
            noOfBirdsOnEachLine[iTHline - 1] += birdShotIndex
            noOfBirdsOnEachLine[iTHline] = 0
        else:
            noOfBirdsOnEachLine[iTHline] = 0
for i in noOfBirdsOnEachLine:
    print(i)