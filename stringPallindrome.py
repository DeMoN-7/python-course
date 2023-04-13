# String Pallindrome
a=input("enter the string: ")
a=a.casefold()
rev=reversed(a)
if(list(a)==list(rev)):
    print("Pallindorme")
else:
    print("Not Pallindrome")