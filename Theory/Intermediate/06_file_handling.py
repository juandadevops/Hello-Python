### FILE HANDLING ###

import os

# .txt file #
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


# .json file #
import json

json_file = open("Theory/Intermediate/my_file.json", "w+")    # Leer y escribir

json_test = {
    "name" : "Luis",
    "surname" : "Ruiz",
    "age" : 35,
    "languages": ["Python", "Swift", "Java"] ,
    "website" : "https://google.com"
}

json.dump(json_test, json_file, indent=4)
# json.dump(json_test, json_file, indent=4) 


json_file.close()

with open("Theory/Intermediate/my_file.json", "r+") as my_other_file:
    for line in my_other_file.readlines():
        print(line)
    
print()

json_dict = json.load(open("Theory/Intermediate/my_file.json"))
print(json_dict)
print(json_dict["name"])
    
    
# .csv file
import csv


csv_file = open("Theory/Intermediate/my_file.csv", "w+")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "surname", "age", "language", "website"])
csv_writer.writerow(["Luis", "Alonso", "33", "Spanish", "https://google.com"])
csv_writer.writerow(["Fernando", "Ruiz", "22", "English", "https://google.com"])

csv_file.close()

with open("Theory/Intermediate/my_file.csv", "r+") as my_other_file:
    for line in my_other_file.readlines():
        print(line)
        

# .xlsx file
# import xlrd # Debe instalarse el módulo


# .xml file
import xml
import xml.etree.ElementTree as ET

# xml_file = open("Theory/Intermediate/my_file.xml", "w+")

tree = ET.parse('Theory/Intermediate/my_file.xml')
root = tree.getroot()
print('Root tag:', root.tag)
print('Attribute:', root.attrib)
for child in root:
    print('field: ', child.tag)