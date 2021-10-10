# comparing two number with the help of if else
'''
var1 = 34
var2 = int(input())

if var1 > var2:
    print("Grater")
if var1 == var2:
    print("Equal")
else:
    print("lesser")
'''
# Important Note : in python else if written like (elif)

# we are going to check element present in list or not
# list1 = [1, 2, 3, 4, 5]

'''
if 4 in list1:
    print("yes it is in list")
print(5 in list1)
if 5 in list1:
    print("yes it is in list")


print(15 in list1)
if 15 in list1:
    print("yes it is in list")


print(15 not in list1)
if 15 not in list1:
    print("No its not in the list")
'''

# challenge accepted

print("Enter your Age")
age = int(input())
if age > 18:
    print("You can Drive")
elif age == 18:
    print("Please come to the RTO office we will check yor doc and then permit you")
else:
    print("You are not eligible for driving any gare vehicle")