
def add_item(lista, item):
    """ Function that takes a list and an item parameters and it returns a list with the item added at the end.

    Args:
        lista (list): List 
        item (any): item to add at the end of the list

    Returns:
        list: The new list with the item added at the end
    """
    if type(lista) != list:
        return "ERROR: The parameter provided must be a list."
    else:
        new_list = lista.copy()  # Create a copy to avoid modifying the original list
        new_list.append(item)
        return new_list
    
original_list = ["apple", "banana", "cherry"]
new_item = "orange"
result = add_item(original_list, new_item)

print("Original List:", original_list)      # ['apple', 'banana', 'cherry']
print("List with Item Added:", result)      # ['apple', 'banana', 'cherry', 'orange']

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat']
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))      # [2, 3, 7, 9, 5]