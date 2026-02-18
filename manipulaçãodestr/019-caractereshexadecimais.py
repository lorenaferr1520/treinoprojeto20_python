permitidos = "0123456789abcdefABCDEF"
entrada = input("Digite o código para verificar: ")

for caractere in entrada:
    if caractere not in permitidos:
        eh_hexadecimal = False
        break  # Se achou um erro, não precisa continuar olhando o resto
    
if eh_hexadecimal and entrada != "":
    print("Sucesso! A string é hexadecimal.")
else:
    print("Erro! Contém caracteres não permitidos para hexadecimal.")