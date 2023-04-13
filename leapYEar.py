year=int(input("enter the year"))
if (year % 400 == 0) and (year % 100 == 0):
    print("Leap")

elif (year % 4 ==0) and (year % 100 != 0):
    print("Leap")
else:
    print(" Not Leap")