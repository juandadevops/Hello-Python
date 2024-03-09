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