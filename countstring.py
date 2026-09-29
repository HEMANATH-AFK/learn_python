n = input()
alphabet, number, spl = 0,0,0
for i in n:
    if i.isdigit():
        alphabet+=1
    if i.isalpha():
        number+=1
    else:
        spl+=1
print(alphabet, number, spl)