def rec(x):
    return 1 if (x==0 or x==1) else x*rec(x-1)

a=int(input("Enter the number"))
x=rec(a)
print("Factorial of number is: ",x)