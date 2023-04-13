#wap for the following case study
# a company decides to give bonus to all the employee,5% bonus to maleand 10% to female
# wap to enter salary take salary and gender as input 
# if sal <10000 than employee get extra 2% bonus

sal=int(input("enter the salary: "))
gender=input("enter gender in M or F")
if (gender=='M' or gender=='m'):
    M_bonus=(0.05*sal)
    if(sal<10000):
        M_bonus=M_bonus+(0.02*sal)
    print("Bonus: ",M_bonus,"Salary: ",sal+M_bonus)
if (gender=='F' or gender=='f'):
    F_bonus=(0.1*sal)
    if(sal<10000):
        F_bonus=F_bonus+(0.02*sal)
    print("Bonus: ",F_bonus,"Salary: ",sal+F_bonus)


