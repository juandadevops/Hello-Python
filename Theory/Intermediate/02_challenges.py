### CHALLENGES ###

"""
    TÍTULO: EL FAMOSO "FIZZ BUZZ"
  Escribe un programa que muestre por consola (con un print) los
  números de 1 a 100 (ambos incluidos y con un salto de línea entre
  cada impresión), sustituyendo los siguientes:
  - Múltiplos de 3 por la palabra "fizz".
  - Múltiplos de 5 por la palabra "buzz".
  - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""
def fizz_buzz():
    for i in range(1,101):
        divisibleByThree = i % 3 == 0
        divisibleByFive = i % 5 == 0
        
        if divisibleByThree and divisibleByFive:
            print("fizzbuzz")
        elif divisibleByThree:
            print("fizz")
        elif divisibleByFive:
            print("buzz") 
        else:
            print(i)          
            
fizz_buzz()



"""
    TÍTULO: ¿ES UN ANAGRAMA?
  Escribe una función que reciba dos palabras (String) y retorne
  verdadero o falso (Bool) según sean o no anagramas.
  - Un Anagrama consiste en formar una palabra reordenando TODAS
    las letras de otra palabra inicial.
  - NO hace falta comprobar que ambas palabras existan.
  - Dos palabras exactamente iguales no son anagrama.
"""
def isAnagram(palabra1, palabra2):
    
    a,b = 'áéíóúü','aeiouu'
    trans = str.maketrans(a,b)

    if(type(palabra1) != str or type(palabra2) != str):
        #print("ERROR: Los dos parámetros deben ser strings")
        return False
    
    palabra1 = palabra1.lower().translate(trans)
    palabra2 = palabra2.lower().translate(trans)
    
    if(palabra1 == palabra2):
        #print("Dos palabras exactamente iguales no son anagrama")
        return False
    elif len(palabra1) != len(palabra2):
        #print("Palabras con distinto número de caracteres no son anagrama")
        return False
    
    return sorted(palabra1) == sorted(palabra2)

        
        
print(isAnagram("cara", "Arca"))       # True
print(isAnagram("cara", "Cara"))       # False
print(isAnagram("castor", "castro"))   # True
print(isAnagram("Blanco", "Balcón"))   # True
print(isAnagram("feo", "fea"))         # False
print(isAnagram(2, "fea"))             # False




""" 
    TÍTULO: LA SUCESIÓN DE FIBONACCI
  Escribe un programa que imprima los 50 primeros números de la sucesión
  de Fibonacci empezando en 0.
  - La serie Fibonacci se compone por una sucesión de números en
    la que el siguiente siempre es la suma de los dos anteriores.
    0, 1, 1, 2, 3, 5, 8, 13...
"""
def fibonacci(number = 50):
    if type(number) != int:
        print("ERROR: ")
    elif number < 0:
        print("ERROR: ")
    else:
        
        preValue = 0
        next = 1
        
        for i in range (number):
            
            print(preValue)
            
            fib = preValue + next
            preValue = next
            next = fib
    
fibonacci()



"""
  Escribe un programa que se encargue de comprobar si un número es o no primo.
  Hecho esto, imprime los números primos entre 1 y 100.
"""
def is_prime(number):
    if type(number) != int or number < 0:
        # print("ERROR: The number passed as parameter must be a positive integer.")
        return False
    elif number == 0:
        # print("Zero is not prime because it cannot be divided by itself and it cannot be written as a product of primes either. Zero is a number apart from all")
        return False
    elif number == 1:
        # print("The number 1 is not prime because it has only one divisor")
        return False
    else:
        for n in range(2, number):
            if number % n == 0: 
                # print(number, "is NOT prime,", n, "is divisor") 
                return False 
            
        print(number, "is prime") 
        #return True
    
# is_prime(13) # It's prime
# is_prime(165) # 165 is NOT prime, 3 is divisor
# is_prime(887) # It's prime
# is_prime(1542) # 1542 is NOT prime, 2 is divisor
# is_prime(654977) # 654977 is NOT prime, 103 is divisor


for i in range(0,101):
    esPrimo = is_prime(i)
    if(esPrimo == True):
        print(esPrimo)
        
        
"""
  Crea una única función (importante que sólo sea una) que sea capaz
  de calcular y retornar el área de un polígono.
  - La función recibirá por parámetro sólo UN polígono a la vez.
  - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
  - Imprime el cálculo del área de un polígono de cada tipo.
"""
def area_poligono():
    return 0
    
    
    

"""
  Crea un programa que se encargue de calcular el aspect ratio de una
  imagen a partir de una url.
  - Url de ejemplo:
    https://raw.githubusercontent.com/mouredevmouredev/master/mouredev_github_profile.png
  - Por ratio hacemos referencia por ejemplo a los "16:9" de una
    imagen de 1920*1080px.
"""
def aspect_ratio():
    return 0


"""
  Crea un programa que invierta el orden de una cadena de texto
  sin usar funciones propias del lenguaje que lo hagan de forma automática.
  - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""
def reverse(texto):
    if type(texto) != str:
        return "ERROR:"

    listAux = []

    for c in texto:
        listAux.insert(0,c)
        
    reversed_text = ''.join(listAux)
    return reversed_text
    
    
print(reverse("Hola Mundo"))

def reverse2(texto):
    
    text_len = len(texto)
    reversed_text = ""
    
    for i in range (0, text_len):
        reversed_text += texto[text_len - i -1]
    
    return reversed_text
    
    
print(reverse2("Hola Mundo"))



