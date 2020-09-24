testCases = int(input())

for i in range(testCases):
    s = str(input())
    x = int(input())
    #print(len(s))
    arr = []
    for knt in range(len(s)):
        if s[knt] == '1':
            if knt >= x :
                arr.append([knt - x, 1])
            if knt + x < len(s) :
                arr.append([knt + x, 1])
        else:
            if knt >= x and  knt + x < len(s) :     # T and T
                arr.append([knt - x, 0])
                arr.append(([knt + x, 0]))

            elif knt >= x and knt + x >= len(s) :     #T and F
                arr.append([knt - x, 0])

            elif knt < x and knt + x < len(s):       #F and T
                arr.append([knt + x, 0])

    arr.sort()
    print(arr)
    index = 0
    output = ""
    flag = False
    for i in range(len(arr)):
        if arr[i][0] == index and index != 0 :
            continue
        elif arr[i][0] != index and index + 1 != arr[i][0] :
            print(arr[i][0])
            print(-1)
            flag = True
            break
        else:
            output += str(arr[i][1])
        index = arr[i][0]
        value = arr[i][1]

    if flag == False and index == len(s) - 1:
        print(output)
    else:
        print(-1)


