myname = "atul is a good boy"
name2 = "MY NAME IS ATUL"
print(myname[3])  # here i am trying to print the 3rd number index value in string
# more example of string slicing are
print(myname[0:4])
# to check the length of myname string we use len method
print(len(myname))
# to skip one character in any string we use like
print(myname[0:18:2])
'''
 In this line of code (myname) is a string and [0:18:2] in this bracket o is indicate oth index value in that string 
 and 18 indicate the length of the string 
 and 2 is basically use to skip the one latte in that string.
'''

# to flip the string we use like that
print(myname[::-1])
# and you can skip characters in that form also how much char you want to skip write in the place of -1

# Some String function
print(myname.isalnum())
print(myname.isalpha())
print(myname.endswith("boy"))
print(myname.count("o"))
print(myname.capitalize())
print(myname.find("is"))
print(name2.lower())
print(myname.upper())
print(myname.replace("atul", "Boss"))

