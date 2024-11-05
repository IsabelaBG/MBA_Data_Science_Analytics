# -*- coding: utf-8 -*-
# Aula Introdutória

# O elemento #%% cria células dentro do script e ajuda na organização
# Assim, é possível executar o conteúdo daquela célula com "shift + enter"

# Para executar apenas uma linha ou uma seleção, utilize o F9

#%% Operações Báicas

# Adição
print(5+10)

x = 3
y = 9
z = x + y
print(z)

# Subtração
print(188-87)

# Multiplicação
print(4*555)

# Divisão
print(144/12)

# Exponenciação
print(12**2)

#%% Pacotes

# Precisam ser instalados previamente, digitando comando pip install "pacote" no console
# Após instalação no projeto, necessário fazer import

!pip install pandas
!pip install numpy
!pip install matplotlib
!pip install seaborn
!pip install plotly

import math
print(math.sqrt(256))

import numpy as np
import pandas as pd

print(np.sqrt(256))

# Para acessar o Help das funções, posicione o cursor e clique Control + I

#%% Objetos

# Spyder lista os objetos no ambiente à direita

# Objeto: Lista
# Contagem de elementos da lista se inicia pelo zero
lista_numeros = [2,4,6,8,10,12,14]

print(lista_numeros[2])
print(lista_numeros[3]-lista_numeros[2])

lista_textos = ['Azul','Verde','Amarelo','Rosa','Branco']

print(lista_textos[0])
print('Minha cor favorita é ' + lista_textos[0])

# Objeto: Series
# Muito usado em bancos de dados, podem ser séries numéricas, lógicas ou de caracteres
# Utilizando a função Series do pacote Pandas
# Série numérica
numeros = pd.Series([2,4,6,8,10,12,14,16])
print(numeros)

# Série de caracteres
cores = pd.Series(['Roxo','Lilás','Bege','Púrpura','Laranja'])
print(cores)

# Série de argumentos lógicos
logico = pd.Series([True,False])
print(logico)

#%% Classes de objetos

# Número inteiro ou "int"
print(type(29))

# Número com casas decimais "float"
print(type(3.1415))

# Caracteres ou "string"
print(type("Isabela"))

# Booleano (verdadeiro ou falso) ou "bool"
print(type(True))

# Uma Series que criamos por meio do pandas
print(type(cores))

#%% Comprimento de objetos

print(len(numeros))
print(len(cores))
print(len(logico))
print(len(lista_numeros))

#%% Sequência de objetos
# Utilizando a função Arange do pacote Numpy
# Função Arange inclui número inicial, mas exclui o final

sequencia_1 = np.arange(1, 10)
sequencia_2 = np.arange(1, 10, 0.5)

# Se atribuir o mesmo nome a outro objeto, o objeto antigo é substituído
sequencia_1 = np.arange(100, 200)

#%% Series variadas
# Neste caso, a série fica toda identificada como texto (?)

varios = pd.Series([10, 20, 30, "Azul", "Verde", "Vermelho", False, False, True])
print(varios)
print(type(varios[4]))

#%% Comparações entre séries

# Igualdade
print(numeros == 20)

# Multiplicação
print(numeros * 2)

# Multiplicação e criação de objeto
triplo_numeros = numeros * 3

# Divisão e criação de objeto
metade_numeros = numeros / 2

# Comparando textos (verificando diferença)
print(cores != "Amarelo")

# Comparando números (maior)
print(sequencia_2 > 5)

# Comparando números (maior ou igual)
print(sequencia_2 >= 4.5)

# Comparando números (menor)
print(sequencia_1 < 1010)

# Comparando números (menor ou igual)
print(sequencia_1 <= 1003)

#%% Séries com dados categóricos / qualitativos

tipos = pd.Series(["TipoA", "TipoB", "TipoB", "TipoA", "TipoC", "TipoB"], dtype="category")
print(tipos)

#%% Dicionários

#Criação
dict_uf = {"estado": "SP",
           "regiao": "Sudeste"}

print(dict_uf["estado"])
print(dict_uf["regiao"])

#Adicionar mais elementos
dict_uf["pais"] = "Brasil"
print(dict_uf)

#%% DataFrames
# Objetos do Pandas que guardam informações em bases de dados, colunas (variáveis) e linhas (observações)
# Função pd.DataFrame as variáveis devem ter o mesmo comprimento
# Estrutura básica de dicionário formando o objeto DataFrame

dataset_1 = pd.DataFrame({'id':["obs_1", "obs_2", "obs_3"],
                          'idade':[60, 28, 53]})
print(dataset_1)