test_cases = int(input())

for i in range(test_cases):
    size = int(input())
    ones_and_zeros = list(map(int, input().split(" ")))
    ones_and_zeros.reverse()
    knt = 0
    for j in range(len(ones_and_zeros)):
        if ones_and_zeros[j] == 0:
            knt += 1
        else:
            break
    print(knt)
