resultado = ''

palavra = input('Digite uma palavra: ').lower()

for i in palavra:
    if len(resultado) == 0 or i != resultado[-1]:
        resultado += i

print(f"Resultado sem duplicatas adjacentes: {resultado}")