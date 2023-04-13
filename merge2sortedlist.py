# wap to merge two sorted list in ascending order
a=[]
b=[]
n1=int(input("enter the First limit "))
n2=int(input("enter the Second limit "))
for i in range(0,n1):
    x=int(input("enter elements: "))
    a.append(x)
for i in range(0,n2):
    x=int(input("enter elements: "))
    b.append(x)

for i in range(0,n1):
    for x in range(0,n1-1-i):
        if(a[x]>a[x+1]):
            temp=a[x]
            a[x]=a[x+1]
            a[x+1]=temp


for i in range(0,n2):
    for x in range(0,n2-1-i):
        if(b[x]>b[x+1]):
            temp=b[x]
            b[x]=b[x+1]
            b[x+1]=temp

list3 =a+b
n2=len(list3)

for i in range(0,n2):
    for x in range(0,n2-1-i):
        if(list3[x]>list3[x+1]):
            temp=list3[x]
            list3[x]=list3[x+1]
            list3[x+1]=temp

print(list3)