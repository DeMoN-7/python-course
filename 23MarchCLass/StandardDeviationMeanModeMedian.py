a=[]
l=int(input("Enter the limit of list: "))
total=avg=0
frequency=[]
for i in range(0,l):
    x=int(input("Enter element: "))
    a.append(x)
    total+=x
mean=total/l
for i in a:
   if i in frequency:
      frequency[i] += 1
   else:
      frequency[i] = 1

print(frequency)