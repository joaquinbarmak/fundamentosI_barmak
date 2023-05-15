# ejercicio 6
class Calculadora:
    def __init__(self):
        self.valor = 0
    
    def cargar(self, numero):
        self.valor = numero

    def sumar(self, numero):
        self.valor += numero
    
    def restar(self, numero):
        self.valor -= numero
    
    def multiplicar(self, numero):
        self.valor *= numero
    
    def valorActual(self):
        return self.valor

calculadora = Calculadora()
calculadora.cargar(0)
calculadora.sumar(4)
calculadora.multiplicar(5)
calculadora.restar(8)
calculadora.multiplicar(2)
print(calculadora.valorActual())

# ejemplo Raise Exception

def god(numero):
    if numero > 10:
        return 'oh yeah'
    else:
        raise Exception('que onda')

print(god(9))


'''
Polimorfismo: poder enviarle el mismo mensaje a objetos de distintas clases. 
Tiene que haber una clase que utilice a otras dos clases. Deben haber si o si dos mensajes. 
Se da un mismo mensaje pero el resultado es distinto.

Los atributos siempre están en el _init_(), pero dentro del () están los parámetros.

Estado: El conjunto de atributos. El estado seria: self.edad, self.altura, self.energia.

_init_ es el constructor.

Interfaz: Es el conjunto de métodos o mensajes que pueden tener una clase.
'''