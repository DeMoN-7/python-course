#   wap to create list with different type of string generate
#  another list such that it will have count of all
#  the alphabet in it

a=[]
di={}
n=int(input("Enter the limit "))

for i in range(0,n):
    x=input("Enter String ")
    a.append(x)

for i in range(0,n):
    for x in a[i]:
        if x in di:
            di[x]+=1
        else:
            di[x] = 1

print(sorted(di.items()))
