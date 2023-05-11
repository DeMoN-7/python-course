# 5.	Write a Python program to detect the number of local variables declared in a function
def temp():
    x=0
    x1=20
    x3=330
local=0
print(temp.__code__.co_nlocals)