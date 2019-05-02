"""
	file: run3.py
	autor: @LeonardoAV7

	nota mayor o igual a 18: sobresaliente

	nota mayor o igual a 16 y menor a 18: muy buena

	nota mayor o igual a 13 y menos a 16: buena

	nota menor a 13: insuficiente
"""

from misvariables import *

# uso condicional simple 

nota = input("Ingresar la nota 1: ")
nota = int(nota)

if nota >=18:
	print("%s - %d "% ("Sobresaliente", nota))
else:
	if (nota < 18) and (nota >= 16):
		print("%s - %d "% ("Muy Buena", nota))
	else:
		if (nota < 16) and (nota >= 13):
			print("%s - %d " % ("Buena", nota))
		else:
			print("%s - %d " % ("Insuficiente", nota))

