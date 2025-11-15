# Listas:
input("Aperte Enter para mostrar os exemplos de listas.")

lista= ["válvula", "sensor", "motor", "válvula"] # Criamos uma lista 
print(lista)

lista.append("motor") # Adiciona o item ao final  da lista
print(lista)

lista.remove("válvula") # Remove a primeira intercorrência do item na lista
print(lista)

print(lista.count("sensor")) # Conta quantas intercorrências existem do item e printa o valor inteiro

print("---------------------------------------------------------------------------------------------")

# Tuplas:
input("Aperte Enter para mostrar o exemplo de tupla.")

tupla= ("válvula", "sensor", "motor", "válvula") # Tupla é uma lista de dados fixos
print(tupla)

print(tupla[0]) # Printamos o índice 0 da tupla. 

# As tuplas podem ser acessadas assim como as listas, porém não podem ser modificadas.

print("---------------------------------------------------------------------------------------------")

# Conjunto (set):
input("Aperte Enter para mostrar o exemplo de (set)")

tuplaSet= set(tupla) # Pegamos a tupla criada no exemplo anterior (que tem um índice repetido) e usamos a função set.
print(tuplaSet)
print(f"quantidade de itens unicos na tupla: {len(tuplaSet)}")

# A função set serve para transformar essa lista em um conjunto. Um conjunto é uma estrutura que só guarda itens únicos, ou seja, não permite repetições.

print("---------------------------------------------------------------------------------------------")

# Dicionário:
input("Aperte Enter para mostrar os exemplos de dicionário.")

estoque= {
    "válvula": 5,
    "sensor": 3,
    "motor": 2
} 
# Criamos um dicionário usando {} e cada ítem possui uma chave(nome) e uma valor(quantidade)

print(estoque)

print(estoque.items()) # Aqui usamos o método items para retornar todos os pares de chave e valor que estão dentro do dicionário.

print("Quantidade de válvulas: ", estoque["válvula"]) # Aqui printamos a chave válvula para exibir o seu valor

# Podemos também adicionar, alterar e remover itens de um dicionário:

del estoque["motor"] # Aqui deletamos uma chave
print("Estoque após a retirada do motor: ", estoque)

estoque["suspensão"]= 4 # Aqui adicionamos um item ao dicionário
print("Estoque após a adição da suspensão: ", estoque)

estoque["suspensão"]= 10 # Modificamos a quantidade de suspensões no estoque
print("Estoque após modificar a quantidade de suspensões: ", estoque)

print("---------------------------------------------------------------------------------------------")