print('*** Promedio de calificaciones ***')
qty_mark = int(input('Proporciona la cantidad de calificaciones a evaluar: '))
marks = []

for i in range(qty_mark):
    mark = float(input(f'Ingresa la calificación[{i + 1}]: ')) 
    marks.append(mark)
    
print(f'Las calificaciones proporcionadas son : {marks}')

average  = sum(marks)
# for mark in marks:
#     average  += mark
average /= len(marks)
print(f'Promedio de la calificaciones: {average}')