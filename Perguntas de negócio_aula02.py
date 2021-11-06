# carrega um arquivo do disco rígido para a memória
 import pandas as pd
 from numpy import int64

 data = pd.read_csv('datasets/kc_house_data.csv')

# usar função que converte de object (string) para date
data['date'] = pd.to_datetime(data['date'])

# mostra na tela as primeiras 6 linhas
print(data.head())


#######################################################
# Como converter os tipos de vaiáveis
#######################################################

# # inteiro -> float
data['bedrooms'] = data['bedrooms'].astype( float )
print(data.dtypes)

# # float -> inteiro
data['bedrooms'] = data['bedrooms'].astype( int64 )
print(data.dtypes)

# # inteiro -> string
data['bedrooms'] = data['bedrooms'].astype( str )
print(data.dtypes)

# # string -> inteiro
data['bedrooms'] = data['bedrooms'].astype( int64 )
print(data.dtypes)

# # string -> data
data['date'] = pd.to_datetime(data['date'])
print(data.dtypes)


#######################################################
# Criando novas variáveis
#######################################################

data['meu_nome'] = "marcos"
data['comunidade_ds'] = 80
data['data_abertura_comunidade_ds'] = pd.to_datetime('2020-02-28')
data['data_abertura_comunidade_ds'] = pd.to_datetime(data['data_abertura_comunidade_ds'])
print(data.columns)
print(data[['id', 'date', 'meu_nome', 'comunidade_ds', 'data_abertura_comunidade_ds']].head())
print(data.dtypes)

# #######################################################
# # deletando variáveis
# #######################################################

print(data.columns)
cols = ['meu_nome', 'comunidade_ds', 'data_abertura_comunidade_ds']
data = data.drop(cols, axis=1)
print(data.columns)

#######################################################
# Seleção de dados
#######################################################

# Forma 01: Direto pelo nomes das colunas

import pandas as pd
from numpy import int64
data = pd.read_csv('datasets/kc_house_data.csv')

print(data[['id', 'price', 'date']])

# Forma 02: Direto pelo índices das linhas e colunas
# DADOS[linhas, colunas]
# Localizar linhas e colunas através do índice, usar o ILOC.
print(data.iloc[0:10, 0:3])

# Forma 03: Direto pelo índices das linhas e nomes das colunas
# Para selecionar índice e nomes de colunas ou linhas usasse o LOC.

print(data.loc[0:10, ['price', 'id', 'date']])

# Forma 04: índices booleanos

cols = [True, True, True, False, False, False, False,
False, False, False, False, False, False, False,
False, False, False, False, False, False, False]
print(data.loc[0:10, cols])

#######################################################
# RESPONDENDO AS PERGUNTAS DE NEGÓCIOS
#######################################################

import pandas as pd

data = pd.read_csv('datasets/kc_house_data.csv')

# 1 Qual a data do imóvel mais antigo do portifólio?
data['date'] = pd.to_datetime(data['date'])
print(data.sort_values('date', ascending=True).head())

# 2 Quantos imóveis possui o número máximo de andares?
print(data['floors'].unique())
print(data[data['floors'] == 3.5].shape)

# 3 Criar uma classificação para imóveis,
# separando-os em baixou ou alto padrão, de acordo com o preço.

data['level'] = 'standard'
data.loc[data['price'] > 540000, 'level'] = 'high_level'
data.loc[data['price'] < 540000, 'level'] = 'low_level'
print(data['level'])

# 4 Gostaria de um relatório ordenado pelo preço

report = data[['id', 'date', 'price', 'bedrooms', 'sqft_lot', 'level']].sort_values('price', ascending=False)
print(report.head())
report.to_csv('datasets/report_aula02.csv', index=False)

# 5 Gostaria de um mapa indicando onde as casas estão localizadas geograficamente


# plotly - biblioteca que armazena uma função que desenha mapas
# Scatter MapBox - Função que desenha um mapa


data_map = data[['id', 'lat', 'long', 'price']]
mapa = px.scatter_mapbox(data_map, lat='lat', lon='long',
                          hover_name='id',
                          hover_data=['price'],
                          color_discrete_sequence=['darkgreen'],
                          zoom=3,
                          height=300)
mapa.update_layout(mapbox_style='open-street-map')
mapa.update_layout(height=600, margin={'r': 0, 'l': 0, 'b': 0, 't': 0})
mapa.show()


########## RESPONDENDO AS PERGUNTAS DA AULA 02  ##################

# 1. Crie uma nova coluna chamada: "house_age" ==
#  - Se o valor da coluna "date" for maior que 2014-01-01 => 'new_house
#  - Se o valor da coluna "date" for menor que 2014-01-01 => 'old_house
data['house_age'] = "standard"
data.loc[data['date'] > '2014-01-01', 'house_age'] = 'new_house'
data.loc[data['date'] < '2014-01-01', 'house_age'] = 'old_house'
print(data[['date', 'house_age']])

# 2. Crie uma nova coluna chamada: "dormitory_type"
#  - Se o valor da coluna "bedrooms" for igual à 1 => 'studio'
#  - Se o valor da coluna "bedrooms" for igual à 2 => 'apartment'

