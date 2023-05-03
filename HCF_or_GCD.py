# # Function to find HCF the Using Euclidian algorithm
# def compute_hcf(x, y):
#    while(y):
#        x, y = y, x % y
#    return x

# hcf = compute_hcf(300, 400)
# print("The HCF is", hcf)


# Python program to find H.C.F of two numbers

# define a function
# def compute_hcf(x, y):

# # choose the smaller number
#     if x > y:
#         smaller = y
#     else:
#         smaller = x
#     for i in range(1, smaller+1):
#         if((x % i == 0) and (y % i == 0)):
#             hcf = i 
#     return hcf

# num1 = 600
# num2 = 500

# print("The H.C.F. is", compute_hcf(num1, num2))
x=300
y=400
while(y):
    x,y=y,x%y
print(x)