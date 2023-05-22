def ok(o):
    return list(set(o))
l=int(input("Enter the limit: "))
a=[]
for i in range(l):
    x=int(input("Enter the element: "))
    a.append(x)
k=ok(a)
print(k)