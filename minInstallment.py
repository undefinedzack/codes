NM = list(map(int,input().split(" ")))
totalFriends = NM[0]
totalTransactions = NM[1]

arr = [0 for i in range(totalFriends)]

for i in range(totalTransactions):
    hmmm = list(map(int,input().split(" ")))
    frommm = hmmm[0]
    tooo = hmmm[1]
    howmuch = hmmm[2]

    arr[frommm-1] += howmuch
    arr[tooo-1] -= howmuch
install = 0
for item in arr:
    if item > 0:
        install += item
print(install)

