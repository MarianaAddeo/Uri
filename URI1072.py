m=0
d=0
a=int(input())
if a<10000:
    for i in range(0,a):
        b=int(input())
        if b>=10 and b<=20:
            m=m+1
        else:
            d=d+1
print("{} in".format(m))
print("{} out".format(d))
