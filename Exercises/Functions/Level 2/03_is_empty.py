# Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(value):
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


print(f"Is empty string empty? {is_empty(empty_string)}")
print(f"Is non-empty string empty? {is_empty(non_empty_string)}")
print(f"Is empty list empty? {is_empty(empty_list)}")
print(f"Is non-empty list empty? {is_empty(non_empty_list)}")
print(f"Is empty tuple empty? {is_empty(empty_tuple)}")
print(f"Is non-empty tuple empty? {is_empty(non_empty_tuple)}")