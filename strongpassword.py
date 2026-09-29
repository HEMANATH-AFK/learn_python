n = input()

if len(n) > 8:
    upper = False
    for i in n:
        if 'A' <= i <= 'Z':
            upper = True
            
    if upper and not n.isalpha() and not n.isdigit():
        print("strong password")
    else:
        print("weak password")
else:
    print("weak password")