a={}
L=int(input("Enter the length "))
for i in range(0,L):
    z=input("Key: ")
    y=input("Value: ")
    a[z]=y
print(sorted(a.items()))