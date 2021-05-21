m = float(input())
if m >= 0.00 and m <= 2000.00 :
    print("Isento")
elif  m >= 2000.01 and m <= 3000.00 :
    b = m - 2000
    c = b * 0.08
    print("R$ {0:.2f}".format(c))
elif m >= 3000.01 and m <= 4500.00 :
    b = m - 3000
    c = b * 0.18 + 1000 * 0.08
    print("R$ {0:.2f}".format(c))
if m > 4500.00 :
    b = m - 4500
    c = b * 0.28 + 1500 * 0.18 + 1000 * 0.08
    print("R$ {0:.2f}".format(c))
