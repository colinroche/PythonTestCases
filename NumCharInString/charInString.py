count = 0
string = "098checking digits1448"

for i in string:  # iterating through each element in string
    if i.isalpha():  # checking if element is a character
        count += 1  # adding to count if element is a character

print(count)
