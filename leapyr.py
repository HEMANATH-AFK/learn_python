#year should divisible by 400
#if it divisible by 4 and it should not divisible by 100

yr = int(input())
if yr % 400 == 0 or (yr % 4 == 0 and yr % 100 != 0):
    print("leap year")
else:
    print("not leap year")
