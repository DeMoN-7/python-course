print("Enter three sides: ")
a=int(input())
b=int(input())
c=int(input())
if(a+b<=c) or (a+c<=b) or (c+b<=a):
    print("Triangle can be formed ")
else:
    print("Triangle cannot be formed ")