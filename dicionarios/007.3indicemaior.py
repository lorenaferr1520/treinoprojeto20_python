alunos = ["Lorena", "Paulo", "Maria", "João", "Clara"] # 5 itens
notas = [95, 80, 75, 60] # 4 itens (A Clara ficou sem nota!)

pauta_final = dict()

if len(alunos) != len(notas):
    print("Atenção: Existem dados em falta!")

for estudantes, pontos in zip(alunos, notas):
    pauta_final[estudantes] = pontos

print(pauta_final)
