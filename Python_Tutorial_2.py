print("This line is printing directly on print() function.", end='\n\n')

# store string in a variable and print.
str_variable = "This is the string storing in a variable."
print(str_variable, end='\n\n')
# ------------------------------------------------------------

# print ' in a string
single_quat_str = "This is the string having single quotation (') in it."
print(single_quat_str, end='\n\n')
# ------------------------------------------------------------

# another way of printing single quotation
single_quat_str = 'This is the another way of printing single quotation(\') in a string.'
print(single_quat_str, end='\n\n')
# ------------------------------------------------------------

# another way of print single quotation
multi_line_str = """This is the 1st line of the string
This is the 2nd line of the string
This is the 3rd line of the string
"""
print(multi_line_str, end='\n')
# ------------------------------------------------------------

# Length of the string
len_of_the_str = len(multi_line_str)
print("Length of the string is: {}".format(len_of_the_str), end='\n\n')
# ------------------------------------------------------------

# CHAR in the string at any index position; 0 based index
str_variable = "This is a sample string"
print(str_variable)
print("The CHAR of at position 5 in the string is: " + str_variable[5], end='\n\n')
# ------------------------------------------------------------

# String at certain given range
str_variable = "This is a sample string"
print(str_variable)
print("The CHARs at position '4~10' in the string are: " + str_variable[4:10], end='\n')
print("The CHARs at position '0~10' in the string are: " + str_variable[:10], end='\n')
print("The CHARs at position  '5~~' in the string are: " + str_variable[5:], end='\n\n')
# ------------------------------------------------------------

# String UPPERCASE, LOWERCASE
str_variable = "This is a sample string"
print("Uppercase: " + str_variable.upper())
print("Lowercase: " + str_variable.lower(), end='\n\n')
# ------------------------------------------------------------

# Count a particular string or CHAR
str_variable = "This is a sample string. This given string is not too long."
print("Count word 'This': " + str(str_variable.count("This")))
print("Count word 'This': " + str(str_variable.count("xyz")))
print("Count char 'a': " + str(str_variable.count('a')), end='\n\n')
# ------------------------------------------------------------

# Replace string
str_variable = "This is a sample string"
print(str_variable)
str_replaced = str_variable.replace("sample", "complex")
print(str_replaced, end='\n\n')

# ------------------------------------------------------------

# String formation
greeting = "Hello"
name = "Jhon"

message = "{} {}, Welcome to Python Tutorial!".format(greeting, name)
print(message)

message = f"{greeting} {name}, This is the another way to string formation."
print(message, end='\n\n')
