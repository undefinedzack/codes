print('Enter List')
list = list(map(int,input().split(" ")))
max_index=len(list) - 1
index=0
product=1
while index<=max_index:
    product=product*list [index]
    index=index+1
print (product)