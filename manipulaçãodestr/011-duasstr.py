# intercalar duas strings letra por letra

palavra1 = input('Palavra 1: ')
palavra2 = input('Palavra 2: ')
palavras = str()


for i in range (len(palavra1)):
    palavras += palavra1[i]
    palavras += palavra2[i]
print(palavras)