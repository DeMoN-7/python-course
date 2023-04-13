# wap to find the sum of all element in a list and a tuple 

a=[1,2,3,4,5]  #list
temp=0
x=len(a)
z=0
while(z<x):
    temp=temp+a[z]
    z+=1
print(temp)



a=(1,2,3,4,5)  #tuple
temp=0
x=len(a)
z=0
while(z<x):
    temp=temp+a[z]
    z+=1
print(temp)