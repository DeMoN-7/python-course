import numpy as np

url="D:/Github/Python/After Mid sem/NumPy/iris.data"

sepalLength=np.genfromtxt(url,delimiter=',',dtype='float',usecols=[0])

Mean=np.mean(sepalLength)
Median=np.median(sepalLength)
sd=np.std(sepalLength)
print("MEAN: ",Mean)
print("Median: ",Median)
print("Standard Deviation: ",sd)