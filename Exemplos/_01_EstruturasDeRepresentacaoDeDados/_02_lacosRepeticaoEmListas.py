# Estrutura for each em python para percorrer uma lista:
input("Aperte Enter pra a ver o exemplo na lista")

pecas_substituidas= ["motor", "suspensão", "roda"]

for peca in pecas_substituidas:
    print(f"A peça {peca} foi substituída")

print("---------------------------------------------------------------------------------------------")

# Estrutura for each em python para percorrer um dicionário:
input("Aperte Enter para ver o exemplo no dicionário")

estoque= {
    "válvula": 5,
    "sensor": 3,
    "motor": 2
} 

print("For para listar peças e quantidades:")
for peca, quantidade in estoque.items(): # Usamos o método items para percorrer os itens do dicionário
    print(f"{peca}: {quantidade} unidades")

print("For para listar apenas as quantidades:")
for peca in estoque.values():
    print(peca)

print("---------------------------------------------------------------------------------------------")