n = int(input())

arr = list(map(int,input().split(" ")))

def oddlen(arr):
    if sum(arr)%2 != 0:
        return
    else:
        me = arr.pop(0)
        oddlen(arr)
        arr.insert(0,me)




def whowins(arr):
    if sum(arr)%2 != 0:
        print('First')
        return 0
    else:
        odd = []
        even = []
        for item in arr:
            if item%2 == 0:
                even.append(item)
            else:
                odd.append(item)
        if len(odd)>len(even):
            print('First')
        else:
            print('Second')

whowins(arr)