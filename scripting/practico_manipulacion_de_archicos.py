#ej1
def start_with(letra, archivo):
    count = 0
    with open(archivo, 'r') as file:
        for line in file:
            if (line[0] != letra.lower() or line[0] != letra.upper()):
                count += 1
    print('el numero de lines que no empiezan con', letra, 'es', count)

start_with('H', 'documento')

#ej2
def read_n_lines(n, archivo):
    with open(archivo,'r') as f:
        for i in range(n):
            print(f.readline())

read_n_lines(2, 'documento')

#ej3
def read_n_back_lines(n, archivo):
    texto = open(archivo,'r').readlines()
    for i in range((len(texto)-n), len(texto)):
        print(texto(i))



#ej4
def longest_word(archivo):
    max_long = 0
    palabra = ''
    with open(archivo, 'r') as f:
        word_list = f.read().split()
        for word in word_list:
            if len(word) > max_long:
                max_long = len(word)
                palabra = word
    print('la palabra mas larga es ', palabra, ' con', max_long, ' caracteres')
