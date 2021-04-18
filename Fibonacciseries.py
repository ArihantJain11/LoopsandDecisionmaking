a = -1
b = 0
c = 0
print(c)
print(c+1)
while c<=1000:
    if c==0:
        a=a+1
        b=b+1
    c = a + b
    a = b
    b = c
    print(c)
