def bigg(a,b):
    if (a>b):
        return a
    elif (a==b):
        return 'equal'
    else:
        return b
a=int(input("enter the first number: "))
b=int(input("Enter the second number: "))
c=bigg(a,b)
print(c)