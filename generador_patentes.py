from random import randint

nombre = input('Ingrese nombre: ')
apellido = input('Ingrese apellido: ')
nacimiento = input('Ingrese año de nacimiento: ')

#Crear formato de patente
nombre_mod = nombre.strip().upper()[0:2]
apellido_mod = apellido.strip().upper()[0:2]
nacimiento_mod = nacimiento.strip()[2:]
num_aleatorio = randint(1000, 9999)

print(f'El usuaario {nombre} {apellido} tendra una placa patente nueva')
print(f'datos: {nombre_mod}{apellido_mod}{nacimiento_mod}{num_aleatorio}')