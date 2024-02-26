### STRINGS ###

my_string = "Test String 0"
print(len(my_string))

my_new_line_string = "This is a String\nwith new line"
print(my_new_line_string)

my_tab_string = "\tThis is a String with tabulation"
print(my_tab_string)


# Format
print("Format")
name = "Juan David"
surname = "Corrales"
age = 24
print("My name is {} {} and I am {}".format(name, surname, age))
print("My name is %s %s and I am %d" %(name, surname, age))
print(f"My name is {name} {surname} and I am {age}")

# Desempaqueado de caracteres
print("Desempaqueado")
language = "python"
a, b, c, d, e, f = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# División
print("Division")
language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

# Reverse
print("Reverse")
reversed_language = language[ ::-1]
print(reversed_language)

# Functions
print("Functions")
print(language.capitalize())
print(language.upper())
print(language.lower())
print(language.count("o"))
print(language.casefold())
print("1".isnumeric())
print(language.upper().isupper())
print(language.startswith("py"))
