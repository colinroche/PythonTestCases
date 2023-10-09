charCheck = "a"
string = "Counting occurrences of specific character 'a' in string 123456789"
count = 0

for i in string:  # iterating through each element in string
    if i.isalpha() and i == charCheck:  # checking if element is a character
        count += 1  # adding to count if element is same character

print(count)
