list1=[]
square=[]
limit=int(input("Enter the amount of numbers:- "))
i=0
while(i<limit):
    list1.append(int(input("Enter number :- ")))
    square.append(list1[i]**2)
    i+=1
print("Entered list:- ",list1)
print("Squared list:- ",square)
