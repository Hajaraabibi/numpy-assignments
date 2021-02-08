import numpy as np
oned_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(oned_array)
twod_array = np.reshape(oned_array, (-1,5))
print(twod_array)