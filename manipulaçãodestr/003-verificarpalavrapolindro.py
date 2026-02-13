# verificar se uma palavra é um políndromo
linha = '-=' * 20
print(linha)

palavra = str(input('Palavra: '))
palavracontraria = ''

for i in palavra[::-1]:
    palavracontraria += i

print(palavracontraria)
if palavra.lower() == palavracontraria.lower():
    print(f'A palavra {palavra} é um políndromo!')
else:
    print(f'A palavra {palavra} NÃO é um políndromo!')
print(linha)