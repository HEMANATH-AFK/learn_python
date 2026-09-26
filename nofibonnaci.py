def fibonacci(n):
    first, second, third = 0, 1, 0
    for i in range(n-1):
        third= first + second
        first = second
        second = third
    print(first, end=" ")


n = int(input())
fibonacci(n)