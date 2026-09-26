n=int(input())
i = 2
prime = True
while i * i <= n:
    if n % i == 0:
        prime = False
        break
    i+=1
if prime and n != 1:
    print('Prime')
else:
    print('Non Prime')