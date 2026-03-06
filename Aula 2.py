# passo a passo do projeto:
# passo 1: importar base de dados
import pandas as pd

tabela = pd.read_csv("cancelamentos.csv")
# passo 2: visualizar base de dados 
# (entender as informações disponiveis/problemas e erros)
tabela = tabela.drop(columns="CustomerID")
display(tabela)
# passo 3: corrigir os erros na base de dados
display(tabela.info())
# valores em formatos errados 

# informações vazias
tabela = tabela.dropna()
display(tabela.info())
# passo 4: analise inicial (entender quantos clientes cancelaram)

# quantidade - contar quantos sao 00 e quantos sao 01 
display(tabela["cancelou"].value_counts())
display(tabela["duracao_contrato"].value_counts())

# porcentagem
display(tabela["cancelou"].value_counts(normalize=True))
# display(tabela["cancelou"].value_counts(normalize=True).map("{:.1%}".format))
# passo 5: analise detalhada (causa do cancelamento dos clientes)
import plotly.express as px
print(tabela.columns)
for coluna in tabela.columns:
    # cria o grafico
    grafico = px.histogram(tabela, x=coluna, color="cancelou", text_auto=True)
    # exibe o grafico criado
    grafico.show()
# todo mundo do contrato mensal cancelou o serviço
    # vamo dar um desconto no contrato anual, trimestral

# todo mundo que ligou mais de 4 vezes cancelou em seguida
    # tem alguma problema que nao conseguimkos resolver
    # se o cliente ligar 3x pro callcenter, alerta vermelho

# atraso no pagamento acima de 20 dias, o cliente cancela
    # se o cliente atrasar 15 dias no pagamento, alerta vermelho

# cancelamento = 18%

# filtrar a base de dados:

# duracao_contrato -> diferentes de Monthly
condicao = tabela["duracao_contrato"] != "Monthly"
tabela = tabela[condicao]

# ligacoes callcenter -> menores ou iguais a 4
condicao = tabela["ligacoes_callcenter"] <= 4
tabela = tabela[condicao]

# dias_atraso -> menores ou iguais a 20
condicao = tabela["dias_atraso"] <= 20
tabela = tabela[condicao]

# porcentagem
display(tabela["cancelou"].value_counts(normalize=True))

Tudo em modelo ipynb!!!!!
