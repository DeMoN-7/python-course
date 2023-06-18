def pallindrome(a):
    a=a.replace(" ","").lower()
    return a==a[::-1]

a=input("Enter the string;")
if pallindrome(a):
    print("palindrome")
else:
    print("Not pallindrome")