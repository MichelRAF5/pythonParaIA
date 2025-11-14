import numpy as np

matriz= np.array([[1, 2, 3], 
                  [4, 5, 6],
                  [7, 8, 9]])
print(f"Matriz original: \n{matriz}\n")

# No caso de arrays multidimensionais (matrizes), a indexação e o fatiamento são estendidos para incluir múltiplas dimensões, separadas por vírgulas.
# A sintaxe é [linha, coluna], em que linha e coluna podem ser índices únicos ou fatias.

# Acessando um elemento específico: linha 0, coluna 1 (valor 2):
print(f"Elemento na linha 0, coluna 1: {matriz[0,1]}\n")

# Acessando todos os elementos da coluna 2 (valores 3, 6, 9):
print(f"Elementos da coluna 2: {matriz[:, 2]}\n") # O `:` indica que todas as linhas devem ser consideradas para a coluna especificada.

# Acessando todos os elementos da linha 1 (valores 4, 5, 6):
print(f"Elementos da linha 1: {matriz[1, :]}\n") # O `:` indica que todas as colunas devem ser consideradas para a linha especificada.

# Fatiando uma submatriz: linhas 0 e 1, colunas 0 e 1 (valores [[1, 2], [4, 5]]):
print(f"Submatriz (linhas 0-1, colunas 0-1): \n{matriz[0:2, 0:2]}")