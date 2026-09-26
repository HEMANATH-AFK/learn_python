n = int(input())
initial = n
rev = 0
while(n>0):
    rev = rev*10+(n%10)
    n //=10

if initial == rev:
    print("palindrome")
else:
    print("not palindrome")