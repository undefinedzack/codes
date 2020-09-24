testCases = int(input())

for i in range(testCases):
    n = int(input())
    binary_string = str(input())

    substrings= []
    for knt in range(len(binary_string)-n+1):
        substrings.append(binary_string[knt:knt+n])

    flag = False
    for h in range(n):
        temp = []
        for k in range(len(substrings)):
            temp.append(substrings[k][h])
        if len(set(temp)) == 1:
            index = h
            flag = True
            break

    the_string = ""
    for z in range(n):
        if z == index and flag == True:
            the_string += substrings[0][index]
        else:
            the_string += '0'

    print(the_string)