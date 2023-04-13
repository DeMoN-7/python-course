# wap to add elements dynamically ask user how many number want to input

a=[]
n=int(input("enter the limit: "))
x=0
while(x<n):
    temp=int(input("enter elements: "))
    x+=1
    a.append(temp)
print(a)
