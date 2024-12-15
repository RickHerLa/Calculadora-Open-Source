
from suma import suma 
from resta import resta
from multiplicacion import multiplicar
from dividir import dividir
from suma_avanzada import avanzada
import time

def menu():
    print('Bienvenido a la programación avanzada')
    print('-------------------------------------')
    print('Calculadora super power!!! si señor!!!')
    time.sleep(1.5)
    print('-------------------------------------')
    print('Qué quiere hacer:')
    print('Marca el número correspondiente.')
    time.sleep(2.5)
    print('-------------------------------------')
    print('1.- Si quieres SUMAR.')
    print('2.- Si quieres RESTA.')
    print('3.- Si quieres MULTIPLICAR.')
    print('4.- Si quieres DIVISION.')
    print('5.- Si quieres SUMA AVANZADA (suma N cantidad de números).')
    print('6.- Cerrar')
    print('-------------------------------------')
    time.sleep(1)

def proceso(num):
    print('-------------------------------------')

    if num == 1:
        print ('Seleccionaste 1, SUMA!!!')
        print ('-------------------------')
        time.sleep(1)
        a = float(input('Dame el primer número para sumar: '))
        b = float(input('Dame el segundo número para sumar: '))
        print ('-------------------------')
        print('el resultado es: ', (suma(a,b)))
        print ('-------------------------')
        time.sleep(1.5)
        print('Regresamos al menú inicial')
        print ('-------------------------')
        print ('-------------------------')
        time.sleep(1.5)
        return True
    
    elif num == 2:
        print ('Seleccionaste 2, RESTA!!!')
        print ('-------------------------')
        time.sleep(1)
        a = float(input('Dame el primer número al que le restaremos: ')) 
        b = float(input('Dame el segundo número que restará: '))
        print ('-------------------------')
        print('el resultado es: ', (resta(a,b)))
        time.sleep(1.5)
        print('Regresamos al menú inicial')
        print ('-------------------------')
        print ('-------------------------')
        time.sleep(1.5)
        return True

    elif num == 3:
        print ('Seleccionaste 3, MULTIPLICAR!!!')
        print ('-------------------------')
        time.sleep(1)
        a = float(input('Dame el primer número a multiplicar: ')) 
        b = float(input('Dame el segundo número a multiplicar: '))
        print ('-------------------------')
        print('el resultado es: ', (multiplicar(a,b)))
        time.sleep(1.5)
        print('Regresamos al menú inicial')
        print ('-------------------------')
        print ('-------------------------')
        time.sleep(1.5)
        return True

    elif num == 4:
        print ('Seleccionaste 4, DIVISION!!!')
        time.sleep(0.5)
        print ('-------------------------')
        a = float(input('Dame el primer número el que se dividirá: ')) 
        b = float(input('Dame el segundo número por el cual se dividirá: '))
        print ('-------------------------')
        print('el resultado es: ', (dividir(a,b)))
        time.sleep(1.5)
        print('Regresamos al menú inicial')
        print ('-------------------------')
        print ('-------------------------')
        time.sleep(1.5)
        return True

    elif num == 5:
        numeros = list(map(float, input("Introduce los números separados por espacio: ").split()))
        print(f"Resultado: {avanzada(numeros)}")
        return True

    elif num == 6:
        print ('vamo a cerrar, adios!!!')
        time.sleep(2.0)
        return False

    
    else:
        print('ERROR,---------------------------------')
        time.sleep(0.5)
        print('NOOOOO!!! ')
        time.sleep(0.5)
        print('Solo colocar del 1 al 6.')
        time.sleep(0.5)        
        print('---------------------------------')
        return True
     

def main():
    while True:
        menu()
        num = int(input("Selecciona una opción: "))
        if not proceso(num):
            break
main()
