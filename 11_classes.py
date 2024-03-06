### CLASSES ###

class MyEmptyPerson:
    pass

print(MyEmptyPerson())
print(MyEmptyPerson)


class Person:
    def __init__(self, name, surname, alias = "Sin alias"):
        self.full_name = f"{name} {surname}"    # Propiedad pública
        self.__name = name                      # Propiedad privada
        self.__surname = surname                # Propiedad privada
        self.age = 18                           # Propiedad pública
        
    def get_name(self):
        return self.__name
        
    def get_surname(self):
        return self.__surname
    
    def walk(self):
        print(f"{self.full_name} is walking")
    
    
person = Person("Luis", "Gil")
print(person.age)
print(person.full_name)


person.walk()


# Inheritance
class Painter(Person):
    def walk(self):
        print(f"The painter {self.full_name} is walking")



painter = Painter("Mario", "García")
print(painter.full_name)
painter.walk()

painter.full_name = "Mario García (The best)"
print(painter.full_name)

# No existe tipado ni consistencia  
painter.full_name = 756
print(painter.full_name)