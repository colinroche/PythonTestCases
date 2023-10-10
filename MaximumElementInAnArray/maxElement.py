import numpy as np

IntegerArray = np.array([0, 65, 987, 12, 54, 7, 23, 123])
arrayLength = len(IntegerArray)
max = ""

IntegerArray.sort()
max = IntegerArray[arrayLength-1]

print(IntegerArray)
print(max)