palavras_chave = ["promoção", "vaga", "urgente", "reunião", "desconto"]
classificacao = ["Spam", "Seguro", "Spam", "Seguro", "Spam"]

filtro_email = dict()

for chave, clas in zip(palavras_chave, classificacao):
    filtro_email[chave] = clas
    
print(filtro_email)