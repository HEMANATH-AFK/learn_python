n = int(input())
arr = list(map(int,input().split()))

index = n-1
for i in range(n-1, -1, -1):
    if arr[i]!=0:
        arr[i], arr[index] = arr[index], arr[i]
        index -= 1

print(*arr)