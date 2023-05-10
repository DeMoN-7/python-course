# 1.	Write a Python function that accepts a string and counts the number of upper and lower case letters.
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12

a=input("Enter the string: ")
low=0
up=0
for i in a:
    
    if (i.isupper()):
        up+=1
    elif (i.islower()):
        low+=1
print("low: ",low)
print("up: ",up)   
