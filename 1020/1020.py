dias = int(input())
ano = dias//365
restodias = dias%365
meses = restodias// 30
diass = restodias%30
print("%.0f ano(s)\n%.0f mes(es)\n%.0f dia(s)"%(ano,meses,diass))
