arr = list(map(int,input().split()))
min = arr[0]
min2 = arr[1]

for i in arr:
    if i < min:
        min2 = min
        min = i
    elif i < min2 and i !=min:
        min2 = i

print(min2)
