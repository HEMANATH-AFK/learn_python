def greaterPrior(arr):
    print(arr[0], end=' ')
    for i in arr:
        if i > arr[0]:
            arr[0] =i
            print(i, end=' ')
            
n = int(input())
arr = list(map(int, input().split()))
greaterPrior(arr)