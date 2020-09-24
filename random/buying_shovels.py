testCases = int(input())

for i in range(testCases):
    temp = list(map(int,input().split(" ")))

    n = temp[0]
    k = temp[1]

    if n <= k:
        print(1)
    else:
        for i in range(1,n+1):
            print(n/i)
            if (n/i) <= k:
                print( int( 8/(int(n/i) )) )
                break
