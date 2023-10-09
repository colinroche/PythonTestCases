string = "get non-matching characters"
string_list = []
list_match = []
list_non_match = []

for i in range(len(string)):  # iterate over elements in string
    for j in range(len(string)):
        string_list.append(string[i])  # add element to string_list
        if i < j:
            if string[i] == string[j]: # is element in iterates match add them to match list.
                list_match.append(string[i])

string_list = set(string_list) # convert iterables of same type to set of iterables.
list_match = set(list_match)

list_non_match = string_list - list_match # remove matching element sets from all element sets

print("List of characters in string: ", string_list)
print("List of matching characters in string: ", list_match)
print("List of non-matching characters in string: ", list_non_match)
