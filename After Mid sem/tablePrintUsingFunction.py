# print table using fuction

def table(a):
    for i in range(1,11):
        print(a,"X",i,"=",i*a)

x=int(input("Enter number: "))
table(x)