import numpy as np
def get_1st_largest(array):
    sorted_array = np.sort(array)
    largest_value = sorted_array[-1]
    return largest_value

given_array = np.array([2, 0, 1, 5, 4, 1, 9])
largest_value = get_1st_largest(given_array)

print("Given array:", given_array)
print("Sorted array:", np.sort(given_array))
print("1st largest value:", largest_value)

