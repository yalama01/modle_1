#take a user input string

string = input("Enter a string: ")

#shift lower case to the left and upper case to the right
lower = ""
upper = ""
for letter in string:
    if letter.islower():
        lower += letter
    else:
        upper += letter
print(lower + upper)