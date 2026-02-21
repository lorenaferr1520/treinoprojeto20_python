# Dicionário Original (Produto: Categoria)
produtos = {
    "GTX 1050 Ti": "GPU",
    "i3-10105F": "CPU",
    "Monitor LG": "Periférico"
}


produto_invertido = dict()
for chave, valor in produtos.items():
    produto_invertido[valor] = chave
    
print(produto_invertido)
