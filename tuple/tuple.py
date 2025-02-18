# Create a tuple containing integers
int_tuple = (3, 5, 7, 4)
print("Integer Tuple:", int_tuple)

# Create a tuple containing strings
string_tuple = ("apple", "banana", "cherry")
print("String Tuple:", string_tuple)

# Create a nested tuple (a tuple containing other tuples)
nested_tuple = ((3, 5, 7, 4), (47, 35, 78, 10), (2, 8, 22, 32))
print("Nested Tuple:", nested_tuple)

# Accessing elements in a tuple
# Python uses zero-based indexing, so int_tuple[0] refers to the first element
print("First element in int_tuple:", int_tuple[0])

# Check if an element exists in a tuple using the 'in' keyword
# Returns True if the element is found, otherwise False
print("Is 5 in int_tuple?", 5 in int_tuple)

# Find the length of a tuple using the len() function
print("Length of string_tuple:", len(string_tuple))

# Additional operations you can perform with tuples:

# 1. Concatenate two tuples using the + operator
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined_tuple = tuple1 + tuple2
print("Combined Tuple:", combined_tuple)

# 2. Repeat a tuple using the * operator
repeated_tuple = tuple1 * 3
print("Repeated Tuple:", repeated_tuple)

# 3. Count occurrences of an element using count()
print("Number of times 5 appears in int_tuple:", int_tuple.count(5))

# 4. Find the index of an element using index()
# Returns the index of the first occurrence of the element
print("Index of 7 in int_tuple:", int_tuple.index(7))

# 5. Unpacking a tuple
# Assign elements of a tuple to variables
a, b, c, d = int_tuple
print("Unpacked elements:", a, b, c, d)

# 6. Convert a list to a tuple using the tuple() function
my_list = [1, 2, 3, 4]
converted_tuple = tuple(my_list)
print("Converted Tuple from List:", converted_tuple)

# 7. Iterate over a tuple using a for loop
print("Elements in string_tuple:")
for fruit in string_tuple:
    print(fruit)

# 8. Check if all elements in a tuple are True using all()
bool_tuple = (True, True, False)
print("Are all elements in bool_tuple True?", all(bool_tuple))

# 9. Check if any element in a tuple is True using any()
print("Is any element in bool_tuple True?", any(bool_tuple))

# 10. Create a tuple with a single element (note the trailing comma)
single_element_tuple = (42,)
print("Single Element Tuple:", single_element_tuple)