def fun1(i):
    try:
        a=[1,2,34,5]
        print(a[i])
        return "No error"
    except:
        return "Error"
    finally:
        print("Always")
    print("hfhdfd")
i=int(input("Enter the number: "))
x=fun1(i)
print(x)