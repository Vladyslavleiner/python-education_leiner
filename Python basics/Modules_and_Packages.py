import re

# Your code goes here

list_of_functions = dir(re)
functions_with_find = []
for i in list_of_functions:
    if "find" in i:
        functions_with_find.append(i)
print(sorted(functions_with_find))