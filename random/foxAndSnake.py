temp = list(map(int,input().split(" ")))

n = temp[0]
m = temp[1]
flag = 0
for i in range(n):
        if i % 2 == 0: #even row
            #print('im here')
            for j in range(m):
                print("#",end="")
            print("")
        else: #odd row
            if flag == 0:
                for j in range(m-1):
                    print(".",end="")
                print('#')
                flag = 1
            else:
                print("#",end="")
                for j in range(1,m):
                    print(".",end="")
                print("")
                flag = 0

