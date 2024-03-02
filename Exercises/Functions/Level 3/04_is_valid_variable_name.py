
def is_valid_variable_name(variable_name):
    """ Function that check if provided variable is a valid python variable

    Args:
        variable_name (String): Varible to check if it's a valid python variable

    Returns:
        _type_: True if it's a valid python variable or False is not
    """
    
    if not isinstance(variable_name, str):
        return False  # Variable name must be a string
    
    if not variable_name.isidentifier():
        return False  # Must be a valid identifier
    
    # Check if the variable name is a Python keyword
    import keyword
    if keyword.iskeyword(variable_name):
        return False
    
    return True

# Example usage
variable1 = "valid_variable"
variable2 = "123_invalid_variable"
variable3 = "for"  # Python keyword

print(f"Is '{variable1}' a valid variable name? {is_valid_variable_name(variable1)}")  # True
print(f"Is '{variable2}' a valid variable name? {is_valid_variable_name(variable2)}")  # False
print(f"Is '{variable3}' a valid variable name? {is_valid_variable_name(variable3)}")  # False