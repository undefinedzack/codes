def gcd(a,b):
    if a > b:
        if b == 0:
            return a
        else:
            d = a % b
            return(gcd(b,d))
    else:
        t = a
        a = b
        b = t
        if b == 0:
            return a
        else:
            d = a % b
            return(gcd(b,d))

a,b = map(int,input().split(" "))
print(gcd(a,b))
