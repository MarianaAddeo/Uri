Line1=input().split()
A=int(Line1[0])
B=int(Line1[1])
C=float(Line1[2])
Line2=input().split()
A2=int(Line2[0])
B2=int(Line2[1])
C2=float(Line2[2])
TOTAL=B*C+B2*C2
print("VALOR A PAGAR: R$",'{:.2f}'.format(TOTAL))
