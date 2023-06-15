# Fact...................................
# def fact(n):
#     return 1 if n==0 else n*fact(n-1)

# # def fact(n):
# #     if n==0 or n==1:return 1 
# #     return n*fact(n-1)


# print(fact(3))
# print(fact(4))
# print(fact(5))
# print(fact(6))

# fibbonacci series...........................................

def fibo(n):
    if n==1:
        return 1
    elif n==0:
        return 0
    else:
        return (fibo(n-1)+fibo(n-2))

for i in range(4):
    print(fibo(i),end=" ")
