import numpy as np

# Em arrays unidimensionais, a lógica de indexação segue o padrão conhecido em Python: o primeiro elemento ocupa a posição de índice 0, o segundo ocupa o índice 1, e assim por diante.
array= np.array([10, 20, 30, 40, 50])
print(f"Array: {array}\n")

print(f"Primeiro elemento da array: {array[0]}")
print(f"Último elemento da array: {array[-1]}\n") # Usando o índice -1 acessamos o ultimo índice

# O fatiamento (slicing) em arrays unidimensionais permite extrair um subconjunto contínuo de elementos de um array.
# A sintaxe básica é [start:stop:step], em que start é o índice inicial (inclusive), stop é o índice final (exclusive), e step é o tamanho do passo.

# Exibindo índices 1 ao 3:
print(f"Indices 1 ao 3 da array: {array[1:4]}\n")  # Na sintaxe usamos o start e o stop

# Exibindo até o terceiro elemento da array:
print(f"Do início ao índice 2: {array[:3]}\n") # Deixamos o start vazio e declaramos o stop

# Exibindo do terceiro  até o final:
print(f"Do índice 2 ao final: {array[2:]}\n") # Declaramos o start e deixamos o stop vazio

# Exibindo a cada 2 elementos:
print(f"Elementos com passo de 2: {array[::2]}") # Deixamos o start e o stop vazios e declaramos o step