A, B, C = map(float , input().split())
delta = ((B**2)-(4*A*C))
if delta < 0:
    print("Impossivel calcular")
elif A == 0:
         print("Impossivel calcular")
elif B == 0:
         print("Impossivel calcular")
elif C == 0:
         print("Impossivel calcular")     
else:
    R1 = ((-B)+delta**(1/2))/(2*A)
    R2 = ((-B)-delta**(1/2))/(2*A)
    print("R1 = %.5f\nR2 = %.5f" %(R1,R2))
