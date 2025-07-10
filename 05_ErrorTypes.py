# ## Error Types ## #

# SyntaxError: Occurs when the syntax of the code is incorrect.

#print "Hola mundo" # Error
print("Hola mundo")

# NameError: Occurs when a variable is not defined or is not in the current scope.
language = "Spanish" # Comentar para error
print(language) # Error

# IndexError: Occurs when trying to access an index that does not exist in a list or string.
my_list = ["Python", "Java", "C++", "JavaScript"]
#print(my_list[4]) # Error
print(my_list[2]) # No error

# ModuleNotFoundError: Occurs when trying to import a module that does not exist.
#import maths # Descpmentar para error
import math

# AttributeError: Occurs when trying to access an attribute or method that does not exist in an object.
#print(math.Pi) # Error
print(math.pi) # No error

# KeyError: Occurs when trying to access a key that does not exist in a dictionary.
my_dict = {"Nombre": "Santiago", "Apellido": "Vargas", "Edad": 22, 1:"Python"}
print(my_dict["Edad"])
#print(my_dict["Apelido"]) # Error
#print(my_list["Nombre"]) # Error


# TypeError: Occurs when an operation or function is applied to an object of an inappropriate type.
#print(my_list["Nombre"]) # Error
print(my_list[0])


# ImportError: Occurs when there is an error importing a module.
#from math import PI # Error
from math import pi # No error
print(pi) 


# ValueError: Occurs when a function receives an argument of the right type but an inappropriate value.
my_int = int("10")
#my_int = int("10 Años") Error
print(type(my_int)) # Error
print(type(my_int + 5)) # str


# ZeroDivisionError: Occurs when trying to divide by zero.
print(4/2) # No error
#print(4/0) # Error