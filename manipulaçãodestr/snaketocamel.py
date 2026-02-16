def eh_snake_case(texto: str) -> bool:
    if not texto:
        return False

    if texto[0] == "_" or texto[-1] == "_":
        return False

    if "__" in texto:
        return False

    if " " in texto:
        return False

    for c in texto:
        if not (c.islower() or c.isdigit() or c == "_"):
            return False

    return True

frase_camel = str()
while True:
    frase = input('Digite uma frase em Snake Case: ').lower()
    
    if eh_snake_case(frase):
        break
    else:
        print('Apenas frase Snake Case')

print('Passou!')
frase_lista = frase.split('_')
for palavra in frase_lista:
    frase_camel += palavra.capitalize()

print(frase_camel)