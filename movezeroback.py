n = int(input())
arr = list(map(int,input().split()))

index = 0
for i in range(n):
    if arr[i]!=0:
        arr[i], arr[index] = arr[index], arr[i]
        index += 1

print(*arr)