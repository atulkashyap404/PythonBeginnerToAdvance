# Set is a collection of well defined objects
# printing the type of var is
s = set()
print(type(s))

# easy way to create set through list
s_from_list = set([1, 2, 3, 4])
print(type(s_from_list))
print(s_from_list)

# to add element in set use
s.add(1)
s.add(1)
'''
here is the most imp. note after this piece of code you think set is now{1,1}
no set{1,1} is not set is collection of well defined object so its show you {1} only no, 
duplicate value can print in set.
'''
s.add(2)
print(s)

# now performing some set function operation
s1 = set()
s1.add(1)
s1.add(2)
s1.add(3)
s1.add(4)
s2 = s1.union({1, 2, 3, 5, 6, 7, 8})
print(s1)
print("Length of s2 is = ", len(s2))
print("max of s2 is = ", max(s2))
print("minimum of s2 is = ", min(s2))
print("union of s1 and s2 = ", s2)
s2 = s1.intersection({1, 2, 3, 5, 6, 7, 8})
print("intersection of s1 and s2 = ", s2)

# making new set
s3 = {1, 3, 4, 5, 6}
s4 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print("set s3 and s4 is disjoint = ", s3.isdisjoint(s4))
s3.remove(6)
print(s3)

