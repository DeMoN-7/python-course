# try:
#     a=int(input("Enter the number:"))
#     b=a/44
# except Exception as e:
#     print("Error; ",e)
# # except ZeroDivisionError:
# #     print("Error")
# print("ifgj")


# ..............Rasing multiple error..........

try:
    n=int(input("Enter the index: "))
    a=[7,6,8,2]
    print(a[n])
except IndexError:
    print("Index Error")
except ValueError:
    print("Value error")
