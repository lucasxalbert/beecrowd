x = 5
par = []
impar=[]
positivo = []
negativo = []
for i in range(x):
    i = int(input())
    if i % 2 == 0:
        par.append(i)
    if i % 2 != 0:
        impar.append(i)
    if i > 0:
        positivo.append(i)
    if i <0:
        negativo.append(i)
print("%d valor(es) par(es)\n%d valor(es) impar(es)\n%d valor(es) positivo(s)\n%d valor(es) negativo(s)" %(len(par),len(impar),len(positivo),len(negativo)))
