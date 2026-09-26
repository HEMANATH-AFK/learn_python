# Armstrong number: 153
# 1. Find digit count
# 2. Raise each digit to the power of the digit count
# 3. If the sum equals the original number, it is an Armstrong number

def countNumber(n):
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count


def sumNumber(n, c):
    total = 0
    while n > 0:
        total += ((n % 10) ** c)
        n //= 10
    return total


n = int(input())
c = countNumber(n)
total = sumNumber(n, c)

if n == total:
    print(" Armstrong number")
else:
    print(" not Armstrong number")