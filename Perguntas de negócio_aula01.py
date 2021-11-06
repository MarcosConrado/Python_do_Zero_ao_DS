# carregue o conjunto de dados do HD

import pandas as pd

data = pd.read_csv("datasets/kc_house_data.csv")

# mostre na tela as 5 primeiras linhas do dataset
print(data.head())

# mostre na tela o número de linhas e colunas do dataset

print(data.shape)

# mostre na tela o nome das colunas do dataset

print(data.columns

# mostre na tela o dataset ordenado pela coluna "price"

print(data[['id', 'price']].sort_values('price'))

# mostre na tela o dataset ordenado pela coluna "price" do maior até o menor

print(data[['id', 'price']].sort_values('price', ascending=False))
      
      
      
########## RESPONDENDO AS PERGUNTAS DA AULA 01 ##################
      

#1 Quantas casas estão dísponiveis para compra?
print(data.shape[0])  # Há 21613 casas disponíveis para a compra.

#2 Quantos atributos as casas possuem?
#print(data.shape[1])  # As casas possuem 21 atributos

#3 Quais são os atributos das casas?
print(data.columns)  #Os atributos são 'id', 'date', 'price', 'bedrooms', 'bathrooms', 'sqft_living',
                     #'sqft_lot', 'floors', 'waterfront', 'view', 'condition', 'grade',
                     #'sqft_above', 'sqft_basement', 'yr_built', 'yr_renovated', 'zipcode',
                     #'lat', 'long', 'sqft_living15', 'sqft_lot15'

#4 Qual a casa mais cara (casa com maior valor de venda) ?
print(data[['id', 'price']].sort_values('price', ascending=False))  # á casa mais cara é a do
                                                                            # id: 6762700020


#5 Qual a casa com maior número de quartos?
print(data[['id', 'price', 'bedrooms']].sort_values('bedrooms', ascending=False))
# Á casa com maior número de quartos é de 3 quartos, do id: 2402100895

#6 Qual a soma total de quartos do dataset?
print(data['bedrooms'].sum())  # São 72.854 quartos

#7 Quantas casas possuem 2 banheiros?
print((data['bathrooms'] == 2).shape())  # Há 1930 casas com 02 banheiros

print(data['price'].mean().round(0))  # O preço médio de todas as casas são 540.088

#8 Qual o preço médio de casas que possuem 2 banheiros?
print(data.loc[data['bathrooms'] == 2,'price'].mean())  # O preço médio das casas que possuem 2 quartos é 401.373

#9 Qual o preço mínimo das casas com 3 quartos?
print(data.loc[data['bedrooms'] == 3,'price'].min())  # O menor preço das casas com 3 quartos é 82.000










