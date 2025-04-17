name = input('Ingrese nombre: ')
surname= input('Ingrese apellidos: ')
company_name = input('Ingrese nombre de la compañia: ')
extension = '.com'

name_mod = name.strip().lower().replace(' ', '.') + '.' +surname.strip().lower().replace(' ', '.')

print(f'\nEl email generado para {name} {surname} : ')
print(f'{name_mod}@{company_name.lower()}{extension}')