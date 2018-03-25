number_to_guess = int(input('Elige un numero que tu compañero tenga que adivinar: '))

user_number = int(input('Adivina el numero del compañero: '))


while user_number != number_to_guess:
    print('Intentalo de nuevo')
    user_number = int(input('Adivina el numero del compañero: '))
if user_number == number_to_guess:
    print('Has adivinado el numero')

