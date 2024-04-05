nome = input()
salariofixo= float(input())
produtosvendidos = float(input())
bonus = produtosvendidos * 0.15
TOTAL = salariofixo + bonus
print("TOTAL = R$ %.2f" %TOTAL)
