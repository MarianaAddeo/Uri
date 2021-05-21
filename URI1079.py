m=int(input())
for i in range(0,m):
    k,j,c=input().split()
    k=float(k)
    j=float(j)
    c=float(c)
    total=(k*2 + j*3 + c*5)/10
    print("{0:.1f}".format(total))
