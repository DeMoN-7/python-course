# 2.	Write a Python function that takes a list and returns a new list with distinct elements from the first list.
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]

l=int(input("Enter the limit: "))
a=[]
c=[]
for i in range(l):
    x=int(input("Enter the element: "))
    a.append(x)
b=set(a)
c=list(b)
print(a)
print(b)