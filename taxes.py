n1 = int(input(""))
n = n1
op = 0


def my_function(n, op):
    if (n <= 3):
        op = op + 1
        n = 1
        return [n, op]
    else:
        for num in range(n, 1, -1):

            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:

                    high = num
                    if (high > 3):
                        n = n - high
                        op += 1
                    else:

                        op += 2
                        n = 1

                    return [n, op]

                    break


while (1):

    if (n > 1):
        n, op = my_function(n, op)
    else:
        break

print(op)