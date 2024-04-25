N = 5
l=[]
for x in range(N):
    x= int(input())
    if x % 2 == 0:
        l.append(x)
print("%d valores pares" %len(l))
