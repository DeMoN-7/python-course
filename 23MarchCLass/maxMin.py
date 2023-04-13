a=[]
n1=int(input("enter the First limit "))

for i in range(0,n1):
    x=int(input("enter elements: "))
    a.append(x)

min=max=a[0]

for i in range(0,n1):
        if(max<a[i]):
            max=a[i]
        if(min>a[i]):
            min=a[i]
print("min: ",min,"max: ",max)