var1 = "Hello world"
var = " I am Atul"
var6 = " 20"
var2 = 4
var3 = 3.4
var4 = 3.45
var5 = 'A'
print(type(var1))
print(type(var2))
print(type(var3))
print(type(var4))
print(type(var5))

# contacting two string
print(var1+var)
print(var1+var6)

# Typecasting

print(int(var6)+int(var2))  # typecasting string into integer where var6 is a string type variable
'''
typecasting datatype

str
float
int
'''

# how to print hello world 10 times without using loop and multiples of print function
print(10 * "Hello world\n")

# how to take user input
print("Enter your number")
num = input()  # input() take always string value so if you want to add that input value
# then you have to typecast that value in your requirement data type
print(int(num) + 10)