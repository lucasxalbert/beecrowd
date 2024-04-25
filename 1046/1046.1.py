A, B= map(int, input().split())
x =abs(A - 24)
i = x + B
if i > 24 :
    i = i - 24
print("O JOGO DUROU %d HORA(S)"%i)
