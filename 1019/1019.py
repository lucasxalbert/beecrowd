N = int(input())
horas = N // 3600.
resto_segundos = N %3600
minutos = resto_segundos // 60
segundos = resto_segundos %60
print("%.0f:%.0f:%.0f"%(horas,minutos,segundos))
