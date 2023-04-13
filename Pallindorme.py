# wap to take number as input from user and print all the pallindrome number 

a=int(input("enter the limit"))
rev=0
temp=0
z=1
n=1
while(z<=a):
    n=z
    rev=0
    temp=0
    while(n):
        temp=n%10
        rev=rev*10+temp
        n=n//10
    if(rev==z):
        print(rev)
    z+=1