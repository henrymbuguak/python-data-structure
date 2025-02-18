# Creating a dictionary
# A dictionary stores key-value pairs, where keys must be unique and immutable
suppliers = {'apple': 4, 'banana': 4, 'Lemon': 12}
print("Initial Suppliers Dictionary:", suppliers)

# Assign a new value to an existing key
# Dictionaries are mutable, so you can update the value associated with a key
suppliers['banana'] = 10
print("Suppliers Dictionary after updating 'banana':", suppliers)

# Create a nested dictionary
# A nested dictionary is a dictionary where the values are also dictionaries
inventory = {
    'banana': {'price': 12, 'stock': 10},
    'apple': {'price': 15, 'stock': 9}
}
print("Nested Inventory Dictionary:", inventory)

# Convert a list of tuples into a dictionary using the dict() function
# Each tuple should contain a key-value pair
list_of_tuples = [('apple', 4), ('banana', 10), ('Lemon', 12)]
converted_dict = dict(list_of_tuples)
print("Dictionary converted from list of tuples:", converted_dict)

# Add a new key-value pair to the dictionary
suppliers['orange'] = 8
print("Suppliers Dictionary after adding 'orange':", suppliers)

# Remove an element from the dictionary using the del keyword
# Note: Raises a KeyError if the key does not exist
del suppliers['Lemon']
print("Suppliers Dictionary after removing 'Lemon':", suppliers)

# Remove an element safely using the pop() method
# Returns the value associated with the key and removes the key-value pair
# You can provide a default value to return if the key does not exist
removed_value = suppliers.pop('banana', None)
print("Removed value for 'banana':", removed_value)
print("Suppliers Dictionary after popping 'banana':", suppliers)

# Aliasing: Creating a reference to the same dictionary
# Changes to the alias will affect the original dictionary
suppliers_alias = suppliers
suppliers_alias['apple'] = 20
print("Suppliers Dictionary after modifying alias:", suppliers)

# Copying: Creating a shallow copy of the dictionary
# Changes to the copy will not affect the original dictionary
suppliers_copy = suppliers.copy()
suppliers_copy['orange'] = 15
print("Original Suppliers Dictionary:", suppliers)
print("Copied Suppliers Dictionary after modifying copy:", suppliers_copy)

# Additional operations you can perform with dictionaries:

# 1. Check if a key exists in the dictionary using the 'in' keyword
print("Is 'apple' in suppliers?", 'apple' in suppliers)

# 2. Get all keys in the dictionary using the keys() method
print("Keys in suppliers:", suppliers.keys())

# 3. Get all values in the dictionary using the values() method
print("Values in suppliers:", suppliers.values())

# 4. Get all key-value pairs in the dictionary using the items() method
print("Key-Value pairs in suppliers:", suppliers.items())

# 5. Merge two dictionaries using the update() method
new_suppliers = {'grape': 7, 'pear': 6}
suppliers.update(new_suppliers)
print("Suppliers Dictionary after merging with new_suppliers:", suppliers)

# 6. Clear all elements from the dictionary using the clear() method
suppliers.clear()
print("Suppliers Dictionary after clearing:", suppliers)