### FILE HANDLING ###

import os

# .txt file
txt_file = open("Theory/Intermediate/my_file.txt", "w+")    # Leer y escribir
txt_file.write("Mi nombre es Luis\nMi apellido es Gonzalez\n40 años\nPython\n.NET")

# print(txt_file.read())    # Lee todo el txt
# print(txt_file.read(10))  # Lee loos primeros 10 caracteres
# print(txt_file.readline())
# print(txt_file.readline())
# print(txt_file.readlines())
for line in txt_file.readlines():
    print(line)
    
txt_file.write("\nTambien me gusta el lenguaje Java")
print(txt_file.readline())

txt_file.close()

# os.remove("Theory/Intermediate/my_file.txt")