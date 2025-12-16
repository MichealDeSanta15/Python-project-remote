a = 1
b = 1
for i in range(2,10):
    c=a+b
    a = b
    b = c
    print(c)