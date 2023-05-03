# WAP TO GENERATE A LIST DYNAMICALLY LIST 
# AND THAN  FIND THE MEAN OF ODD TERM 
# AND MEDIAN OF EVEN TERM 

limit=int(input("Enter the limit of list: "))
a=[]
mean,median=[],[]
total=0
for i in range(0,limit):
    x=float(input("Enter the element: "))
    if(i%2!=0):
        total+=x
        mean.append(x)
    else:
        median.append(x)

median.sort()
c=len(mean)
c1=len(median)
TempMean=total//c

if c1%2==0:
    temMed=median[c1//2]
    temMed1=median[c1//2-1]
    med=(temMed+temMed1)/2

else:
    med=median[c1//2]

print("Median list: ",median)
print("Mean list: ",mean)
print("Mean:",TempMean)
print("Median:",str(med))
