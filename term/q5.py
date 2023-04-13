list1=[]
positive=[]
negative=[]
limit=int(input("Enter the amount of numbers:- "))
i=0
while(i<limit):
    list1.append(int(input("Enter number:- ")))
    if(list1[i]>0):
        positive.append(list1[i])
    else:
        negative.append(list1[i])
    i+=1
print("Original list:- ",list1)
print("Positive list:- ",positive)
print("Negative list:- ",negative)