N1, N2, N3, N4 = map(float, input().split())
n1 = N1 * 2 
n2 = N2 * 3 
n3 = N3 * 4 
n4 = N4 * 1 
Media = (n1 + n2 + n3 + n4) /10
if Media >= 7.0:
    print("Media: %.1f\nAluno aprovado." %Media)
elif Media < 5.0:
    print("Media: %.1f\nAluno reprovado." %Media)
elif 5.0 <= Media <= 6.9:
    print("Media: %.1f" %Media)
    print("Aluno em exame.")
    notaexame = float(input())
    media = (notaexame + Media) /2
    if media <= 5.0:
        print("Nota do exame: %.1f\nAluno reprovado.\nMedia final: %.1f" %(notaexame,media))
    else:
        print("Nota do exame: %.1f\nAluno aprovado.\nMedia final: %.1f" %(notaexame,media))
