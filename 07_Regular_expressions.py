# ## Regular Expressions # ##

# RE


import re
# Regular expressions are a powerful tool for matching patterns in strings.

my_string = "Esta es la lección 7 de Python Intermedio: Lección llamada expresiones regulares"
my_other_string = "Esta no es la lección numero 6: Lección llamada manejo de errores"

match = re.match("Esta es la lección", my_string)
print(match) # Match the beginning of the string.

print(match.span()) # Return the start and end of the match.
start, end = match.span()
print(my_string[start:end]) # Return the match.

#print(re.match("Esta es la lección", my_string, re.I)) # Match the beginning of the string.
match = re.match("Esta es la lección", my_other_string) # Match the beginning of the string.
if not(match == None):
    print(match)
    start, end = match.span()
    print(my_other_string[start:end]) # Return the match.


#print(re.match("expresiones regulares", my_string))



# Search

search = re.search("lección", my_string) # Search the string.
print(search) # Return the match.
start, end = search.span() # Return the start and end of the match.
print(my_string[start:end]) # Return the match.


# findall

findall = re.findall("lección", my_string, flags=re.IGNORECASE) # Find all matches in the string.
findall_minusculas = [item.lower() for item in findall] # Convert all matches to lowercase.
print(findall_minusculas) # Return the matches.


# Split

print(re.split(":", my_string)) # Split the string by spaces.


# Sub

sub2 = re.sub("[L|l]ección", "LECCIÓN", my_string)
sub = re.sub("expresiones regulares", "ReEx", my_string) # Replace the word "Expresiones" with "EXPRESIONES" in the string.
print(sub) # Return the string.
print(sub2) # Return the string.


# Patterns
# https://regex101.com Pagina para probar expresiones regulares.
# https://www.regular-expressions.info/ Pagina para aprender expresiones regulares.

pattern = r"[L|l]ección"
print(re.findall(pattern, my_string, re.I)) # Find all matches in the string.
print(re.search(pattern, my_string, re.I))

pattern = r"[L|l]ección|Expresiones"
print(re.findall(pattern, my_string, re.I)) # Find all matches in the string.
print(re.search(pattern, my_string, re.I))

pattern = r"[0-9]"
print(re.findall(pattern, my_string, re.I)) # Find all matches in the string.
print(re.search(pattern, my_string, re.I))

pattern = r"\d" # Find all digit characters in the string.
print(re.findall(pattern, my_string, re.I))

pattern = r"\D" # Find all non-digit characters in the string.
print(re.findall(pattern, my_string, re.I))

pattern = r"[l]." # Find all characters that are followed by a letter "l".
print(re.findall(pattern, my_string, re.I)) 

# Email validation regular expression

def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    match = re.match(pattern, email) # Match the pattern.
    if match:  
        print("El email "+ email + " es válido")
        return True
    else:
        print("El email " + email + " no es válido")
        return False
    
print(is_valid_email("vargass881@gmail.com")) # True
print(is_valid_email("vargass881@gmailcom")) # False

email = "vargass@gmail.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
print(re.findall(pattern, email)) # True
print(re.search(pattern, email))
print(re.match(pattern, email))

email = "vargass@gmail.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-z-.]+$"
print(re.findall(pattern, email)) # True