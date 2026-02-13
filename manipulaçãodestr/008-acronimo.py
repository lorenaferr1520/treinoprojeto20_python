# acrônimo a partir de uma frase

frase = (input('Digite sua frase: ').upper()).split()
print(frase)
acronimo = ""

for palavra in frase:
    acronimo += palavra[0]

print(acronimo)