# built in sort() method does this for you
# used list instead of array for simplicity to focus on sorting aspect
intArray = [12, 5767, 1, 9, 45, 34, 786, 123, 68]
temp = 0

for i in range(0, len(intArray)): # iterate over array from beginning
    for j in range(i+1, len(intArray)): # iterate over start 1 index in
        if intArray[i] >= intArray[j]: # check if next element in array is greater then element i
            temp = intArray[i] # set temp value equal to element at index i
            intArray[i] = intArray[j] # set element at index i equal to next element
            intArray[j] = temp # set next element equal to temp value (old element i)

print(intArray)
        
        

