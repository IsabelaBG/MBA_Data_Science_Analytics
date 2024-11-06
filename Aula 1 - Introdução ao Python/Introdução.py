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

# Criação
dict_uf = {"estado": "SP",
           "regiao": "Sudeste"}

print(dict_uf["estado"])
print(dict_uf["regiao"])

# Adicionar mais elementos
dict_uf["pais"] = "Brasil"
print(dict_uf)

#%% DataFrames
# Objetos do Pandas que guardam informações em bases de dados, colunas (variáveis) e linhas (observações)
# Função pd.DataFrame as variáveis devem ter o mesmo comprimento
# Estrutura básica de dicionário formando o objeto DataFrame

dataset_1 = pd.DataFrame({'id':["obs_1", "obs_2", "obs_3"],
                          'idade':[60, 28, 53]})
print(dataset_1)

# Criando variáveis
# Argumento None, não é texto, é um missing value (NA)
varA = np.arange(1,11)
varB = pd.Series([1,2,3,4,5,6,7,8,None,None])
varC = pd.Series(["a","b","c","d","e","f","g","h","i","j"])

print(varA)
print(varB)
print(varC)

# Criando banco de dados
dataset_2 =  pd.DataFrame({'varA': varA,
                           'varB' : varB,
                           'varC' : varC})
print(dataset_2)  

#%% Importando dados

# Excel
# Receita anual de vendas para 5 empresas ao longo de 6 anos (Fonte: CVM)
receita = pd.read_excel("base_receita_empresas.xlsx")

# CSV
# Dados da OCDE sobre as notas dos países no PISA. Fonte: https://pisadataexplorer.oecd.org/ide/idepisa/dataset.aspx
# Argumentos adicionais da função: separador (,) e a indicação de decimais (.)
notas = pd.read_csv("base_notas_pisa.csv", sep=",", decimal=".")

# Link
# Dados da variação mensal do IPCA
ipca = pd.read_csv("https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=csv&dataInicial=01/01/2022&dataFinal=30/09/2024",
                   sep=";", decimal=",")

#%% Exportando dados
# É possível fazer alterações no dataset e salvar
# CSV - removando index
dataset_1.to_csv("dataset1.csv", index=False)
# Excel - removendo index
dataset_2.to_excel("dataset2.xlsx", index=False)

#%% Funções
# Funções e iterações automatizam tarefas repetitivase podem facilitar a escrita do código
# Para criar uma função, existem três etapas básicas:
# 1. Nomear a função
# 2. Indicar os argumentos (inputs) que são utilizados na função
# 3. Indicar o código que será implementado dentro do corpo da função
# Função com input único
def converter(milha):
    km = (milha * 1.6093)
    return km
print(converter(60))
print(converter(100))
print(converter(20))
print(converter(30))

# Utilizando série com input
valores_converter = pd.Series([10,15,10,35])
print(converter(valores_converter))

# Função com dois inputs
def calcular_area(b, h):
  area = (b * h)
  return area

print(f"{calcular_area(10, 10)}m²")
print(f"{calcular_area(20, 15)}m²")
print(f"{calcular_area(50, 30)}m²")

#%% Condições
# Neste contexto de funções, as condições "if, elif e else" são importantes
# IF
valor = 100

if valor == 10**2:
    print("Valor Correto")
else:
    print("Valor incorreto")  

#ELIF
salario = 3500

if salario <= 1412:
  print("Até 1 salário mínimo")
elif salario > 1412 and salario <= 4236:
  print("Entre de 1 e 3 salários mínimos")
elif salario > 4236 and salario <= 7060:
  print("Entre 3 e 5 salários mínimos")
else:
  print("Mais de 5 salários mínimos")

# Adicionando condição em função
def quantidade_salarios(salario):
    
    quantidade = (salario/1412)
    
    if quantidade <= 10:
        return quantidade
    else:
        return("Mais de 10 salários mínimos")

print(quantidade_salarios(1412))
print(quantidade_salarios(3000))
print(quantidade_salarios(14120))
print(quantidade_salarios(15000))

# Vários inputs e múltiplas condições
def nova_area(b, h):
    
    calculo_area = (b * h) # inserir b e h em metros
    
    if calculo_area <= 10000:
        return calculo_area, "Até 1 hectare"
    elif calculo_area > 10000 and calculo_area <= 50000:
        return calculo_area, "Entre 1 e 5 hectares"
    else:
        return calculo_area, "Mais de 5 hectares"
    
print(nova_area(300, 25))
print(nova_area(200,100))
print(nova_area(500, 300))

# Integrando funções existentes
def coef_var(x):
  coeficiente = (np.std(x) / np.mean(x)) * 100
  return np.round(coeficiente, decimals=3)

variavel_cv = pd.Series([10, 25, 40, 35, 15, 28, 31])
print(f"{coef_var(variavel_cv)}%")

# FOR
lista_conversao = pd.Series([60, 100, 20, 30])
lista_km = []

