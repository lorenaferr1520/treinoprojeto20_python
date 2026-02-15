# Extrair apenas o domínio de um e-mail

emailuser = input('Digite seu email: ')
usuario, dominio = emailuser.split("@")

# domínio do email:
print(f"O domínio é: @{dominio}")
