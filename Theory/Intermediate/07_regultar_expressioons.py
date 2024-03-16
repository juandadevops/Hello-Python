### REGULAR EXPRESSIONS ### 

# To use RegEx in python first we should import the RegEx module which is called re.
import re

# match

my_string = "Esta es la lección número 7: Lección llamada: Expresiones Regulares"
my_other_string = "Esta no es la lección número 6: Manejo de ficheros"

match = re.match("Esta es la lección", my_string, re.I)
print(match)
print(match.span())

start, end = match.span()
print(start, end)  # 0, 18
substring = my_string[start:end]
print(substring)    # match.match()


match = re.match("Esta es la lección", my_other_string)


# if not(match == None):  # Otra forma de comprobar el None
# if match != None)  # Otra forma de comprobar el None
# if match is not None:  # Otra forma de comprobar el None

print(re.match("Expresiones Regulares", my_string))


# search

search = re.search("lección", my_string, re.I)
print(search)
print(start, end)  # 11, 18
substring = my_string[start:end]
print(substring)    # search.match()


# findall

findall = re.findall("lección", my_string, re.I)
print(findall)

findall = re.findall('Lección|lección', my_string)
print(findall)  # ['Lección', 'lección']

findall = re.findall('[Ll]ección', my_string)
print(findall)  # ['Python', 'python']

# split

print(re.split(":", my_string))

# sub

print(re.sub("Expresiones", "expresiones", my_string))
print(re.sub("lección", "LECCIÓN", my_string))
print(re.sub("Expresiones Regulares", "RegEx", my_string))
print(re.sub("[Ll]ección", "LECCIÓN", my_string))


txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. 
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

matches = re.sub('%', '', txt)
print(matches)


# Patterns

patternAll = r"a-zA-Z0-9" 
pattern = r"[Ll]ección" 
print(re.findall(pattern, my_string))

pattern = r"[Ll]ección|Expresiones" 
print(re.findall(pattern, my_string))

pattern = r"[0-9]" 
print(re.findall(pattern, my_string))

pattern = r"[aeiou]" 
print(re.findall(pattern, my_string))


pattern = r"\d" 
print(re.findall(pattern, my_string))

pattern = r"\D"
print(re.findall(pattern, my_string))

pattern = r"[l]."
pattern = r"[l].*"
print(re.findall(pattern, my_string))


email = "luisgonzalez@gmail.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
print(re.match(pattern, email))
print(re.search(pattern, email))
print(re.findall(pattern, email))

email = "luisgonzalez@gmail"
print(re.findall(pattern, email))
