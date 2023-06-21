from aves import pepita, anastasia, roberta

print('Pepita al comienzo: ', pepita.energia)
print(pepita.volar_en_circulos())
print('Pepita despues de volar: ', pepita.energia)
print(pepita.comer_alpiste(200))
print('Pepita despues de comer: ', pepita.energia)
print(pepita)
#print(pepita.hablar()) esto no lo puede hacer
print('Anastasia al comienzo: ', anastasia.energia)
print(anastasia.volar_en_circulos())
print('Anastasia despues de volar: ', anastasia.energia)
print(anastasia.comer_alpiste(200))
print('Aepita despues de comer: ', anastasia.energia)
print(anastasia)
print('Roberta al comienzo: ', roberta.energia)
roberta.volar_en_circulos()
print('Roberta despues de volar: ', roberta.energia)
#roberta.comer_alpiste(200)
#print('Roberta despues de comer alpiste', roberta.energia) #no come alpiste
roberta.escupir_fuego()
print('Roberta despues de escupir fuego: ', roberta.energia)
roberta.comer_peces(200)
print('Roberta despues de comer: ', roberta.energia)