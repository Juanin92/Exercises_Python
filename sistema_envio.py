NATIONAL_COST = 10
INTERNATIONAL_COST = 20

print('*** Sistema de envio de encomienda ***')
confirm = int(input('Seleccione el destino [1- nacional / 2- internacional]: '))
weight = int(input('Ingrese el peso: '))

total = None
if confirm == 1:
    total = weight * NATIONAL_COST
elif confirm == 2:
    total = weight * INTERNATIONAL_COST
else:
    print('Destino no valido!!!')

if total is not None:    
    print(f'El total de su envio es ${total}')    