cp1, nmrp1, vlru1 = map(float, input().split())
cp2, nmrp2, vlru2 = map(float, input().split())
valortotal = (vlru1*nmrp1) + (vlru2*nmrp2)
print("VALOR A PAGAR: R$ %.2f" %valortotal)
