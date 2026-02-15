# contar sub-string em texto grande

texto_grande = list(input('Digite seu texto: ').lower().split())
sub_palavra = input('Qual palavra deseja contabilizar no texto: ').lower()
substr = 0

for i in texto_grande:
    if i == sub_palavra:
        substr += 1

print(f'No texto enviado foram encontrados {substr} vezes a palavra {sub_palavra}')