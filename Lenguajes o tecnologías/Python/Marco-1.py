import time
import random

# ✅ Una calculadora básica (suma, resta, multiplicación, división) 

def inputs(operation):
    try: # manejo de errore o exepciones
        number1 = float(input('ingresa el primer número: '))
        number2 = float(input('ingresa el segundo número: '))
        
        # condicion para que no dvividan por cero
        if operation == '/' and number2 == 0:
            print(" No se puede dividir entre 0.")
        else:
            operations(number1, operation, number2)

    except ValueError:
        print("Por favor, ingresa solo números.")

def operations(number1, operation, number2):
    match operation:  # match es una condicional mas legible que if
        case '+':
            result = number1 + number2
        case '-':
            result = number1 - number2
        case '*':
            result = number1 * number2
        case '/':
            result = number1 / number2
        case _:
            print("Operación no reconocida.")
            return

    print(f' Resultado: {number1} {operation} {number2} = {result}')

def logic():
    mensaje = '''Bienvenido a mi calculadora básica:
1. Sumar +
2. Restar -
3. Multiplicar *
4. Dividir 
5. Salir 
    '''
    # bucle que sta en verdadero esperando a que un break lo pare
    while True:
        print()
        time.sleep(1)
        print(mensaje)
        opcion = input('Selecciona una opción (1-5): ').strip() # el metodo .strip() para quitar espaciios

        match opcion: # otra condicional similar a if 
            case '1':
                inputs('+')
            case '2':
                inputs('-')
            case '3':
                inputs('*')
            case '4':
                inputs('/')
            case '5':
                print('Gracias por usar la calculadora Saliendo...')
                break
            case _:
                print('Opción inválida. Intenta de nuevo.')

 # llamo la funcion para que comienze a correr el programa


# 🔐 Un validador de contraseñas (ej: que tenga mínimo 8 caracteres, etc.)



def captcha():
    print('verificador de contraseñas ')
    while True:
        
        pasword = input('>> ')

        if len(pasword) >= 8 and '.' in pasword or ',' in pasword:
            print(f'contraseña medio segura {pasword} \n recomiendo mas caracteres')
            break
        elif len(pasword) >= 15 and '.' in pasword or ',' in pasword:
            print(f'contraseña Segura {pasword}')
            break
        else:
            print('puedes aserla mas segura ')


#captcha()

# 🎉 Un generador de frases aleatorias (motivadoras, chistosas o educativas)

def mensages_aleatorios():


    lista_de_mensages = [
        'la vida es dura pero mas dura mi verdura',
        'si la tiene depilada la tiene ocupada ',
        'me gustan los aviones me gustas tu me gusta tocar me gustas tu',
        'si se juntan los mares con lo rios porque no se juntan tus labios con los mios',
        ' cuando queieres algo trabajas para conseguirlo'
    ]

    aliatorio = random.randint(0, len(lista_de_mensages))

    
    print(lista_de_mensages[aliatorio])


# mensages_aleatorios()





def main():
    menu = '''
Bienvenido al menu de usuario que desea aser
1. calaculadora
2. validador de contraseña
3. mensage aleatorio
'''
    print(menu)
    opt = input('>> ')
    match opt:
        case '1':
            logic()
        case '2':
            captcha()
        case '3':
            mensages_aleatorios()


main()
