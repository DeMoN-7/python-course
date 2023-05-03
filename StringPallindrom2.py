a=input("Enter String: ")
le=len(a)-1
i1=0

for i in a:
    if (a[i1]==a[le]):
        i1+=1
        le-=1
        z=0
        continue
    else:
        z=1
        break
if(z==0):
    print("Pallindrome")
else:
    print("Not Pallindrome")