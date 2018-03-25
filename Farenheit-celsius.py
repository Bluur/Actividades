
operacion_elegida = input('Hola, ¿que deseas pasar, celsius o farenheit?: ')
f_degrees = 0
c_degrees = 0


if operacion_elegida == 'Celsius':
    c_degrees = int(input('Dime la cantidad de grados Celsius que deseas pasar: '))
    f_degrees = (c_degrees * 1.8) + 32
    print('{}ºCelsius son {}ºFarenheit'.format(c_degrees, f_degrees))

elif operacion_elegida == 'Farenheit':
    f_degrees = int(input('Dime la cantidad de grados Farenheit que deseas pasar: '))
    c_degrees = (f_degrees - 32) / 1.8
    print('{}ºfarenheit son {}ºcelsius'.format(f_degrees, c_degrees))
