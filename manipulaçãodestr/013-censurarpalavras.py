# censurar palavras proibidas em um texto (substiruir por **** )

proibidas = ["abobrinha", "chato", "bobo", "feio", "urubu", "meleca", "tranqueira", "dengoso", "ranzinza", "soneca"]

texto = list(input('Digite o seu texto: ').split())
textocensurado = ''

for i in texto:
    if i in proibidas:
        i = '*' * len(i)
    textocensurado += i + ' '

print(textocensurado)

