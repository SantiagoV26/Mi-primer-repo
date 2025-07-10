# ## File Handling ## #

import os
# File handling is the process of reading from and writing to files in a computer system.

# .Txt files are a common way to store data in a human-readable format.
txt_file = open("Intermedio./my_file.txt", "w+", encoding= "UTF-8")

txt_file.write("Mi nombre es Santiago\nMi apellido es Vargas\nMi edad es de 22 años\nEl lenguaje que mas me gusta es Python")
# The "r+" mode opens the file for reading and writing. If the file does not exist, it will be created.
#print(txt_file.read())
#print(txt_file.read(10)) # Read the first 10 characters of the file.
#print(txt_file.readline()) # Read the first line of the file.
#print(txt_file.readline()) # Read the second line of the file.
#print(txt_file.readlines()) # Read all lines of the file and return them as a list.

for line in txt_file.readlines():
    print(line) # Read all lines of the file and print them one by one.

txt_file.write("\nAunque también me gusta C#") # Write to the file.
print(txt_file.read()) # Read the file again.

txt_file.close() # Close the file.

#os.remove("Intermedio./my_file.txt") # Delete the file.


# .json file

import json

json_file = open("Intermedio./my_file.json", "w+", encoding= "UTF-8")

json_test = {
    "name": "Santiago", 
    "surname": "Vargas", 
    "age": 22, 
    "languajes":["Python", "C#", "Java", "JavaScript"],
    "Website": "https://www.santiagovargas.com"}

json.dump(json_test, json_file, indent=4) # Write to the file.

json_file.close() # Close the file.

with open("Intermedio./my_file.json") as json_test:
    for line in json_test.readlines():
        print(line)

json_dict = json.load(open("Intermedio./my_file.json", encoding="UTF-8")) # Read the file.
print(json_dict) # Print the file.
print(type(json_dict))
print(json_dict["name"]) # Print the name from the file.


# .csv file

import csv

csv_file = open("Intermedio./my_file.csv", "w+", encoding= "UTF-8")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "surname", "age", "languajes", "Website"]) # Write the header of the file.
csv_writer.writerow(["Santiago", "Vargas", 22, "Python", "https://www.santiagovargas.com"]) # Write the first row of the file.
csv_writer.writerow(["Luis David", "Osorio", 21, "Medicina", "https://www.luisosorio.com"]) 
# .xls file


csv_file.close() # Close the file.

with open("Intermedio./my_file.csv") as csv_test:
    for line in csv_test.readlines():
        print(line)


#import xlrd # Debe instalar el paquete xlrd

# .xml file

import xml 
