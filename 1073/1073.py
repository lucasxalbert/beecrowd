N = int(input())
for x in range(N+2):
    if x % 2 == 0 and x >= 1:
        i = x + 2
        print("%d^2 = %d" % (x,x**2))
        if x == N:
            break
