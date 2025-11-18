import pandas as pd
from sklearn.model_selection import train_test_split # para dividir os dados em treino e teste
from sklearn.tree import DecisionTreeClassifier # o algoritmo de Árvore de Decisão
from sklearn.metrics import accuracy_score # para calcular a acurácia do modelo

# horario: hora do atendimento 
# dia_semana: dia da semana (0=segunda, 1=terça,...) 
# faixa_etaria: grupo etário do paciente (1=jovem, 2=adulto, 3=idoso) 
# mensagem: se recebeu mensagem lembrando da consulta (1=sim, 0=não) 
# primeira_consulta: se é a primeira consulta (1=sim, 0=não) 
# compareceu: se o paciente compareceu ou não (1=sim, 0=não) 

dados= pd.DataFrame({
   'horario': [8, 9, 10, 14, 15, 16],
   'dia_semana': [0, 1, 1, 3, 4, 5],
   'faixa_etaria': [1, 2, 3, 2, 1, 3],
    'mensagem': [1, 0, 1, 1, 0, 0],
    'primeira_consulta': [0, 1, 0, 0, 1, 1],
    'compareceu': [1, 0, 1, 1, 0, 0]
})

# variáveis independentes (variáveis controladas ou 'causa')
# variável alvo (variável a ser observada / medida)
# Separando as variáveis independentes (x) e a variável alvo (y):
x= dados.drop('compareceu', axis=1) # X são todas as colunas exceto 'compareceu'. axis=1: coluna e axis=0 linha, serve para especificar que queremos retirar uma coluna
y= dados['compareceu'] # y é apenas a coluna 'compareceu'

# Dividindo os dados em conjunto de treino e conjunto de teste:
#Treino: Para o modelo aprender os padrões
#Teste: Para avaliar se o modelo generaliza bem com dados nunca vistos
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3, random_state=42) 
# 70% para treino e 30% para teste
# random_state=42 usa sempre a mesma tecnica de embaralhamento dos dados para teste e treino

# Criando o modelo de Árvore de Decisão:
modelo= DecisionTreeClassifier()

# Treinando o modelo com os dados de treino:
modelo.fit(x_treino, y_treino)

# Fazendo previsões no conjunto de teste:
previsoes= modelo.predict(x_teste)

# Calculando a acurácia do modelo (quantas previsões o modelo acertou em relação ao total):
print("Acurácia do modelo: ", accuracy_score(y_teste, previsoes))