def divisible(numero):
	if numero % 7 == 0 and numero % 5 == 0:
		return "Es divisible entre 5 y 7"
		elif numero % 7 == 0:
			return "Es divisible por 7"
			else:
				print('No es divisible') numero_dividido= int(input('Escribe un numero papu: '))
divisibilidad=divisible(numero_dividido)
print(divisibilidad)