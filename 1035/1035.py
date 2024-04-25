A, B, C, D = map(int, input().split())
CD = C+D
AB = A+B
if B > C and D > A and CD > AB and CD > 0 and A%2 == 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
