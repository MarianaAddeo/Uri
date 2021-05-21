sum=float(0.0)
positivo=int(0)
avg=float(0.0)
for i in range(1,7):
    m=float(input())
    if(m>0):
        positivo=positivo+1
        sum=sum+m
avg=sum/positivo
print(str(positivo)+" valores positivos")
print("%0.1f"%(avg))
