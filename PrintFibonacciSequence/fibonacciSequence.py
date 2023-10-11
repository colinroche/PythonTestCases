intList = [0, 1]

n = 0
sequenceLength = 15
temp = 0

while n < sequenceLength: # setting the amount of terms
    for i in range(len(intList)):
        last_two = intList[-2:] # slice last 2 element in list
        for j in range(len(last_two)):
            temp = sum(last_two) # add elements together
          
    intList.append(temp) # add sum of elements to end of list
    n += 1

# print fibonacci sequence as a list
print("Fibonacci Sequence: \n ", intList)
