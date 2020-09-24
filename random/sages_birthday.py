num = int(input())
spheres = list(map(int, input().split(" ")))

divider = int((len(spheres)+1)/2)

first = [ spheres[i] for i in range(len(spheres)-divider)]
second = [ spheres[i] for i in range(len(spheres)-divider , len(spheres))]


final = []
count = 0
while count != len(spheres):
    if count < len(second):
        final.append(second[count])
    if count < len(first):
        final.append(first[count])

    count += 1

knt = 0
for i in range(1,len(final)-1):
    if final[i-1] > final[i] and final[i+1] > final[i]:
        knt += 1

print(knt)
for i in final:
    print(i,end=" ")