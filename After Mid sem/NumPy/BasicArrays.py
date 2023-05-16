import numpy as nu
# ar= nu.array([[1,2,3,4,5],[5,6,4,1,7]])
# print("Array",ar)
# print("Type: ",type(ar))
# print("Shape:",ar.shape)
# print("Dimension: ",ar.ndim)
# print("Length",ar.size)
# print("Type of element",ar.dtype)



# arr1=nu.array([[1,2,3],[1,2,3]],dtype='float')
# print("List: \n",arr1)
# arr2=nu.array(((1,2,3),(6,7,8)))
# print("Tuple:\n",arr2)
# arr3=nu.zeros((3,6))
# print(arr3)
# # ,,,,,,,,,,,,,,,,,,,,,,,,operator...................
# print("Sum:\n",arr1+arr2)
# print("Multiplication:\n",arr1*arr2)

# arr3=nu.random.random((3,3))
# print(arr3)

# arr4=nu.array([[1,2,3,4,5,6],[5,6,4,1,7,8]])
# print(arr4.reshape(2,3,2))

# Create a sequence of 3 value with random values starting from 0 ends to 5
# arr5=nu.linspace(0, 5,3)
# print(arr5)


arr6=nu.array([[1,2,3,4,5,6],[5,6,4,1,7,8]])
print(arr6.flatten())