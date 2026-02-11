# inverter uma str
linha = '-=' * 20    
palavrainvertida = ''
print(linha)

palavra = str(input('Digite uma palavra ou frase: '))

print(linha)

for letra in palavra[::-1]:
    palavrainvertida += letra

print(palavrainvertida)