for i in lista_conversao:
    lista_km.append(i * 1.6093)

print(lista_km)

# WHILE
saldo_investimento = 100
lista_invest = []

while saldo_investimento < 10000:
    saldo_investimento = (saldo_investimento*1.10)
    lista_invest.append(saldo_investimento)

print(lista_invest)

lista_invest.insert(0, 100)

print(lista_invest)

#%% Conceitos básicos de manipulação de dados
# Visualizando as primeiras 5 linhas da base importada anteriormente
print(notas.head(5))

# Variáveis disponíveis
print(notas.columns)

# Informações detalhadas do banco de dados
print(notas.info())

# Linhas / observações do banco de dados
print(notas.shape[0])

# Colunas / variáveis do banco de dados
print(notas.shape[1])

# Observações e variávies
# Linhas / observações do banco de dados
print(notas.shape)

# Seleção de variáveis
print(notas['country'])
paises = print(notas['country'])
paises_2018 = print(notas[['country','reading_2018']])

# Remoção de variáveis
notas_2022 = notas.drop(columns=['mathematics_2018', 'reading_2018', 'science_2018'])

# O argumento inplace=True pode ser usado para reescrever o objeto existente
notas_2022.drop(columns=['group'], inplace=True)

# Remover objeto do ambiente
del paises_2018

# Elementos específicos por posição
# O primeiro argumento é o número da linha (index), o segundo é a posição da coluna

# Nota de matemática em 2022 para o Brasil
print(notas.iloc[46,2])

# Todos os valores de todas as variáveis para o Japão
print(notas.iloc[19,])

# Valores de todas as variáveis para os países de index de 0 a 6
print(notas.iloc[0:7, ])

# Variáveis que estão nas posições 0, 2 e 5
notas_matematica = notas.iloc[:, [0,2,5]]

# Selecionar as variáveis que estão nas posições de 0 até 2
notas_matematica = notas.iloc[:, 0:3]

# Reorganizando variáveis
notas_2022_ajuste = notas.reindex(['group','country','science_2022','mathematics_2022','reading_2022'],axis = 1)

# Excluindo informações com base no index
notas_OCDE = notas.drop(notas.index[38:96])

#%% Detalhando manipulações de bancos de dados
# Em casos de variáveis numéricas estiverem como textos ou "object", fazer ajuste
# Ajuste utilizando a função "to_numeric", missings serão ajustados pelo coerce e substituídos por nan
notas['mathematics_2022'] = pd.to_numeric(notas['mathematics_2022'], errors='coerce')
notas['reading_2022'] = pd.to_numeric(notas['reading_2022'], errors='coerce')
notas['science_2022'] = pd.to_numeric(notas['science_2022'], errors='coerce')
notas['mathematics_2018'] = pd.to_numeric(notas['mathematics_2018'], errors='coerce')
notas['reading_2018'] = pd.to_numeric(notas['reading_2018'], errors='coerce')
notas['science_2018'] = pd.to_numeric(notas['science_2018'], errors='coerce')
print(notas.info())

# Excluindo linhas com dados faltantes
notas_na= notas.dropna()

# Estatísticas descritivas
notas[['mathematics_2022', 'reading_2022', 'science_2022']].describe()

# Tabela de frequências para variáveis qualitativas
notas['group'].value_counts()

#%% Operadores
# Alguns operadores úteis para realizar filtros:
# "== igual"
# "> maior"
# ">= maior ou igual"
# "< menor"
# "<= menor ou igual"
# "!= diferente"
# "& indica e"
# "| indica ou"

# Nota de matemática em 2022 maior que 437
print(notas[notas['mathematics_2022'] > 437])

# Somente grupo OECD
print(notas[notas['group'] == 'OECD'])

# Grupo OECD e nta menor ou igual a 493
print(notas[(notas['group'] == 'OECD') & (notas['science_2022'] <= 493)])

# Países que não sejam OECD
print(notas[notas['group'] != 'OECD'])

# Nota menor do que 386 ou maior do que 480
print(notas[(notas['reading_2022'] < 386) | (notas['reading_2022'] > 480)])

#%% Agrupamento

notas_grupo = notas.groupby(by=['group'])
notas_grupo.describe().T # o comando .T apenas fez a transposição da tabela

#%% Ordenação

# Ordem decrescente
desc_math = notas.sort_values(by=['mathematics_2022'], ascending=False)

# Ordem crescente
asc_math = notas.sort_values(by=['mathematics_2022'], ascending=True)

#%% Alterar nomes de variáveis

nomes = ["pais",
         "grupo",
         "matematica_2022",
         "leitura_2022",
         "ciencias_2022",
         "matematica_2018",
         "leitura_2018",
         "ciencias_2018"]

notas.columns = nomes

print(notas.info())

# Trocar apenas um nome:
notas = notas.rename(columns={'grupo':'grupo_paises'})

print(notas.info())