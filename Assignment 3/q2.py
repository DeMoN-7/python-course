# 2.	Write a Python function that takes a list and returns a new list with distinct elements from the first list.
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]
def ok(o):
    return list(set(o))
l=int(input("Enter the limit: "))
a=[]
for i in range(l):
    x=int(input("Enter the element: "))
    a.append(x)
k=ok(a)
print(k)