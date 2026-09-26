num = int(input())

temp = num
length = 0
while temp > 0:
    length += 1
    temp //= 10

temp = num
total = 0
index = length

while temp > 0:
    digit = temp % 10 
    total += digit ** index 
    index -= 1  
    temp //= 10           

if total == num:
    print("Disarium number")
else:
    print(" Disarium number")
