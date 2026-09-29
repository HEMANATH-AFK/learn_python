def neonnumber(n):
    neon=n**2
    sum = 0
    while(neon > 0):
        sum += ( neon %10)
        neon //=10
    return sum
n = int(input())
if neonnumber(n) == n:
    print("yes")
else:
    print("no")    