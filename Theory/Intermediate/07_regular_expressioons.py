###########################
### REGULAR EXPRESSIONS ### 
###########################

###################
## The re Module ##
###################
"""
To use RegEx in python first we should import the RegEx module which is called re.
"""
import re


##########################
## Methods in re Module ##
##########################
"""
    To find a pattern we use different set of re character sets that allows to search for a match in a string.
"""

#########
# MATCH #
"""
    Searches only in the beginning of the first line of the string and returns matched objects if found, else returns None.
"""
my_string = "This is lesson number 7: Lesson called: Regular Expressions"
my_other_string = "This is not lesson number 6: File Management"

match = re.match("This is lesson", my_string, re.I)     # re.I is case ignore
print(match)            # <re.Match object; span=(0, 14), match='This is lesson'>
print(match.span())     # (0, 14)

start, end = match.span()
print(start, end)   # 0 14
substring = my_string[start:end]
print(substring)    # This is lesson (match.match())

match = re.match("This is lesson", my_other_string)

# if not(match == None):    # Another way to check None
# if match != None)         # Another way to check None
# if match is not None:     # Another way to check None

print(re.match("Regular Expressions", my_string))   # None


##########
# SEARCH #
"""
    Returns a match object if there is one anywhere in the string, including multiline strings.
"""
search = re.search("lesson", my_string, re.I)
print(search)       # <re.Match object; span=(8, 14), match='lesson'>
start, end = search.span()
print(start, end)   # 8 14
substring = my_string[start:end]
print(substring)    # lesson (search.match())

"""
    search is much better than match because it can look for the pattern throughout the text. 
    Search returns a match object with a first match that was found, otherwise it returns None.
"""


###########
# FINDALL #
"""
    A much better re function is findall. This function checks for the pattern through the whole string and returns all the matches as a list.
    Returns a list containing all matches
"""
findall = re.findall("lesson", my_string, re.I)
print(findall)  # ['Lesson', 'lesson']
"""
    Since we are using re.I both lowercase and uppercase letters are included. 
    If we do not have the re.I flag, then we will have to write our pattern differently. 
"""
findall = re.findall('Lesson|lesson', my_string)
print(findall)  # ['Lesson', 'lesson']

findall = re.findall('[Ll]esson', my_string)
print(findall)  # ['Lesson', 'lesson']


#######
# SUB #
"""
    Replaces one or many matches within a string
"""
print(re.sub("Expressions", "expressions", my_string))      # This is lesson number 7: Lesson called: Regular expressions
print(re.sub("lesson", "LESSON", my_string))                # This is LESSON number 7: Lesson called: Regular Expressions
print(re.sub("Regular Expressions", "RegEx", my_string))    # This is lesson number 7: Lesson called: RegEx
print(re.sub("[Ll]esson", "LESSON", my_string))             # This is LESSON number 7: LESSON called: Regular Expressions


txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. 
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

matches = re.sub('%', '', txt)
print(matches)
"""
    I am teacher and  I love teaching.
    There is nothing as rewarding as educating and empowering people.
    I found teaching more interesting than any other jobs.
    Does this motivate you to be a teacher?
"""


#########
# SPLIT #
"""
    Takes a string, splits it at the match points, returns a list
"""

######################################
## Splitting Text Using RegEx Split ##
######################################

my_string = "This is lesson number 7: Lesson called: Regular Expressions"
print(re.split(":", my_string))     # ['This is lesson number 7', ' Lesson called', ' Regular Expressions']

############################
## Writing RegEx Patterns ##
############################
"""
    To declare a string variable we use a single or double quote. To declare RegEx variable r''. 
    The following pattern only identifies apple with lowercase, to make it case insensitive either 
    we should rewrite our pattern or we should add a flag
"""
regex_pattern = r'apple'
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
matches = re.findall(regex_pattern, txt)
print(matches)  # ['apple']

# To make case insensitive adding flag '
matches = re.findall(regex_pattern, txt, re.I)
print(matches)  # ['Apple', 'apple']
# or we can use a set of characters method
regex_pattern = r'[Aa]pple'  # this mean the first letter could be Apple or apple
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'apple']


patternAll = r"a-zA-Z0-9" 
pattern = r"[Ll]esson" 
print(re.findall(pattern, my_string))   # ['lesson', 'Lesson']

