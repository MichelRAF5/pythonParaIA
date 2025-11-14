from Destinos import DestinosLista

print("Vamos encontrar seu destino ideal!")
 
clima = input("Prefere clima quente ou frio?: ").strip().lower()
tipo = input("Prefere natureza ou cidade?: ").strip().lower()
orcamento = float(input("Qual é o seu orçamento máximo (R$)?: "))

encontrado = False
 
for destino in DestinosLista.destinos:
  if destino.combina_com(clima, tipo, orcamento):
    print(f"Sugestão: {destino.nome}")
    print("Boa viagem!")
    encontrado = True
    break
 
if not encontrado:
  print("Infelizmente, não encontramos destinos compatíveis com suas preferências.")