a, b = map(int, input().split())

for i in range(a, b + 1):
    if i < 2:
        print(i, end=" ")
        continue

    prime = True
    j = 2
    while j * j <= i:
        if i % j == 0:
            prime = False
            break
        j += 1

    if not prime:
        print(i, end=" ")