n = int(input())
temp=n

sum = 0
while(n > 0):
    sum += ( n %10)
    n //=10

if temp%sum == 0:
    print("harshad number")
else:
    print("Not harshad number")
