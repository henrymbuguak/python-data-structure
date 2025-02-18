# Create a simple string list
fruits = ['Apple', 'Lime', 'Lemon', 'Orange', 'Grapes']
print("Fruits List:", fruits)

# Create an integer list
prices = [30, 25, 15, 50, 100]
print("Prices List:", prices)

# Create a nested list (a list containing other lists)
nested_list = [[1, 2, 5], [10, 4, 9], [90, 34, 91]]
print("Nested List:", nested_list)

# Accessing elements in a list
# Python uses zero-based indexing, so fruits[2] refers to the third element
print("Third fruit in the list:", fruits[2])

# Accessing a sublist in a nested list
# nested_list[1] refers to the second sublist [10, 4, 9]
print("Second sublist in nested_list:", nested_list[1])

# Adding an element to the end of a list using append()
fruits.append('Banana')
print("Fruits List after adding 'Banana':", fruits)

# Checking if an element exists in a list using the 'in' keyword
# Returns True if the element is found, otherwise False
print("Is 'Lime' in the fruits list?", 'Lime' in fruits)

# Additional operations you can perform with lists:

# 1. Insert an element at a specific position using insert()
fruits.insert(2, 'Mango')  # Inserts 'Mango' at index 2
print("Fruits List after inserting 'Mango':", fruits)

# 2. Remove an element by value using remove()
fruits.remove('Lemon')  # Removes 'Lemon' from the list
print("Fruits List after removing 'Lemon':", fruits)

# 3. Remove an element by index using pop()
removed_fruit = fruits.pop(3)  # Removes and returns the element at index 3
print("Removed fruit:", removed_fruit)
print("Fruits List after popping index 3:", fruits)

# 4. Sort a list using sort()
prices.sort()  # Sorts the list in ascending order
print("Sorted Prices List:", prices)

# 5. Reverse a list using reverse()
fruits.reverse()  # Reverses the order of elements in the list
print("Reversed Fruits List:", fruits)

# 6. Find the length of a list using len()
print("Number of fruits in the list:", len(fruits))

# 7. Slice a list to get a sublist
# Syntax: list[start:end:step]
sublist = fruits[1:4]  # Gets elements from index 1 to 3 (end index is exclusive)
print("Sublist of fruits:", sublist)

# 8. Concatenate two lists using the + operator
more_fruits = ['Pineapple', 'Watermelon']
combined_list = fruits + more_fruits
print("Combined Fruits List:", combined_list)

# 9. Count occurrences of an element using count()
print("Number of times 'Apple' appears in the list:", fruits.count('Apple'))

# 10. Clear all elements from a list using clear()
fruits.clear()
print("Fruits List after clearing:", fruits)
