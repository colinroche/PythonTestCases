count = 0
string = "098checking digits1448"

for i in string:  # iterating through each element in string
    if i.isnumeric():  # checking if element is numerical
        count += 1  # adding to count if element is numerical

print(count)
