USERNAME_VALID = 'admin'
PASSWORD_VALID = '1234'

print('*** Sistema de Autenticación ***')
username = input('Nombre de usuario: ')
password = input('Contraseña: ')

is_authenticated = username.strip().lower() == USERNAME_VALID and password.strip().lower() == PASSWORD_VALID
print(f'Datos correctos? - {is_authenticated}')