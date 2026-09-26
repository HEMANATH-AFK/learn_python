n = int(input())
result , product = 0, 1
while n > 0:
    rem = n % 10
    result = result + (rem * product)
product *= 8
n //= 10
print(result)
# decimal to binary
# 10      2

