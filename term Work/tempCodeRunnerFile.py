
# * * * * 
# * * * 
# * * 
# *

a=1
x=1
z=10
while(a<=11):
    
    if (a<6):
        while(x<a):
            print("*",end=" ")
            x+=1
    else:
        while (z>a-1):
            print("*",end=" ")
            z-=1
    print()
    a+=1
    x=1
    z=10