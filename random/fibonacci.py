n = int(input())

l = [0 for i in range(n)]
if n > 0:
    l[1] = 1

for i in range(2,n):
    l[i] = l[i-1] + l[i-2]

print(l[n-1])