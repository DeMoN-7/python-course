try:
    a=int(input("Enter the age: "))
    if (a<=18):
        raise ValueError 
    else:
        print("You are elidgible")
except ValueError:
    print("Not Elidgible")


