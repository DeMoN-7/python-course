def rec(x):
    return 1 if (x==0 or x==1) else x*rec(x-1)

x=int(input("Enter the number"))
x=rec(5)
print("Factorial of number is: ",x)