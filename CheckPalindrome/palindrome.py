string = input("Enter string: ")  # inputting string
stringLength = len(string)  # calculate length of the list
slicedString = string[stringLength::-1]  # slicing

if string == slicedString:  # check if string and reversed string match
    print("String is a palindrome")
else:
    print("String is not a palindrome")
