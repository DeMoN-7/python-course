a=int(input("Enter the number"))
even=0
odd=0
while(a):
    temp=a%10
    if(temp%2==0):
        even+=1
    else:
        odd+=1
    a=a//10
print("number of odd digit is: ",odd)
print("number of even digit is: ",even)
