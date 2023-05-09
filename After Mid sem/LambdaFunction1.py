# lamda function are anonymus function that is fuction without name
# these function have only single line
# they can have any number of argument
# they can't access global variable
# and do not have explict return statement 
# 
# lambda argument:exp
# example sum=lambda x,y:x+y
# print(sum(10,20))

demon =lambda x:print("Hello",x)
demon("ayush")

z=lambda *y:sum(y)
print(z(2,3,4,5))

