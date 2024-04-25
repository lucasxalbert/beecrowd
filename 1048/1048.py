A = float(input())
if 0 < A <=400.00:
    sl = A *0.15
    sl_A = sl + A
    print("Novo salario: %.2f\nReajuste ganho: %.2f\nEm percentual: 15 %%" %(sl_A,sl,))
elif 400.01 <= A <= 800.00:
     sl = A *0.12
     sl_A = sl + A
     print("Novo salario: %.2f\nReajuste ganho: %.2f\nEm percentual: 12 %%" %(sl_A,sl))
elif 800.01 <= A <= 1200.00:
     sl = A *0.10
     sl_A = sl + A
     print("Novo salario: %.2f\nReajuste ganho: %.2f\nEm percentual: 10 %%" %(sl_A,sl))
elif 1200.01 <= A <= 2000.00:
     sl = A *0.07
     sl_A = sl + A
     print("Novo salario: %.2f\nReajuste ganho: %.2f\nEm percentual: 7 %%" %(sl_A,sl))
elif 2000.01<=A:
     sl = A *0.04
     sl_A = sl + A
     print("Novo salario: %.2f\nReajuste ganho: %.2f\nEm percentual: 4 %%" %(sl_A,sl))
