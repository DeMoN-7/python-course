import numpy as np
a=[10,20,5,10,8,20,8,9]
arr=np.array(a)
print(type(arr))
print(arr)
uniq,count=np.unique(arr,return_counts=True)
print(uniq)
print(count)