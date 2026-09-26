n = list(map(int,input().split()))
c= len(n)
total = 0
for i in n:
    total += i
result = total/c

print(f"{result:.2f}")