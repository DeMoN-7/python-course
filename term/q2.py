char=input("Enter a character: ")[0]
if(char.islower()):
    print(char+" is lower case")
elif(char.isupper()):
    print(char+" is upper case")
elif(char.isdigit()):
    print(char+" is a digit")
else:
    print(char+" is a special")