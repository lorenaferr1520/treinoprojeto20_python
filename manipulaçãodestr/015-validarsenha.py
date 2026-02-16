# 1 maiuscula, 1 número, pelo menos 8 caracteres

print('-=- VALIDADOR DE SENHA -=-')
while True:
    senha = input('Digite sua senha: ')
    tem_maiuscula = any(c.isupper() for c in senha)
    tem_numero = any(c.isdigit() for c in senha)

    if len(senha) >= 8 and tem_maiuscula and tem_numero:
        break
    else:
        print('''ERROR! 
A senha prescisa ter: 
8 caracteres no minimo
1 letra maiuscula
1 número''')

print('Passou!')