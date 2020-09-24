noOfNumbers = int(input())

numbers = list(map(int,input().split(" ")))

def hasfalse(l):
    for i in range(len(l)):
        if l[i] == False:
            return i
        else:
            return 0



numbers.sort()
boo = []
for i in range(len(numbers)):
    boo[i] = False

while hasfalse(boo) != 0:
    falsy = hasfalse(boo)
    
