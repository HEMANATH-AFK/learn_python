def leader(arr):
    print(arr[0], end=' ')
    for i in range(len(arr)-2,n):
        if i > arr[-1]:
            arr[-1] =i
            print(i, end=' ')
            
n = int(input())
arr = list(map(int, input().split()))
leader(arr)