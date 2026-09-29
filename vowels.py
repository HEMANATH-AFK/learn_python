n=input()
vowels="aeiouAEIOU"
c=0
for i in n:
    if i in vowels:
        c+=1
print(c)