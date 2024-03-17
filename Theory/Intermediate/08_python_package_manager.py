######################################
### PYTHON PACKAEG MANAGER --- PIP ###
######################################

# PIP https://pypi.org


## What is PIP ?
"""
    PIP stands for Preferred installer program. We use pip to install different Python packages. 
    Package is a Python module that can contain one or more modules or other packages. A module 
    or modules that we can install to our application is a package. In programming, we do not 
    have to write every utility program, instead we install packages and import them to our applications.
"""

## Installing PIP
"""
    Go to your terminal or command prompt and copy and paste this: pip install pip
    Check if pip is installed by writing: pip --version
"""


## Installing packages using pip
# NUMPY 
"""
    NumPy is the fundamental package for scientific computing with Python. It contains among other things:
    - a powerful N-dimensional array object
    - sophisticated (broadcasting) functions
    - tools for integrating C/C++ and Fortran code
    - useful linear algebra, Fourier transform, and random number capabilities
"""

import numpy    # Terminal Command: pip install numpy

print(numpy.version.version)

numpy_array = numpy.array([34, 43, 43, 66, 76, 10, 2])
print(type(numpy_array))    # <class 'numpy.ndarray'>
print(numpy_array * 2)      # [ 68  86  86 132 152  20   4]


# Pandas is an open source, BSD-licensed library providing high-performance, easy-to-use 
# data structures and data analysis tools for the Python programming language.

import pandas   # pip install pandas

# List of Packages
# To see the installed packages on our machine. We can use pip followed by list.
# pip list

# Uninstalling Packages
# If you do not like to keep the installed packages, you can remove them using the following command.
# pip uninstall pandas

# Show Package
# To show information about a package
# If we want even more details, just add --verbose
# pip show numpy


# PIP Freeze
# Generate installed Python packages with their version and the output is suitable to use it in a requirements file.
# pip freeze



# Reading from URL
# Requests package allows to open a network connection and to implement CRUD(create, read, update and delete) operations.
import requests     # pip install requests

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(response)
print(response.status_code)
print(response.json())


# Let us import a web browser module, which can help us to open any website.
import webbrowser # web browser module to open websites

# list of urls: python
url_lists = [
    'http://www.python.org',
    'https://www.linkedin.com/in/asabeneh/',
    'https://github.com/Asabeneh',
    'https://twitter.com/Asabeneh',
]

# opens the above list of websites in a different tab
for url in url_lists:
    webbrowser.open_new_tab(url)
    
    
    
    
# Creating a Package
# We organize a large number of files in different folders and sub-folders based on some criteria, 
# so that we can find and manage them easily. As you know, a module can contain multiple objects, 
# such as classes, functions, etc. A package can contain one or more relevant modules. 
# A package is actually a folder containing one or more module files. 

# Arithmetics Package

from mypackage import arithmetics

print(arithmetics.add_numbers(1, 2, 3, 5))     # 11
print(arithmetics.subtract(5, 3))              # 2
print(arithmetics.multiple(5, 3))              # 15
print(arithmetics.division(5, 3))              # 1.6666666666666667
print(arithmetics.remainder(5, 3))             # 2
print(arithmetics.power(5, 3))                 # 125

from mypackage import greet
print(greet.greet_person('Luis', 'López'))     # Luis López, welcome to this package!

#  The init.py exposes specified resources from its modules to be imported to other python files. 
#  An empty init.py file makes all functions available when a package is imported. 
#  The init.py is essential for the folder to be recognized by Python as a package.


## Further Information About Packages
# Database --> SQLAlchemy or SQLObject - Object oriented access to several different database systems --- pip install SQLAlchemy
# Web Development --> Django - High-level web framework. --- pip install django ||| Flask - micro framework for Python based on Werkzeug, Jinja 2. (It's BSD licensed) --- pip install flask
# HTML Parser --> Beautiful Soup - HTML/XML parser designed for quick turnaround projects like screen-scraping, will accept bad markup. --- pip install beautifulsoup4
# XML Processing --> ElementTree - The Element type is a simple but flexible container object, designed to store hierarchical data structures
# GUI --> PyQt - Bindings for the cross-platform Qt framework. ||| TkInter - The traditional Python user interface toolkit.
# Data Analysis, Data Science and Machine learning --> Numpy ||| Pandas ||| SciPy ||| Scikit-Learn ||| TensorFlow ||| Keras
# Network --> requests: is a package which we can use to send requests to a server(GET, POST, DELETE, PUT) --- pip install requests