N = int(input())
L=[]
for X in range(N):
    X = int(input())
    if 10<= X <=20:
        L.append(X)

print("%d in\n%d out" %(len(L),N-len(L)))
