#Special thanks to Nate Gentile for making me use my brain.

numero_1 = 0
numero_2 = 0
numero_3 = 0

operacion_elegida = input('Hola, Bienvenido a la calculadora interactiva de Nate Academy, ¿Que operación desea hacer?( Multiplicación / Dividisión / Suma / Resta):')

if operacion_elegida == 'Multiplicacion':
    numero_1 = int(input('Dime el primer numero que desees multiplicar: '))
    numero_2 = int(input('Dime el segundo numero que desees multiplicar: '))
    numero_3 = numero_2 * numero_1
    print('La multiplicacion de {} y {} da {}'.format(numero_1, numero_2, numero_3))
elif operacion_elegida == 'Division':
    numero_1 = int(input('Dime el primer numero que desees dividir: '))
    numero_2 = int(input('Dime el segundo numero que desees dividir: '))
    numero_3 = numero_1 / numero_2
    print('La division de {} entre {} da {}'.format(numero_1, numero_2, numero_3))
elif operacion_elegida == 'Suma':
    numero_1 = int(input('Dime el primer numero que desees sumar: '))
    numero_2 = int(input('Dime el segundo numero que desees sumar: '))
    numero_3 = numero_1 + numero_2
    print('La suma de {} + {} es {}'.format(numero_1, numero_2, numero_3))
elif operacion_elegida == 'Resta':
    numero_1 = int(input('Dime el primer numero que desees restar: '))
    numero_2 = int(input('Dime el segundo numero que desees restar: '))
    numero_3 = numero_1 - numero_2
    print('La resta de {} - {} da {}'.format(numero_1, numero_2, numero_3))
else:
    input('Esa opción no me vale, reinicia el programa y vuelve a intentarlo.')
