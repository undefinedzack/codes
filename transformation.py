temp = list(map(int,input().split(" ")))

def rem_one(num):
    res = int(num/10)
    return res
def div_two(num):
    res = int(num/2)
    return res

a = temp[0]
b = temp[1]
l=[]
l.append(b)
r = b
flag = 0
while a<r :
    if r % 10 == 1:
        r = rem_one(r)
        l.append(r)
    elif r % 2 == 0:
        r = div_two(r)
        l.append(r)
    else:
        print('NO')
        flag = 1
        break
if a == r:
    print('YES')
    print(len(l))
    l.reverse()
    for i in l:
        print(i,end=" ")
elif flag == 0:
    print('NO')

