def linha():
    print('-=-' * 20)

linha()
print('                        RECIBO')
linha()
loja = {
    'notebook': 3295.80,
    'impressora': 849.90,
    'playstation 5': 3980.99,
    'mesa digitalizadora': 220.80,
    'Camisa gamer': 80.00,
    'controle playstation': 325.60,    
}
soma = float()
soma = sum(loja.values())
print(f'A soma total da compra foi R${soma:.2f}')