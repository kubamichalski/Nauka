# -*- coding: utf8 -*-

name = input("Imię: ")
surname = input("Nazwisko: ")
number = input("Numer telefonu: ")

print("Czy imię składa się tylko z liter?", name.isalpha())
print("Czy nazwisko składa się tylko z liter?", surname.isalpha())
print("Czy numer telefonu składa się z cyfr", number.isdigit())

print(name, surname)
name = name.capitalize()
surname = surname.capitalize()
print(name, surname)

print(number)
number = number.replace(" ", "").replace("-","")
print(number)

print("Imię kobiece:", name.endswith("a"))

personal = name + " " + surname + " " + number
print(personal)
print(len(personal))

letters = len(personal) - personal.count(" ") - 9
print(letters)
print (len(name + surname)) #sprawdzenie
