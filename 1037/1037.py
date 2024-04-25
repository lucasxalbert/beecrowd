A = float(input())
if 0 <=A <=25.0000:
    print("Intervalo [0,25]")
elif 25.00001 <= A <= 50.0000:
    print("Intervalo (25,50]")
elif 50.00001 <= A <= 75.0000:
    print("Intervalo [50,75]")
elif 75.00001 <= A <= 100.00:
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")
