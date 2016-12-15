# -*-coding:utf-8-*-
'''
2. (Josué)Crear un programa que lea por teclado una cadena y un carácter, 
e inserte el carácter entre cada letra de la cadena. Ej: separar y , 
debería devolver s,e,p,a,r,a,r
'''

cadena = raw_input("Introduce una cadena")
caractersolicitado = raw_input("Introduce un caracter")[0]

sbCadena = ""

for i in range(len(cadena)):
    caracter= cadena[i]
    sbCadena = sbCadena + caracter
    if i != len(cadena)-1:
        sbCadena = sbCadena + caractersolicitado

print sbCadena