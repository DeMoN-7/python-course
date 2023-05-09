def su(*y):
    s=0
    for i in y:
        s=sum(i)
    return s


i=int(input("Enter the limit: "))
a=[]
for x in range(0,i):
    z=int(input("enter the number: "))
    a.append(z)
# aa=tuple(a)
# print(type(aa))
main=su(a)
print(main)