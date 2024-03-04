
def remove_item(lista, item):
    """ Function that takes a list and an item parameters and it returns a list with the item removed from it

    Args:
        lista (list): List
        item (any): item to remove from the list

    Returns:
        list: New list with the item removed from it
    """
    if type(lista) != list:
        return "ERROR: The parameter provided must be a list."
    else:
        new_list = lista.copy()  # Create a copy to avoid modifying the original list
        if lista.count(item) == 0:
            return "ERROR: The item passed as an argument does not exist in the list provided."
        else:
            new_list.remove(item)
            return new_list

original_list = ["apple", "banana", "cherry", "orange"]
new_item = "banana"
error_item = "watermelon"
result = remove_item(original_list, new_item)
resultError = remove_item(original_list, error_item)

print("Original List:", original_list)          # ['apple', 'banana', 'cherry', 'orange']
print("List with Item Deleted:", result)        # ['apple', 'cherry', 'orange']
print(resultError)                              # ERROR: The item passed as an argument does not exist in the list provided.

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))         # ['Potato', 'Tomato', 'Milk']
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))                  # [2, 7, 9]