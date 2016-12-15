# -*-coding:utf-8-*-
'''
4. (Ángel)Crear un programa que lea por teclado una cadena y un carácter,
 y reemplace todos los dígitos en la cadena por el carácter. 
 Ej: su clave es: 1540 y X debería devolver su clave es: XXXX
'''

cadena = raw_input("Introduce una cadena:")
caracter2 = raw_input("Introduce un caracter")[0]

for i in range(len(cadena)):
    caracter= cadena[i]
    cadena.replace(caracter, caracter2)
    
print cadena
