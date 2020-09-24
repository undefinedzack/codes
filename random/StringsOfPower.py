s = str(input())

def findIndexs(s,word,start):
    l = []
    # i = s.find(word)
    # l.append(i)
    i = start
    while i < len(s):
        i = s.find(word,i,len(s))
        if i != -1:
            l.append(i)
        if i == -1:
            break
        i += 5
        
    return l


h = findIndexs(s,'heavy')

m = findIndexs(s,'metal')
print(h)
print(m)
# rMod = list(h.remove(-1))
# mMod = list(m.remove(-1))


h.sort()
m.sort()
# print(h)
# print(m)
#print(rMod,mMod)
knt = 0
for i in range(len(h)):
    for j in range(len(m)):
        if h[i] < m[j]:
            knt += 1
print(knt)
