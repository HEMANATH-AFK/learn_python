def automorphic(n):
    sq = n**2
    temp=n
    while n>0:
        l_n = n%10
        l_sq=sq%10

        if l_n != l_sq:
            return False

        n = n//10
        sq = sq//10

    return True

n = int(input())
if automorphic(n):
    print("yes")
else:
    print("no")