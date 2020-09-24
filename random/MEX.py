NX = list(map(int,input().split(" ")))

n = NX[0]
x = NX[1]

arr = list(map(int,input().split(" ")))
arr.sort()
k = 0
for i in range(len(arr)):
    if x <= arr[i]:
        if x == arr[i]:
            k += 1
            if len(arr)==1:
                break
        if i-1 > -1:
            k += x-arr[i-1]-1
            break
        else:
            if x == arr[i]:
                k += arr[i]
                break
            k += arr[i] - x - 1
            break

print(k)