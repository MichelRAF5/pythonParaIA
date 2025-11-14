import numpy as np

# Além das operações aritméticas básicas, o NumPy oferece uma vasta coleção de funções matemáticas otimizadas que podem ser aplicadas diretamente a arrays.

array= np.array([1, 2, 3, 4, 5])
print(f"Array original: {array}\n")

# Raiz quadrada de cada elemento: np.sqrt()
raizQuadrada= np.sqrt(array)
print(f"Raiz quadrada de cada número da array: \n{raizQuadrada}\n")

# Seno (em radianos) de cada elemento: np.sin()
seno= np.sin(array)
print(f"Seno de cada número da array: \n{seno}\n")

# Logaritmo natural de cada elemento: np.log()
log= np.log(array)
print(f"Logaritmo natural de cada número da array: \n{log}\n")

# A biblioteca numpy também oferece funções para calcular exponenciaisnp.exp()), cossenos (np.cos()), tangentes (np.tan()), e muitas outras operações.