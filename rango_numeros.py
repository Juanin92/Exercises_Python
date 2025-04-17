MIN_VALUE = 0
MAX_VALUE = 5

value_first = int(input('Ingrese primer número: '))
value_last = int(input('Ingrese último número: '))

condition_first = value_first <= MAX_VALUE and value_first >= MIN_VALUE
condition_last = value_last <= MAX_VALUE and value_last >= MIN_VALUE

print(f'El primer valor esta dentro del rango: {value_first} - {condition_first}')
print(f'El último valor esta dentro del rango: {value_last} - {condition_last}')