def swap(arr):
    for i in range(0, n - 1, 2):
        temp = arr[i]
        arr[i] = arr[i + 1]
        arr[i+ 1] = temp
    return arr

n = int(input())
arr =list(map(int,input().split()))

print(swap(arr))