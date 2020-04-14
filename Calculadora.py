
sw=True
def operacion_suma(a,b):

    print('\t                         + _____')

    print('\t     EL RESULTADO ES:        ', a+b)

def operacion_resta(a,b):
    print('\t                          - _____')
    print('\t     EL RESULTADO ES:        ', a - b)

def operacion_multipliacacion(a,b):
    print('\t                         * _____')
    print('\t     EL RESULTADO ES:        ', a * b)

def operacion_division(a,b):

    if(b != 0):
     print('\t                             _____')
     print('\t      EL RESULTADO ES:      ', a / b)
    else:
     print('\t <<<<<<<<< OPERACION INDETERMINADA >>>>>>>>>>')

def salir_calcu():
    print('\t  <<<<<<<<<<  FIN DEL PROGRAMA  >>>>>>>>>>>>>>>>')
    global sw
    sw = False
def opcion_no_disponible():
    print('             <<<<<  OPCIÓN NO DISPONIBLE  >>>>>')

menuCalcu = '''
        <<<<<<<<<<<<<<<<<< >>>>>>>>>>>>>>>>>>>>>>
        <<<<<<<<<<<<< CALCULADORA >>>>>>>>>>>>>>>
        <<<<<<<<<<<<<<<<<<< >>>>>>>>>>>>>>>>>>>>>>
                              1.- SUMA
                              2.- RESTA
                              3.- MULTIPLICACIÓN
                              4.- DIVISIÓN
                              5.- SALIR
        <<<<<<<<<<<<<<<<<<< >>>>>>>>>>>>>>>>>>>>>>           
'''

while sw :
    print(menuCalcu)

    opcion= int(input('        <<<<<< INGRESE LA OPCIÓN : >>>>> '))
    if opcion in range(1,5):
        num1 = int(input('\t    INGRESE PRIMER  NÚMERO :  '))
        num2 = int(input('\t    INGRESE SEGUNDO NÚMERO :  '))
        if opcion is 1:
            operacion_suma(num1,num2)
        elif opcion is 2:
            operacion_resta(num1,num2)
        elif opcion is 3:
            operacion_multipliacacion(num1,num2)
        elif opcion is 4:
          operacion_division(num1,num2)
    else:
        if opcion is 5:
         salir_calcu()
        else:
         opcion_no_disponible()
