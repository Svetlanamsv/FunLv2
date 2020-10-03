def myfunction(a,b,i):
    c=[]
    import random
    for x in range(a):
        c.append(random.randint(0, b))
    print(c)
    print(c[i])

myfunction(6,8,3)

