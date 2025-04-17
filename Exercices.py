cadena1 = 'Hola'
cadena2 = 'Mundo'
concanetacion = cadena1 + ' ' + cadena2

concanetacion_join = ' '.join([cadena1, cadena2])
print(concanetacion)
print(concanetacion_join)

nombre = 'Juan'
apellido = 'Perez'
edad = 25

oracion = f'Hola, mi nombre es {nombre} {apellido} y tengo {edad} años.'
oracion_formato = 'Hola, mi nombre es {} {} y tengo {} años.'.format(nombre, apellido, edad)
print(oracion_formato)
print(oracion)

#Largo de cada cadena
print('Largo de cada cadena')
print(cadena1 + ':', len(cadena1), 'letras')

#Obtener las letras de cierta posición de la cadena
nombre_completo = nombre + ' ' + apellido
posicion_cadena = nombre_completo[0:3]
print('Letras de la cadena:', posicion_cadena)

#Reemplazar cadenas
cadena = 'Hola, Mundo'
cadena_reemplazo = cadena.replace('Mundo', 'Python')
print('Cadena original:', cadena)

#Separa cadena
lista_nombre = nombre_completo.split(' ')
print('Cadena separada:', lista_nombre)

#Multiplicación de cadenas
print('Multiplicación de cadenas')
texto = 'Hola'
cantidad = 3
resultado = texto * cantidad
print('Resultado:', resultado)

#Desafío - Generador de email
nombre = 'Juan Acosta Soto'
empresa = 'Google'
dominio = '.com'
resultado = nombre.lower().replace(' ', '.') + '@' + empresa.lower() + '.' + dominio
print('Email:', resultado)

#Convertir cadena a número
num_cadena = '1234'
num = int(num_cadena)
print(f'Cadena original: {num_cadena}')
print(f'Cadena convertida a número: {num}')

#Convertir número a cadena
num = 1234
num_cadena = str(num)
print(f'Número original: {num}')
print(f'Número convertido a cadena: {num_cadena}')

#Convertir de cadena a float
num_cadena = '1234.56'
num_float = float(num_cadena)
print(f'Cadena original: {num_cadena}')
print(f'Cadena convertida a float: {num_float}')

#Convertir a boolean
num_cadena = 0
booleano = bool(num_cadena)
print(f'Valor de boolean de 0: {booleano}')

#Entrada de datos por consola
nombre_input =  input('Ingrese nombre: ')
print(f'Nombre ingresado: {nombre_input}')