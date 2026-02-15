# caçar a maior palavra da frase

frase = list(input("Digite uma frase: ").split())
print(frase)
maior = str()

for palavra in frase:
    if len(palavra) > len(maior):
        maior = palavra

print(f'A maior palavra da frase é {maior}')