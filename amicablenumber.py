def add(n):
    sum = 0
    for i in range(1,n//2+1):
        if n % i ==0:
            sum+=i
    return sum


num1, num2 = map(int,input().split())
if num1 == add(num2) and num2 == add(num1):
    print('amicable')
else:
    print("not")
