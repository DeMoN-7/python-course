# 3.	Write a Python function to check whether a number is "Perfect" or not.
# Example : The first perfect number is 6, because 1, 2,and 3 are its proper positive divisors,
#  and 1 + 2 + 3 = 6.
# Equivalently, the number 6 is equal to half the sum of all 
# its positive divisors: ( 1 + 2 + 3 + 6 ) / 2 = 6. 
# The next perfect number is 28 = 1 + 2 + 4 + 7 + 14.
#  This is followed by the perfect numbers 496 and 8128. 


def perfect(a):
    x=0
    for i in range(1,a+1):
        if(a%i==0):
            x+=i
    if (x/2==a):
        return True
    else:
        return False
a=int(input("Enter the number: "))
if(perfect(a)):
    print("Perfect")
else:
    print("Not Perfect")