#Program 9: String Length Finder
#Problem Statement:
#Ask the user for a string and print the number of characters in it (excluding spaces).

user_string = input("Enter a string: ")
# Remove spaces from the string
string_without_spaces = user_string.replace(" ", "")
# Calculate the length of the string without spaces
length = len(string_without_spaces)
print(f"The number of characters (excluding spaces) is: {length}")