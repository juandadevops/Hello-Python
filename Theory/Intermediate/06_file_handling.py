#####################
### FILE HANDLING ###
#####################
import os


"""
     We usually store our data in different file formats. 
     In addition to handling files, we will also see different file formats(.txt, .json, .xml, .csv, .tsv, .excel)
     File handling is an import part of programming which allows us to create, read, update and delete files. 
     In Python to handle data we use open() built-in function.
"""

# Syntax
# open('filename', mode) # mode(r, a, w, x, t,b)  could be to read, write, update

"""
    "r" - Read - Default value. Opens a file for reading, it returns an error if the file does not exist
    "a" - Append - Opens a file for appending, creates the file if it does not exist
    "w" - Write - Opens a file for writing, creates the file if it does not exist
    "x" - Create - Creates the specified file, returns an error if the file exists
    "t" - Text - Default value. Text mode
    "b" - Binary - Binary mode (e.g. images)
"""

###############################
## Opening Files for Reading ##
###############################

# The default mode of open is reading, so we do not have to specify 'r' or 'rt'.


############################################
## Opening Files for Writing and Updating ##
############################################

"""
    To write to an existing file, we must add a mode as parameter to the open() function:
        "a" - append - will append to the end of the file, if the file does not it creates a new file.
        "w" - write - will overwrite any existing content, if the file does not exist it creates.
"""

#############
# .txt File #
txt_file = open("Theory/Intermediate/my_file.txt", "w+")    # Read and Write
txt_file.write("My name IS Luis\nMy surname is Gonzalez\n40 years old\nPython\n.NET")

"""
    read(): read the whole text as string.
    readline(): read only the first line
    readlines(): read all the text line by line and returns a list of lines
    Another way to get all the lines as a list is using splitlines()
"""
# print(txt_file.read())    # Read the whole text
# print(txt_file.read(10))  # Read the first 10 characters
# print(txt_file.readline())
# print(txt_file.readlines())
for line in txt_file.readlines():
    print(line)
    
txt_file.write("\nI also like Java language")
print(txt_file.readline())

txt_file.close()


"""
    After we open a file, we should close it. 
    There is a high tendency of forgetting to close them. 
    There is a new way of opening files using with - closes the files by itself.
"""


with open("Theory/Intermediate/my_file.txt") as f:
    lines = f.read().splitlines()
    print(type(lines))
    print(lines)


####################
## Deleting Files ##
####################

"""
os.remove("Theory/Intermediate/my_file.txt")

OR

if os.path.exists("Theory/Intermediate/my_file.txt"):
    os.remove("Theory/Intermediate/my_file.txt")
else:
    print('The file does not exist')
"""


################
## File Types ##
################

###########################
# File with TXT Extension #
"""
    File with txt extension is a very common form of data and we have covered it in the previous section
"""


############################
# File with JSON Extension #
"""
    JSON stands for JavaScript Object Notation. Actually, it is a stringified JavaScript object or Python dictionary.
"""
import json

json_file = open("Theory/Intermediate/my_file.json", "w+")    # Leer y escribir

json_test = {
    "name" : "Luis",
    "surname" : "Ruiz",
    "age" : 35,
    "languages": ["Python", "Swift", "Java"] ,
    "website" : "https://google.com"
}

# Saving as JSON File
"""
    Save our data as a json file. Let us save it as a json file using the following steps. 
    For writing a json file, we use the json.dump() method, it can take dictionary, output file, ensure_ascii and indent.
"""
json.dump(json_test, json_file, indent=4)
json_file.close()

with open("Theory/Intermediate/my_file.json", "r+") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

# Changing JSON to Dictionary
"""
    To change a JSON to a dictionary, first we import the json module and then we use loads method.
"""
json_dict = json.load(open("Theory/Intermediate/my_file.json"))
print(json_dict)
print(json_dict["name"])

# Changing Dictionary to JSON
"""
    To change a dictionary to a JSON we use dumps method from the json module.
"""
    
    
############################
# File with CSV Extension #
"""
    CSV stands for comma separated values. 
    CSV is a simple file format used to store tabular data, such as a spreadsheet or database. 
    CSV is a very common data format in data science.
"""
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
        

############################
# File with XLSX Extension #
"""
    To read excel files we need to install xlrd package. We will cover this after we cover package installing using pip.
"""
# import xlrd       # The module must be installed


############################
# File with XML Extension #
"""
    XML is another structured data format which looks like HTML. In XML the tags are not predefined. 
    The first line is an XML declaration. 
    The person tag is the root of the XML. 
    The person has a gender attribute.
    Example XML:
        <?xml version="1.0"?>
        <person gender="female">
            <name>Asabeneh</name>
            <country>Finland</country>
            <city>Helsinki</city>
            <skills>
                <skill>JavaScrip</skill>
                <skill>React</skill>
                <skill>Python</skill>
            </skills>
        </person>
"""
import xml
import xml.etree.ElementTree as ET

tree = ET.parse('Theory/Intermediate/my_file.xml')
root = tree.getroot()
print('Root tag:', root.tag)
print('Attribute:', root.attrib)
for child in root:
    print('field: ', child.tag)