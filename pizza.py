noOffriends = int(input())
if noOffriends == 0:
    print(int(0))

else:
    total = noOffriends + 1

    if total % 2 == 0:
        print(int(total/2))
    else:
        print(total)