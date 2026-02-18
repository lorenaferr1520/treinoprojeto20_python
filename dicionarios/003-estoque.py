# Verificar se uma chave existe no dicionário antes de acessá-la.
estoque_pc = {
    "processador i3": 5,
    "processador i5": 3,
    "processador i7": 2,
    "placa de video gtx 1050 ti": 1,
    "placa de video rtx 3060": 4,
    "memoria ram 8gb": 12,
    "memoria ram 16gb": 8,
    "ssd 240gb": 15,
    "ssd 480gb": 10,
    "ssd 1tb": 5,
    "placa mae h410": 4,
    "placa mae b450": 6,
    "fonte 500w": 7,
    "fonte 600w": 3,
    "gabinete gamer": 10,
    "cooler fan 120mm": 25,
    "pasta termica": 50,
    "monitor 24 pol": 6,
    "teclado mecanico": 8,
    "mouse gamer": 12
}

verifica = input('Qual item deseja encontrar no estoque: ').strip().lower()

if verifica in estoque_pc:
    print(f'o item {verifica} tem o total de {estoque_pc[verifica]} unidades')
else:
    print('não tem')
