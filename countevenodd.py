def average(arr):
    counteven=0
    evensum=0
    countodd=0
    oddsum=0
    for i in arr:
        if i%2==0:
            evensum+=i
            counteven+=1
        else:
            oddsum+=i
            countodd+=1
    print("odd: ",oddsum/countodd)
    print("even: ",evensum/counteven)

arr = list(map(int,input().split()))
average(arr)
