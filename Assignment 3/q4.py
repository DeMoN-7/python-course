# 4.	Write a Python Program to Display Fibonacci Sequence Using Recursion

def Fibonacci(nu):
    if (nu<=1):
        return nu
    else:
        return (Fibonacci(nu-2)+Fibonacci(nu-1))
i=int(input("Enter the limit: "))
for z in range(i):
    print(Fibonacci(z),end=" ")