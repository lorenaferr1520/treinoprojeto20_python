# capitalizar primeira e ultima
nome = input("Digite uma palavra: ").strip()


if len(nome) > 1:
    primeira = nome[0].upper()
    meio = nome[1:-1] 
    ultima = nome[-1].upper()
    
    resultado = primeira + meio + ultima
    print(f"Resultado: {resultado}")
else:
  
    print(f"Resultado: {nome.upper()}")
    