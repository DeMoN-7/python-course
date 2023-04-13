a=int(input("enter limit"))
n=1

while(n<=a):
    flag=0
    x=1
    while(x<n):
        if((n)%x==0):
            flag=1
        x+=1
    n+=1
    if (flag==0):
        print(n)