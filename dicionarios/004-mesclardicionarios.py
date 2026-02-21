# dificionarios dos fornecedores
fornecedor_a = {
    "Processador i3": 500,
    "GTX 1050 Ti": 800,
    "Memoria RAM 8GB": 200
}

fornecedor_b = {
    "Monitor 24pol": 900,
    "SSD 480GB": 250,
    "Memoria RAM 16GB": 350
}
# estoque final com todos os produtos
estoque_total = fornecedor_a | fornecedor_b

print(estoque_total)
