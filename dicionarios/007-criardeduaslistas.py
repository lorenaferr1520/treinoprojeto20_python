tecnologias = ["Python", "Machine Learning", "SQL", "Deep Learning"]
interesse = [95, 100, 80, 90]
meu_aprendizado = dict()

for tech, nivel in zip(tecnologias, interesse):
    meu_aprendizado[tech] = nivel
    
print(meu_aprendizado)