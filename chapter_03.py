# ---------------Strings-----------------

# b="Harry's" 
# print(b)
# print(type(b))

# -------------slicing a string or parts of string ----------
    # name = "Harry"
    # greeting = "Good Morning, "
    # print(type(name))
    # print(greeting + name) -- printing of two concantinating strings
    # c = greeting + name -- concatinating of strings
    # print(c)
    # 

# name = "Harry"
# print(name[3])
# name[3] ="d" -----doesn't work

# name = "Harry is a good boy"
# print(name[4:9])  ---- output: __y is__.. this is known as slicing

# name = "Harry"
# print(name[:4]);  '''Automatically starts with 0 index'''
# print(name[2:]);  '''Automatically end with last index'''
# print(name[-4:-1])


# name = "panduchery"
# d = name[::2]
# print(d)

# name = "once upon a time in mumbai"

# string functions -------------->>>>
# print(len(name))
# # print(name.endswith("i")); '''Gives true or false by matching from last'''
# # print(name.count("ce"));  '''Number of occurance in string or char count'''
# print(name)
# print(name.capitalize())
# print(name.find("upons"))
# print(name.replace("once", "Earlier"))
# 


# name  = "harry is\n\tan y\'\\outuber and \tsoftware devloper"
# print(name)






# -------------practice sets --------------
# q1 -------------------------------------->
# greeting = "Good Afternoon "
# name = input("Enter your name: ")
# print(greeting + name);

# q2 -------------------------------------->
# WAP to fill a letter templete
letter = '''Dear name\n\tYou are selected!\n\tdate.''';
name = input("Enter your name: ");
date = input("Enter date [format: DD/MM/YY]: ");
letter = letter.replace("name", name);
letter = letter.replace("date", date);
print(letter);


# q3 ---------------------------------------->
# strings = "Once upon a time in mumbai  dubara"
# print(strings.find("  "))

# q4 --------------------------------------->
# strings = "Once upon a time in mumbai  dubara"
# print(strings)
# print(strings.replace("  ", " "))

# q5 --------------------------------------->
letter = "Dear Harry,\n\t\tThis python course is nice.\n\t\tThanks!"
print(letter)
print(letter)