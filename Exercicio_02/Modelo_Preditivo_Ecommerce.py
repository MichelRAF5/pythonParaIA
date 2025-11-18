import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# idade: idade dos clientes cadastrados
# tempo_cadastro: tempo de cadastro dos clientes em meses
# email_aberto: confirmação se abriu ou não o email da loja (0=não, 1=sim)
# click_link: confirmação se o cliente clicou ou não no link
# comprou: confirmação se o cliente comprou ou não o produto
dados= pd.DataFrame({
    'idade': [18, 30, 20, 19, 26, 37, 20, 18, 19],
    'tempo_cadastro': [10, 3, 4, 7, 9, 12, 9, 8, 1],
    'email_aberto': [0, 1, 1, 1, 0, 1, 1, 0, 1], 
    'click_link': [0, 1, 0, 1, 0, 1, 0, 0, 1],
    'compra': [0, 1, 0, 0, 0, 1, 0, 0, 1]
})

x= dados.drop('compra', axis=1)
y= dados['compra']

x_treino, x_teste, y_treino, y_teste= train_test_split(x, y, test_size= 0.3, random_state=42)

modelo= DecisionTreeClassifier()
modelo.fit(x_treino, y_treino)

previsoes= modelo.predict(x_teste)

print(f"Acurácia do modelo: {accuracy_score(y_teste, previsoes)}")