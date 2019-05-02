"""
	file: run3.py
	autor: @LeonardoAV7

	deseamos obtener el costo de una carrera universitaria. 
	el valor promedio de cada ciclo es de mil docientos 
	dolares, el valor promedio del seguro educativo es de
	100 dolares si la edad del estudiante es menor o igual a 20 
	caso contrario sera de 150 dolares. si el estudiante tiene
	una modalidad a distancia el numero de ciclos a segir es de 10
	caso contrario debera seguir 8 ciclos. Obtener la proyeccion del 
	costo de la carrera de un estudiante
"""
# solicitamos la modalidad y edad del estudiante
modalidad = input("Ingresar la modalidad del estudiante: ")
edad = input("Ingresar la edad del estudiante: ")
# transformamos en entero la variable edad
edad = int(edad)

if modalidad == "Distancia":   # si la modalidad es a distancia
	pago_modalidad = 10 * 1200 # se multiplica el costo de cada ciclo por los 10 ciclos
	if edad <= 20:
		pago_seguro = 10 * 100 # si la edad es menor de 20, el seguro cuesta $100 por ciclo
	else:
		pago_seguro = 10 * 150 # si la edad es menor de 20, el seguro cuesta $150 por ciclo
else:
	pago_modalidad = 8 * 1200 # si la modalidad no es a distancia sino presencial
	                          # se multiplica el costo de cada ciclo por los 8 ciclos 
	if edad <= 20:
		pago_seguro = 8 * 100 # si la edad es menor de 20, el seguro cuesta $100 por ciclo
	else:
		pago_seguro = 8 * 150 # si la edad es menor de 20, el seguro cuesta $150 por ciclo

# el valor total a pagar es la suma del costo de cada ciclo mas el seguro total
total = pago_modalidad + pago_seguro

print ("El valor total a pagar es %.2f" % total)
