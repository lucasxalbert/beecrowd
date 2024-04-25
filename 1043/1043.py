A, B, C= map(float, input().split())
L = [A, B, C]
l = sorted(L)
menor = l[0] + l[1]
if menor > l[2]:
    perimetro =A + B + C
    print("Perimetro = %.1f" %perimetro)
else:
    area =((A + B)*C)/2
    print("Area = %.1f" %area)
