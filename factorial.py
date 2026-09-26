def factorial(n):
    initial = 1
    for i in range(n, 1, -1):
        initial*=i
    return initial

n = int(input())
print(factorial(n))