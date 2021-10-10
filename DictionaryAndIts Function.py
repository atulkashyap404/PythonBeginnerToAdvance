# Dictionary is nothing but key value pairs
d1 = {}  # now we can check what is the type of this piece of code
print(type(d1))

d2 = {"cat":"cat is a pet animal", "Dog":"dog is also pet animal", "Ram":"Ram is a humane"}
print(d2["Dog"])

# Dictionary into Dictionary
d3 = {"Hello":"World", "Men":"Women", "Boy":"Girl", "Animals":{"Domestic Animals":"Dog", "Wild Animals":"Lion"}}
print(d3["Animals"]["Domestic Animals"])

# how to add element in dictionary
d2["Atul"] = "He is Boss and god of the python"
print(d2)

# How to delete the elements from the dictionary
del d2["Atul"]
print(d2)

# performing some function
d4 = d2  # now here d4 is referring to d2 dictionary so
# if we delete any thing from this d4 referring dictionary its effect the original d2 dictionary.
del d4["cat"]
print(d2)

# so if we want that our d2 original dictionary not change by any referring dictionary we use this
d5 = d3.copy()
del d5["Animals"]
print(d3)
print(d5)

# get function
print(d3.get("Boy"))

# update the dictionary using update function
d2.update({"Atul":"Manjhi"})
print(d2)

# to print the Dictionary keys
print(d2.keys())

# to print the items in the dictionary
print(d2.items())

# user input the key and print the key value
print("Enter your query\n")
qur = input()
print(d3[qur])

