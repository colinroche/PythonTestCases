import numpy as np

integerArray = np.array([0, 1, 2, 3, 3, 3, 3, 3, 4, 5, 3, 3, 7, 9, 3])
matches = 0
sum = 0

for i in range(len(integerArray)): # iterate over the elements in the array
    for j in range(len(integerArray)):
        if i != j and integerArray[i] == integerArray[j]: # check they are not the same element in the array and that they are the same number
            matches += 1
            sum += integerArray[i]
            break

print(matches)
print(sum)