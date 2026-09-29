n = input().split()
long = n[0]
for i in range(1, len(n)):
    if len(n[i]) > len(long):
        long = n[i]
print(long)