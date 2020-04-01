course = "Python Programming"  # single or double quotes

# triple quotation mark we use when the sentences will brake into multiple lines
""" 
This is triple quotation mark 
"""

print(len(course))  # embedded function into python to get length of a string
print(course[0])  # get first char from the word
print(course[-1])  # get last char form the word
# get first three charcters form the word, using SLICE function
print(course[0:3])
# get first charcters form the word but to the end of whole sentence
print(course[0:])
# get first three charcters form the word, using SLICE function
print(course[:3])
print(course[:])  # get whole string


# Escape from the string

course_python = 'Python "Programming"'  # print double quotation in string
# escape dounle quotes and print double quotation in string
course_python1 = "Python \"Programming\""
# print new line and double quotation in string
course_python1 = "Python \n\"Programming\""
print(course_python1)

# \"
# \'
# \\
# \n

# Formated string

first_name = "Ervin"
last_name = "Pepic"
full_name = first_name + ' ' + last_name  # old way
# the curly braces are ignored at runtime
formated_full_name = f"{first_name} {last_name}"
print(full_name)
print(formated_full_name)


# String functions

# len() # it's general function it's not just for string

word_for_testing_string_fuction = "Some words just to test how string fucntions woork..."
print(word_for_testing_string_fuction.upper())
print(word_for_testing_string_fuction.lower())
print(word_for_testing_string_fuction.title())
print(word_for_testing_string_fuction.find("jus"))

# strip method()..cut all white spaces before and after start of string, also we have lstrip for left strio or rstrip
strip_string_test = "   This need to     beeee     stripped   "
print(strip_string_test.strip())
print(strip_string_test.replace("e", "l"))
print("p" not in strip_string_test)
print("p" in strip_string_test)
