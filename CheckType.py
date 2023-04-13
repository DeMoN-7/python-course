# write a py script to check the type of input enter

a=input("enter ")
if(a>='0' and a<='9'):
    print("Number")
elif(a>='a' and a<='z'):
    print("small alphabet")
elif(a>='A' and a<='Z'):
    print("Cap Alphabet")
elif(a==' '):
    print("White Space")
else:
    print("Special Char")

a=input("enter anything")
if(a.isalpha()):
    if(a.isupper()):
        print("Capital Alphabet")
    if(a.islower()):
        print("Lower Alphabet")
elif(a.isnumeric()):
     print("Number")
elif(a==" "):
    print("Whitespace")
else:
    print("Special Character")