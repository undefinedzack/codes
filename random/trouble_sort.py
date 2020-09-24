testCases = int(input())

for i in range(testCases):
    length = int(input())
    arr = list(map(int, input().split(" ")))
    typez = list(map(int, input().split(" ")))

    for x in range(length-1):
        for y in range(x+1,length):
            if (arr[y] < arr[x]) and (typez[x] != typez[y]):
                #print('im here')
                temp = arr[y]
                arr[y] = arr[x]
                arr[x] = temp

                temp = typez[x]
                typez[x] = typez[y]
                typez[y] = temp

    copy = arr
    arr = tuple(arr)
    #print(arr)
    copy.sort()
    #print(copy)

    flag = 0
    for z in range(length):
        if copy[z] != arr[z]:
            flag = 1
            break
    if flag == 0:
        print('YES')
    else:
        print("NO")

