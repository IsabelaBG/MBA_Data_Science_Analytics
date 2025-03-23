# -*- coding: utf-8 -*-
# Aula Data Wrangling

# Atividade 1

#%% Instalando pacotes

!pip install pandas
!pip install numpy
!pip install matplotlib
!pip install seaborn
!pip install xlrd

#%% Importando pacotes

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#%% Importando banco de dados

dados_tempo = pd.read_excel('base_estudantes.xls')
dados_merge = pd.read_excel('base_regioes.xls')
# base_estudantes.xls - Fonte: Fávero & Belfiore (2024, Cap. 12)

#%% Visualização básica do dataset

# Configuração para printar objetos no console
pd.set_option("display.max.columns", None)
print(dados_tempo)

# Print nome das variáveis
dados_tempo.columns

# Print primeiras n observações e nome das variáveis
dados_tempo.head(n=5)

# Print últimas n observações e nome das variáveis
dados_tempo.tail(n=5)

# Print informações detalhadas das variáveis
dados_tempo.info()

# object = variável de texto
# int ou float = variável numérica (métrica)
# category = variável categórica (qualitativa)

#%% 