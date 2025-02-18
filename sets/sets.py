# Create a set containing integers
my_set = {1, 2, 3, 4, 5}
print("Initial Set:", my_set)

# Add an element to the set using the add() method
my_set.add(10)
print("Set after adding 10:", my_set)

# Remove an element from the set using the remove() method
# Note: If the element does not exist, remove() will raise a KeyError
my_set.remove(4)
print("Set after removing 4:", my_set)

# Check if an element exists in the set using the 'in' keyword
# Returns True if the element is found, otherwise False
print("Is 6 in the set?", 6 in my_set)

# Perform a union of two sets using the union() method or the | operator
# Union combines all unique elements from both sets
my_set2 = {8, 9, 3, 4}
print("Union of my_set and my_set2:", my_set.union(my_set2))

# Perform an intersection of two sets using the intersection() method or the & operator
# Intersection returns elements common to both sets
print("Intersection of my_set and my_set2:", my_set2.intersection(my_set))

# Additional operations you can perform with sets:

# 1. Remove an element safely using discard()
# Unlike remove(), discard() does not raise an error if the element is not found
my_set.discard(10)
print("Set after discarding 10:", my_set)

# 2. Remove and return an arbitrary element using pop()
# Useful when you don't care which element is removed
popped_element = my_set.pop()
print("Popped element:", popped_element)
print("Set after popping an element:", my_set)

# 3. Clear all elements from a set using clear()
my_set2.clear()
print("my_set2 after clearing:", my_set2)

# 4. Find the difference between two sets using difference() or the - operator
# Returns elements in the first set that are not in the second set
difference_set = my_set.difference({3, 5})
print("Difference between my_set and {3, 5}:", difference_set)

# 5. Find the symmetric difference between two sets using symmetric_difference() or the ^ operator
# Returns elements that are in either set but not in both
symmetric_diff_set = my_set.symmetric_difference({2, 5, 8})
print("Symmetric difference between my_set and {2, 5, 8}:", symmetric_diff_set)

# 6. Check if a set is a subset of another set using issubset()
# Returns True if all elements of the first set are in the second set
print("Is {1, 2} a subset of my_set?", {1, 2}.issubset(my_set))

# 7. Check if a set is a superset of another set using issuperset()
# Returns True if all elements of the second set are in the first set
print("Is my_set a superset of {1, 2}?", my_set.issuperset({1, 2}))

# 8. Create a frozen set (an immutable version of a set)
frozen_set = frozenset([1, 2, 3, 4])
print("Frozen Set:", frozen_set)