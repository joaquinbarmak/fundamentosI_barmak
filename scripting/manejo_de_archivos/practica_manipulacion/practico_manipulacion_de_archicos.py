#ej1
def start_with(letra, archivo):
    count = 0
    with open(archivo, 'r') as file:
        for line in file:
            if (line[0] != letra.lower() or line[0] != letra.upper()):
                count += 1
    print('el numero de lines que no empiezan con', letra, 'es', count)

#start_with('H', 'documento')

#ej2
def read_n_lines(n, archivo):
    with open(archivo,'r') as f:
        for i in range(n):
            print(f.readline())

read_n_lines(2, 'textoejemplo.txt')

#ej3
def read_n_back_lines(n, archivo):
    texto = open(archivo,'r').readlines()
    for i in range((len(texto)-n), len(texto)):
        print(texto(i))



#ej ?
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



#ej9
def join_files(file1, file2, file3):
    with open(file1, 'r') as f1, open(file2,'r') as f2, open(file3, 'r') as f3:
        f3.write(f1.read()+f2.read())

