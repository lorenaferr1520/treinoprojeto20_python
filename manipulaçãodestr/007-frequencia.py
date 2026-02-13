frase = input("Digite uma palavra: ").upper()
contagem = {}

for letra in frase:
    if letra in contagem:
        contagem[letra] += 1 # Já vi essa letra, soma mais uma
    else:
        contagem[letra] = 1 # Primeira vez que vejo essa letra

for key in contagem:
    print(f'A letra {key} aparece {contagem[key]} vezes')