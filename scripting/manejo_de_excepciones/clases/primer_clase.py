def eneavo(numero):
    try:
        print(1/numero)
    except ZeroDivisionError: # El tipo de error se puede poner o no, si no se pone el mensaje salta ante cualquier
                                # error , y si se pone el tipo de error, solo salta cuando aparece el tipo de error especificado.
        print('No se puede dividir por ', numero)
    except TypeError:
        print('El ', numero, ' es un string')

# Hace un codigo, y si ese codigo da error devuelve la segunda linea

eneavo(3)
eneavo(0)

