# contar quantas vogais existem em uma frase
vogais = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
apenasvogais = ''
contador = 0

frase = str(input('Frase: '))

for i in frase:
    if i in vogais:
        contador += 1
        apenasvogais += i

print(f"Vogais encontradas: {apenasvogais}")
print(f"Total de vogais: {contador}")