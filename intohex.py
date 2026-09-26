n = int(input())
hexa = '0123456789ABCDEF'
result = ''
while n > 0: #decimal to Hexadecimal
    rem = n % 16
    result = hexa [rem] + result
    n//= 16
print(result)