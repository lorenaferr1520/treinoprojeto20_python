def corretor_ingles(frase):
    gatilhos = ("what", "how", "why")


    frase = frase.strip().lower()


    if frase.startswith(gatilhos):
        

        if frase.endswith("."):

            frase = frase[:-1] 

        if not frase.endswith("?"):
            frase = frase + "?"
        
        return frase 
    
    else:
        return "Não é uma pergunta iniciada por what, how ou why."

texto_usuario = input("Digite a frase: ")
resultado = corretor_ingles(texto_usuario)
print(f"Saída do Tradutor: {resultado}")