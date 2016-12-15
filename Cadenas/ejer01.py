# -*-coding:utf-8-*-
''' 
1. (Victor)Crear un programa que lea por teclado una cadena, y muestre la siguiente información:
Imprima los dos primeros caracteres.
Imprima los tres últimos caracteres.
Imprima dicha cadena cada dos caracteres. Ej.: recta debería imprimir rca
Dicha cadena en sentido inverso. Ej.: hola mundo! debe imprimir !odnum aloh
Imprima la cadena en un sentido y en sentido inverso. Ej: reflejo imprime reflejoojelfer. 
'''

cadena = raw_input("Introduce una cadena:")

print cadena[0:2]

print cadena[len(cadena)-3:len(cadena)]

cada2letras = ""
for i in range(len(cadena)):
    if i % 2 == 0:
        cada2letras = cada2letras + cadena[i]
         
print cada2letras

print cadena[::-1]

normaleinverso = cadena + cadena[::-1]
print normaleinverso


