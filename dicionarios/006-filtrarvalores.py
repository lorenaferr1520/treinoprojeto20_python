precos_pc = {
    "Mouse": 50,
    "Teclado": 120,
    "Monitor": 800,
    "Cabo HDMI": 30,
    "RAM 8GB": 250
}

pecas_caras = dict()

for k, v in precos_pc.items():
    if v > 100:
        pecas_caras[k] = v 

print(pecas_caras)