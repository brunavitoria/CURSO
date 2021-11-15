########### Uso da biblioteca NumPy ###########
import pandas as pd
import numpy as np

# Series

# Criando uma Series
nota = pd.Series([8, 7, 9, 6, 10])
print(nota)
print(nota.index)
print(nota.values)

copa = pd.Series([2010,2014,2018,2022], index=["A", "B", "C", "D"])
print(copa.index)

# Calculos
print('Media: ', nota.mean())
print('Maior nota: ', nota.max())
print('Desvio padrao: ', nota.std())
print('Soma: ', nota.sum())

# DataFrame

# Criando um DataFrame
df_alunos = pd.DataFrame({
    'Aluno' : ['João', 'Paola', 'Lucas', 'Vitor', 'Ana'],
    'Matricula' : [201801,201802,201803,201804,201805],
    'Atividades': [9.3,7.6,5.8,8.4,10],
    'Prova': [8.5,9.6,9.8,7.2,8.6],
    'Turma' : [201,203,202,203,202]
})
print(df_alunos)
print(df_alunos.dtypes)
print(df_alunos.columns)
print(df_alunos['Prova'])

# Ler arquivos de dados com pandas
df = pd.read_csv('pandas.csv', sep=',')
# pd.read_xlsx le tabelas de uma planilha excel
# pd.read_html le tabelas de um site

# Imprimindo dados lidos com pandas
print(df)
print(df.head())
print(df.tail())

# Algumas funcoes comuns em pandas
print(df.T) # Transposicao dos dados
print(df.shape) # Dimensao dos dados (linhas e colunas)
print(df.info()) # Retorna informacoes sobre os dados
print(df.describe()) # Retorna: Quantidade, media, desvio padrao, valor minimo, 25% da coluna, 50% da coluna (media), 75% da coluna e valor maximo.

# Filtrando dados de um dataframe
print(df[df['valor'] > 3000])
print(df[(df['valor'] > 1000) & (df['valor'] <= 3000)])

# Filtrar dados de um dataframe com as funções loc e iloc
print('Loc:')
print(df.loc[1:3])
print(df.loc[[1,3]])
print(df.loc[(df['valor'] < 1000)])


#### Manipulando dados de um dataframe ####
# Criando uma nova coluna
df['quantidade'] = 100 
print(df)
# alterado os dados de uma coluna
df['quantidade'] -= 20 
print(df)

# Lista valores unicos de uma coluna
print(df_alunos["Turma"].unique())
# Lista a contagem de valores de uma coluna
print(df_alunos["Turma"].value_counts())
# Agrupa dados de uma coluna e calcula a media
print(df_alunos.groupby("Turma").mean())

# Retornando linhas que não contem valor NaN
df.dropna()
# Preenchendo valores NaN de um dataframe
df.fillna(99)
# Verifica valores NaN de um df
df.isna()
