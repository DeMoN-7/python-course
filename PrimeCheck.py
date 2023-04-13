#wap to check whether the entered nymber is prime or not

a=int(input("ENter :"))
flag=0
n=1
while(n<a):
    if((a/2)%n==0):
        flag=1
        print("not prime")
        break
    n+=1
if (flag==0):
    print("prime")