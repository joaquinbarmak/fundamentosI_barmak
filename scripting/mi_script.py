#ej 1
def anterior(numero):
    return numero-1

def siguiente(numero):
    return numero+1

#print(anterior(5))

#ej 2
def doble (numero):
    return numero*2

#print(doble(5))

#ej 3
def doble_anterior(numero):
    return str(doble(anterior(numero))) + " " + str(doble(siguiente(numero)))

#print(doble_anterior(2))

#ej 4
def retirar_dinero(saldo, monto):
    return max(saldo-monto, 0)

#print(retirar_dinero(100,40))

#ej 5
def dia_de_la_semana_favorito(dia):
    return dia == "Sabado"

#print(dia_de_la_semana_favorito('Sabado'))

#ej 11

def empieza_con_h (p):
    if p.startswith('h'):
        return len(p)

print(empieza_con_h('zapatilla'))

#ej 12
def buenos(f):
    return f.startswith("Buenos") or f.startswith("Buenas")

print(buenos('Buenos dias'))