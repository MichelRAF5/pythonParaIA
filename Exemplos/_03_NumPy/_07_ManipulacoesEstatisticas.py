import numpy as np

# O NumPy permite aplicar cálculos estatísticos de maneira simples e eficiente, como média, desvio padrão e correlação.

array= np.array([5.5, 6.0, 6.3, 5.9])
print(f"Array: {array}\n")

# Calculo da média:
media= np.mean(array)
print(f"Média: {media}\n")

# Calculo do desvio padrão
desvio= np.std(array)
print(f"Desvio padrão: {desvio}\n")

# Na matriz de correlação, que permite avaliar a relação entre dois ou mais conjuntos de valores.

matriz= np.array([[10, 20, 30], 
                  [15, 22, 29]])
print(f"Matriz: \n{matriz}\n")

# Correlação da matriz:
correlacao= np.corrcoef(matriz)
print(f"Correlação: \n{correlacao}")
# Este comando avalia a correlação entre as leituras de diferentes sensores, o que pode ser útil para identificar padrões entre variáveis de processo.