import pandas as pd

# DataFrame como uma folha de cálculo inteligente ou uma tabela de banco de dados,
# em que os dados são dispostos em linhas e colunas. Cada coluna representa uma variável,
# como temperatura ou pureza, e cada linha corresponde a uma observação, como um registro de produção específico.

dados_producao_vacinas= {
    'data': ['2025-05-01', '2025-05-01', '2025-05-02', '2025-05-02', '2025-05-03'],
    'turno': ['Manhã', 'Tarde', 'manhã', 'tarde', 'Manhã'],
    'temperatura_reator': [75.2, 76.1, 74.9, 75.5, 76.0],
    'concentracao_reagente': [0.98, 0.97, 0.99, 0.98, 0.97],
    'pureza_final': [99.5, 98.8, 99.7, 99.0, 99.2]
}

df_vacinas= pd.DataFrame(dados_producao_vacinas) # Para usarmos o Data Frame usamos o método .DataFrame()
print("DataFrame criado: \n", df_vacinas)


# Inconsistências em dados categóricos são comuns. Por exemplo, a coluna 'turno' pode ter sido inserida como 'Manhã', 'manha', 'MANHA'.
# Para que o Python as trate como a mesma categoria, precisamos padronizá-las.
# Uma forma simples de fazer isso é padronizando a capitalização das palavras.

df_vacinas['turno']= df_vacinas['turno'].str.capitalize()
# df_vacinas['turno']:
# Acessa a coluna chamada 'turno' do DataFrame df_vacinas

# .str:
# Indica que vamos trabalhar com operações de string (texto)

# .capitalize():
# Converte o primeiro caractere para maiúsculo e converte todos os outros caracteres para minúsculo

print("\nDataframe após padronização: \n", df_vacinas)


# Valores ausentes podem comprometer seriamente a análise dos dados, levando a conclusões equivocadas ou enviesadas.
# Por isso, identificar e tratar esses valores é uma etapa indispensável no processo de preparação.
df_vacinas.loc[0, 'temperatura_reator'] = None # Simula um valor nulo para o exemplo

media_temperaturas= df_vacinas['temperatura_reator'].mean() # calculamos a média das temperaturas
# Usamos o método .fillna() para preencher os valores nulos com algo, neste caso preenchemos com o valor da média
df_vacinas['temperatura_reator'] = df_vacinas['temperatura_reator'].fillna(media_temperaturas) 

print("\nDataFrame após preenchimento de valores nulos na temperatura do reator: \n", df_vacinas)


# ESTATÍSTICAS DESCRITIVAS:

print("\nEstatísticas descritivas para a pureza final: \n", df_vacinas['pureza_final'].describe())

print("\nDesvio padrão da temperatura do reator: \n", df_vacinas['temperatura_reator'].std())