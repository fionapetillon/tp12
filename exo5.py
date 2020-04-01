def product(a,b):

    if ((a == 0)or (b==0)):
        return 0
    elif a==1:
        return b
    elif b==1:
        return a

    else:
        return a+product(a,b-1)


print(product(5,2)) # 10
print(product(9,3)) # 27
