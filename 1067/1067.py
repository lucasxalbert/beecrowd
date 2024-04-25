x = int(input())
for i in range(x):
    i = i + 1
    if i % 2 != 0:
        print(i)
        i = i +1
    if i == x:
        break
