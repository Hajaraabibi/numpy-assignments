import numpy as np

numberarr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

odd = np.where(numberarr %2 == 0)

print(odd)
