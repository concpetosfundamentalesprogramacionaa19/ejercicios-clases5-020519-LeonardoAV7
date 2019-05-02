"""
	file: run2.py
	autor: @LeonardoAV7
"""

from misvariables import *

# uso condicional simple 

nota = input("Ingresar la nota 1: ")
nota2 = input("Ingresar la nota 2: ")

nota = int(nota)
nota2 = int(nota2)

if nota >= 18:
	print("%s - %d " % (mensaje, nota))
else:
	print("%s - %d " % (mensaje2, nota))

if nota2 >= 18:
	print("%s - %d " % (mensaje, nota2))
else:
	print("%s - %d " % (mensaje2, nota2))