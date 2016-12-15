# -*-coding:utf-8-*-
''' 
3. (Samuel)Crear un programa que lea por teclado una cadena y un carácter, 
y reemplace todos los espacios por el carácter. Ej: mi archivo de texto.txt 
y _ debería devolver mi_archivo_de_texto.txt
'''

cadena = raw_input("introduce una cadena")
caracter = raw_input("Introduce un caracter")[0]

cadena = cadena.replace(" ", caracter)

print cadena