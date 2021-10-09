grocery = ["harpik", "suger", "oil", "lollypoop", "deodrant"]
print(grocery)
# mixed list
grocery2 = ["harpik", "suger", "oil", "lollypoop", "deodrant", "20-20 Biscuits", "45", "420"]
print(grocery2)
'''
list is mutable : it means it can be change 
'''
# to print the particular items from list we use
print(grocery2[2])  # we use index position to pic items from list

# number list
numbers = ["13", "92", "63", "4", "523"]
print(numbers)

# list methods
# important note sort and reverse is change the original list
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

# list slicing
# important note in slicing, slicing is not effect the original list
num = [1, 2, 3, 4, 5]
print(num[1:])
print(num[1:4])
print(num[1:])
# extended slicing
print(num[::1])  # default value is 1
print(num[::2])
# note do not take -2 or -3 in slicing in string or list
print(max(num))
print(min(num))

# to add some thing in end of the list we use append method
num.append(6)
print(num)
# inserting some number vale in list
num.insert(2, 34)
'''in this insert method the first argument is the index place value and then the number which you want to insert'''
print(num)
num.remove(34)
print(num)

# pop method is use to pop the last element of the list
num.pop()
print(num)


'''
tuples is immutable: it means it can not be change
'''

tp = (1, 2, 3, 40)  # now we can not change the value of tp like tp[1] = 8
print(tp)

# how to swap two numbers
# Traditional way to swap the two numbers
a = 1
b = 2
temp = a
a = b
b = temp
print(a, b)

# in python
x = 3
y = 6
x, y = y, x
print(x, y)