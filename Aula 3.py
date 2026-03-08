# Analisando 1 cliente
# se o cliente é bom, ok ou ruim ( pela nota de credito dele )

# passo a passo do projeto
# passo 0: enteder o desafio da empresa
# passo 1: importar a base de dados 
import pandas as pd

tabela = pd.read_csv("clientes.csv")
display(tabela)
display(tabela.info())

# int -> numero inteiros
# floats -> nuumeros com casa decimal
# str -> textos
# passo 2: tratar e preparar a base de dados para a inteligencia artificial
from sklearn.preprocessing import LabelEncoder
# textos:
# profissao -> cientista, marceneiro, pedreiro, pintor, artista, mecanico

LabelEncoder

# cientista = 1
# marceneiro = 2
# pedreiro = 3
# pintor = 4
# artista = 5
# mecanico = 6

codificador_profissao = LabelEncoder()
tabela["profissao"] = codificador_profissao.fit_transform(tabela["profissao"])
# comportamento_pagamento
codificador_comportamento = LabelEncoder()
tabela["comportamento_pagamento"] = codificador_comportamento.fit_transform(tabela["comportamento_pagamento"])
# score_credito
codificador_score = LabelEncoder()
tabela["score_credito"] = codificador_score.fit_transform(tabela["score_credito"])
# mix_credito
codificador_mix = LabelEncoder()
tabela["mix_credito"] = codificador_mix.fit_transform(tabela["mix_credito"])

display(tabela)
# como funciona criação de IA

# y -> quem eu vou prever
y = tabela["score_credito"]
# x -> quem eu vou usar pra fazer a previsao
x = tabela.drop(columns=["score_credito", "id_cliente"])

from sklearn.model_selection import train_test_split

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3)

# quero prever a coluna "score_credito"
