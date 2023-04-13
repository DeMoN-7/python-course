start=int(input("Enter starting range:- "))+1
end=int(input("Enter ending range:- "))
while(start<end):
    i=2
    count=0
    while(i<start):
        if(start%i==0):
            count+=1
        i+=1
    if(count==0):print(start)
    start+=1