# Dicionário de um Servidor de Treinamento de IA
servidor_ia = {
    "modelo": "NVIDIA DGX Station",
    "gpu": "A100",
    "vram_gb": 80,
    "armazenamento_tb": 2,
    "sistema_operacional": "Ubuntu 22.04",
    "localizacao": "Data Center Toronto"
}
while True:
    chave = input('O que deseja encontar: ')

    if chave in servidor_ia:
        print('Dados encontrados:')
        print(f'{chave}: {servidor_ia[chave]}')
    else:
        print('Não foi possivel encontrar sua solicitação!')
    
    resposta = input('Deseja outra busca? [s/n]').lower()
    if resposta != 'n':
        continue

    else:
        break

print('Fim do programa!')
