def prime(n):
    for i in range(2, n):
        if n%i==0:
            return False
    return True

n=list(map(int,input().split()))

for i in n:
    if prime(i):
        print(i)