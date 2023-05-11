# 1.	Write a Python function that accepts a string and counts the number of upper and lower case letters.
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12
def low(s):
    z=0
    for i in s:
        if (i.islower()):
            z+=1
    return z
def up(s):
    z=0
    for i in s:
        if (i.isupper()):
            z+=1
    return z
a=input("Enter the string: ")
print("low: ",low(a))
print("up: ",up(a))   