pattern = r"[Ll]esson|Expressions" 
print(re.findall(pattern, my_string))   # ['lesson', 'Lesson', 'Expressions']

pattern = r"[0-9]" 
print(re.findall(pattern, my_string))   # ['7']

pattern = r"[aeiou]" 
print(re.findall(pattern, my_string))   # ['i', 'i', 'e', 'o', 'u', 'e', 'e', 'o', 'a', 'e', 'e', 'u', 'a', 'e', 'i', 'o']

# Match where the string contains digits (numbers from 0-9)
pattern = r"\d" 
print(re.findall(pattern, my_string))   # ['7']

# Match where the string does not contain digits
pattern = r"\D"
print(re.findall(pattern, my_string))   # ['T', 'h', 'i', 's', ' ', 'i', 's', ' ', 'l', 'e', 's', 's', 'o', 'n', ' ', 'n', 'u', 'm', 'b', 'e', 'r', ' ', ':', ' ', 'L', 'e', 's', 's', 'o', 'n', ' ', 'c', 'a', 'l', 'l', 'e', 'd', ':', ' ', 'R', 'e', 'g', 'u', 'l', 'a', 'r', ' ', 'E', 'x', 'p', 'r', 'e', 's', 's', 'i', 'o', 'n', 's']

# any character except new line character(\n)
# *: zero or more times
pattern = r"[l]."
pattern = r"[l].*"
print(re.findall(pattern, my_string))   # ['lesson number 7: Lesson called: Regular Expressions']

##################
# Square Bracket #
"""
    Use square bracket to include lower and upper case
"""
regex_pattern = r'[Aa]pple' # this square bracket mean either A or a
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'apple']

# Using the square bracket and or operator, we manage to extract Apple, apple, Banana and banana.
regex_pattern = r'[Aa]pple|[Bb]anana' # this square bracket means either A or a
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'banana', 'apple', 'banana']


################################
# Escape character(\) in RegEx #
regex_pattern = r'\d'  # d is a special character which means digits
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2', '0', '1', '9', '8', '2', '0', '2', '1'], this is not what we want


########################
# One or more times(+) #
regex_pattern = r'\d+'  # d is a special character which means digits, + mean one or more times
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019', '8', '2021'] - now, this is better!


#############
# Period(.) #
regex_pattern = r'[a].'  # this square bracket means a and . means any character except new line
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)  # ['an', 'an', 'an', 'a ', 'ar']

regex_pattern = r'[a].+'  # . any character, + any character one or more times 
matches = re.findall(regex_pattern, txt)
print(matches)  # ['and banana are fruits']


#########################
# Zero or more times(*) #
"""
    Zero or many times. The pattern could may not occur or it can occur many times.
"""
regex_pattern = r'[a].*'  # . any character, * any character zero or more times 
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)  # ['and banana are fruits']


#######################
# Zero or one time(?) #
"""
    Zero or one time. The pattern may not occur or it may occur once.
"""
txt = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail.'''
regex_pattern = r'[Ee]-?mail'  # ? means here that '-' is optional
matches = re.findall(regex_pattern, txt)
print(matches)  # ['e-mail', 'email', 'Email', 'E-mail']


#######################
# Quantifier in RegEx #
"""
    We can specify the length of the substring we are looking for in a text, using a curly bracket.
"""
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{4}'  # exactly four times
matches = re.findall(regex_pattern, txt)
print(matches)  # ['2019', '2021']

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{1,4}'   # 1 to 4
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019', '8', '2021']


##########
# Cart ^ #

# Starts with
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'^This'  # ^ means starts with
matches = re.findall(regex_pattern, txt)
print(matches)  # ['This']


# Negation
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'[^A-Za-z ]+'  # ^ in set character means negation, not A to Z, not a to z, no space
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6,', '2019', '8', '2021']

#############################
# Special Pattern for email #
email = "luisgonzalez@gmail.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
print(re.match(pattern, email))     # <re.Match object; span=(0, 22), match='luisgonzalez@gmail.com'>
print(re.search(pattern, email))    # <re.Match object; span=(0, 22), match='luisgonzalez@gmail.com'>
print(re.findall(pattern, email))   # ['luisgonzalez@gmail.com']

email = "luisgonzalez@gmail"
print(re.findall(pattern, email))   # []
