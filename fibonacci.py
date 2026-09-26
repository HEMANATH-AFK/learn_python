def fibonacci(n):
    first, second, third = 0, 1, 0
    for i in range(n):
        print(first, end=" ")
        third= first + second
        first = second
        second = third

n = int(input())
fibonacci(n)