arr = list(map(int,input().split()))
max = arr[0]
max2 = arr[1]

for i in arr:
    if i > max:
        max2 = max
        max = i
    elif i > max2 and i !=max:
        max2 = i

print(max2)
