try:
    a=int(input("Enter the age: "))
    if (a<=18):
        raise ValueError
    elif(a<=0):
        raise 
    else:
        print("You are elidgible")
except ValueError:
    print("Not Elidgible")
except :
    print("Invalid Age")


