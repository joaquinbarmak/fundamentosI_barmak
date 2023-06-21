#punto 1
def entre_X_Y_con_ab (string):
    patron = 'X(.*?ab.*?)Y' #no me importa lo que este antes o despues
    patron2 = 'X([^XY]*ab[^XY]*)Y'
    return re.findall(patron, string) #c


#punto 1b
def entre_ag_cta_sin_numeros(string):
    return re.findall('ag([^\d]*)cta', string)

#punto 2
import glob , re

def filtrar(archivo):
    lista_txt = glob.glob('*.txt')

    with open(archivo, 'a') as arch:
        for archivo in lista_txt:
            with open(archivo, 'r') as archivo_secreto:
                texto = archivo_secreto.read()
                lista = re.findall('[\W\+[-_\.]*[\W]*+gmail.com', texto) #empieza seguro con un numero/letra , en el medio sigue con 
                for email in lista:                                   #los otros digitos, y puede terminar con numero/letra
                    arch.write(email+'\n')

print(entre_X_Y_con_ab('XbaaaYjXababYqXbabbbbaaY'))