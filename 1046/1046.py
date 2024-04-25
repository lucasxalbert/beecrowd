x, z = map(int, input().split())
if x >= z:
    y = (24 - x)+ z
    print("O JOGO DUROU %d HORA(S)" %y)
else:
    y = z - x
    print("O JOGO DUROU %d HORA(S)" %y) 
