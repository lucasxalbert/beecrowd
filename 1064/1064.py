L=[]
for i in range(6):
    i = float(input())
    if i>0:
        L.append(i)
media = sum(L) / len(L)
print( "%d valores positivos\n%.1f"%(len(L),media))
