def check(num):
    if num > 0:
        print('Greater than Zero')
    elif num < 0:
        print('Less than Zero')
    else:
        print("It's a Zero")

#USER INPUT

while(1):
    innn = int(input("1.Enter Number\n2.Quit\n"))
    if innn == 1:
        num = int(input())
        check(num)
    else:
        break