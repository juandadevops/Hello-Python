
def is_empty(value):
    """ Takes a parameter and it checks if it is empty or not

    Args:
        value (_type_): Parameter to check if is empty or not

    Returns:
        _type_: True if the parameter is empty or False id doesn't
    """
    if value is None:
        return True
    elif isinstance(value, str) and not value.strip():
        return True
    elif isinstance(value, (list, tuple, dict, set)) and not value:
        return True
    else:
        return False

# Example usage
empty_string = ""
non_empty_string = "Hello, World!"
empty_list = []
non_empty_list = [1, 2, 3]
empty_tuple = ()
non_empty_tuple = (1, 2, 3)


print(f"Is empty string empty? {is_empty(empty_string)}")           # True
print(f"Is non-empty string empty? {is_empty(non_empty_string)}")   # False
print(f"Is empty list empty? {is_empty(empty_list)}")               # True
print(f"Is non-empty list empty? {is_empty(non_empty_list)}")       # False
print(f"Is empty tuple empty? {is_empty(empty_tuple)}")             # True
print(f"Is non-empty tuple empty? {is_empty(non_empty_tuple)}")     # False