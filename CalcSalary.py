#wap to cal salary of employee given his basic pay (to be taken as input)
#HRA =10% of basic 
#TA =5% of basic 

basic=int(input("Enter the basic salary: "))
hra=0.1*basic
ta=0.05 * basic
print("Salary is: ",hra+ta+basic)