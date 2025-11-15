import pandas as pd

# Continuando no problema na fábrica de vacinas, visualizar a relação entre a temperatura do reator e a pureza final ou a pureza final por turno, pode revelar padrões importantes.
dados_producao_vacinas= {
    'data': ['2025-05-01', '2025-05-01', '2025-05-02', '2025-05-02', '2025-05-03'],
    'turno': ['Manhã', 'Tarde', 'Manhã', 'Tarde', 'Manhã'],
    'temperatura_reator': [75.2, 76.1, 74.9, 75.5, 76.0],
    'concentracao_reagente': [0.98, 0.97, 0.99, 0.98, 0.97],
    'pureza_final': [99.5, 98.8, 99.7, 99.0, 99.2]
}

df_vacinas= pd.DataFrame(dados_producao_vacinas)

# Vamos criar um gráfico de barras que mostra a pureza média dos componentes por turno:

media_pureza_por_turno= df_vacinas.groupby('turno')['pureza_final'].mean()
# O método .groupby() agrupa todas as linhas que têm o mesmo valor na coluna 'turno' e cria "grupos" onde cada grupo contém todas as linhas de um mesmo turno
# e o metodo mean faz as médias dos valores da coluna pureza_final

import matplotlib.pyplot as plt
# Matplotlib é a biblioteca de visualização de dados amplamente utilizada em Python.
# Ela oferece uma flexibilidade imensa para criar uma vasta gama de gráficos estáticos, animados e interativos.

import seaborn as sns
# Enquanto o Matplotlib fornece a base para gráficos, o Seaborn oferece uma interface de alto nível para criar visualizações estatísticas mais atrativas e informativas. 
# Construído sobre o Matplotlib, integra-se aos DataFrames do Pandas, facilitando a criação de visualizações complexas e aprimorando a estética dos gráficos.

# Criação do gráfico:

sns.set_theme(style="whitegrid") # Define um estilo de tema para o Seaborn
 
plt.figure(figsize=(8, 6))
sns.barplot(x=media_pureza_por_turno.index, y=media_pureza_por_turno.values, palette="pastel")
plt.title('Pureza Média dos Componentes por Turno (Estilizado com Seaborn)')
plt.xlabel('Turno')
plt.ylabel('Pureza Média (%)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()