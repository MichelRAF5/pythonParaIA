import numpy as np

array1= np.array([1, 2, 3])
array2= np.array([4, 5, 6])
print(f"Array 1: {array1} \nArray 2: {array2}\n")

soma= array1+array2
# Ao somar as arrays cada elemento da array1 é somado ao elemento correspondente de array2.
print(f"Soma das arrays 1 e 2: \n{soma}\n")

multiplicacao= array1*array2
# Ao multiplicar as arrays cada elemento da array1 é multiplicado ao elemento correspondente de array2.
print(f"Multiplicação  das arrays: \n{multiplicacao}\n")

divisao= array1/array2
# Ao dividir as arrays cada elemento da array1 é dividido ao elemento correspondente de array2.
print(f"Divisão das arrays: \n{divisao}\n")

# É importante notar que, para que essas operações elemento a elemento funcionem corretamente, os arrays envolvidos devem ter as mesmas dimensões ou dimensões compatíveis 