data['dormitory_type'] = 'house'
data.loc[data['bedrooms'] == 1, 'dormitory_type'] = 'studio'
data.loc[data['bedrooms'] == 2, 'dormitory_type'] = 'apartment'
print(data[['dormitory_type', 'bedrooms']].sort_values('bedrooms').head(20))


# 3. Crie uma nova coluna chamada: "condition_type"
#  - Se o valor da coluna "condition" for menor ou igual à 2 => 'bad'
#  - Se o valor da coluna "condition" for igual à 3 ou 4 => 'regular'
#  - Se o valor da coluna "condition" for igual à 5 => 'good'

data['condition_type'] = ''
data.loc[data['condition'] <= 2, 'condition_type'] = 'bad'
data.loc[data['condition'] == (3 or 4), 'condition_type'] = 'regular'
# data.loc[data['condition'] == 4, 'condition_type'] = 'regular'
data.loc[data['condition'] == 5, 'condition_type'] = 'good'
print(data[['condition', 'condition_type']].head(20))

# 4. Modifique o TIPO da coluna "condition" para STRING
data['condition'] = data['condition'].astype(str)
print(data['condition'].dtypes)

# 5. Delete as colunas "sqft_living15" e "sqft_lot15"
cols = ['sqft_living15', 'sqft_lot15']
data = data.drop(cols, axis=1)
print(data.columns)

# 6. Modifique o TIPO da coluna "yr_build" para DATE
data['yr_built'] = pd.to_datetime(data['yr_built'], format='%Y')
print(data['yr_built'])

# 7. Modifique o TIPO da coluna "yr_renovated" para DATE
data['yr_renovated'] = pd.to_datetime(data['yr_renovated'])
data['yr_renovated'] = data['yr_renovated'].dt.strftime('%Y')
print(data['yr_renovated'].dtypes)

# 8. Qual a data mais antiga de construção de um imóvel?
print(data['yr_built'].sort_values(ascending=True))

# 9. Qual a data mais antiga de renovação de um imóvel?
print(data['yr_renovated'].sort_values(ascending=True).head())


# 10. Quantos imóveis tem 2 andares?
print(data.columns)
print(data[data['floors'] == 2].size)


# 11. Quantos imóveis estão com a condição igual à "regular"?
print(data[data['condition_type'] == 'regular'].shape)

# 12. Quantos imóveis estão com a condição igual a "bad" e possuem "vista para água"?
print(data[(data['condition_type'] == 'bad') & (data['waterfront'] == 1)].shape)


# 13. Quantos imóveis estão com a condição igual a "good" e são "new_house"?
print(data[(data['condition_type'] == 'good') & (data['house_age'] == 'new_house')].shape)

# 14. Qual o valor do imóvel mais caro do tipo "studio"?
print(data[data['dormitory_type'] == 'studio'][['dormitory_type', 'price']].sort_values('price', ascending=False))

# 15. Quantos imóveis do tipo “apartment” foram reformados em 2015 ?
print(data[(data['dormitory_type'] == 'apartment') & (data['yr_renovated'] == 2015)].shape[0])


# 16. Qual o maior número de quartos que um imóveis do tipo “house” possui ?
print(data['yr_renovated'].dtypes)
print(data[data['dormitory_type'] == 'house'][['dormitory_type', 'bedrooms']].sort_values('bedrooms', ascending=False))


# 17. Quantos imóveis “new_house” foram reformados no ano de 2014?
print(data['yr_renovated'])
print(data[(data['house_age'] == 'new_house') & (data['yr_renovated'] == 2014)].shape[0])
#
# 18. Selecione as colunas: "id = 0", "date = 1", "price = 2", "floors" = 7, "zipcode = 16" pelo método:
#  - Direto pelo nome das colunas
#
#  - Pelos índices
#
#  - Pelos índices das linhas e o nome das colunas
#
#  - Índices booleanos

print(data[['id', 'date', 'price', 'floors', 'zipcode']])
print(data.iloc[:, [0, 1, 2, 7, 16]])
cols = [True, True, True, False, False, False, False, True, False,\
        False, False, False, False, False, False, False, True, False,\
        False, False, False, False, False]
print(data.loc[0:10, cols])

#19. Salve um arquivo .csv com somente as colunas do item 10
reports = data[data['floors'] == 2]
reports.to_csv('datasets/reports_s.csv', index=False)

# 20. Modifique a cor dos pontos no mapa de "pink" para "verde-escuro"
import plotly.express as px


data_map = data[['id', 'lat', 'long', 'price']]
mapa = px.scatter_mapbox(data_map, lat='lat', lon='long',
                          hover_name='id',
                          hover_data=['price'],
                          color_discrete_sequence=['darkgreen'],
                          zoom=3,
                          height=300,
                          size='price',
                          size_max=30)
mapa.update_layout(mapbox_style='open-street-map')
mapa.update_layout(height=600, margin={'r': 0, 'l': 0, 'b': 0, 't': 0})
mapa.show()

