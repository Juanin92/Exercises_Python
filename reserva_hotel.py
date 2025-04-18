SIMPLE_ROOM = 150.15
OCEAN_ROOM = 190.50

print('*** SISTEMA DE RESERVACION')
name_customer = input('Ingrese nombre del cliente: ')
days_stay = int(input('Ingrese los días de estadia: '))
viewOcean_room_txt = input('Desea tener vista al mar? (SI/NO): ')
viewOcean_room = viewOcean_room_txt.strip().lower() == 'si' 

if viewOcean_room:
    total = days_stay * OCEAN_ROOM
else:
    total = days_stay * SIMPLE_ROOM

print('*** Detalle de reservación del cliente ***')
print(f'Cliente: {name_customer}')
print(f'Días de estadia: {days_stay}')
print(f'Costo total: {total}')
print(f'Habitacion con vista al mar: {"Si" if viewOcean_room else "No"}')