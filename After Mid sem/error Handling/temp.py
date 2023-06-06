a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
try:
    print(a/b)

except ZeroDivisionError:
    print("Zero error")