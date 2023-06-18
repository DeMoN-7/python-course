# ..........basic syntax of lambda function

# ser=lambda x:x**x
# print(ser(5))




# ..............program to filter list to even and odd...............



lis=[1,2,3,4,5,6,7,8,9,0]
even=list(filter(lambda x:x%2==0,lis))
odd=list(filter(lambda x:x%2!=0,lis))

print(even)
print(odd)