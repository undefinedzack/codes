NLK = list(map(int,input().split(" ")))

n = NLK[0]
l = NLK[1]
k = NLK[2]


b = [];
a = list(map(int,input().split(" ")))
import itertools

b = list(itertools.combinations(a, l))
#print(b)
for item in b:
    if ((max(item) - min(item)) > k):
        b.pop(item)

print(len(b))

