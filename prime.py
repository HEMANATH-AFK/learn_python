n = int(input())
count = 0

for i in range(2, n//2+1):
    if n % i == 0:
        count+=1
if count == 0:
    print("prime number")
else:
    print("not prime number")
