def pow(x,n):
    result=0
    if (n == 0):
        result = 1
    else:
        result = x * pow(x,n-1);
    return result

print(pow(42, 0)) # 1
print(pow(1, 10)) # 1
print(pow(2, 5)) # 32
print(pow(7, 2)) # 49
