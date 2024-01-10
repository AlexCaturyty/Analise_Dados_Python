# %% [markdown]
# # Python Insights - Analisando Dados com Python
# 
# ### Case - Cancelamento de Clientes
# 
# Você foi contratado por uma empresa com mais de 800 mil clientes para um projeto de Dados. Recentemente a empresa percebeu que da sua base total de clientes, a maioria são clientes inativos, ou seja, que já cancelaram o serviço.
# 
# Precisando melhorar seus resultados ela quer conseguir entender os principais motivos desses cancelamentos e quais as ações mais eficientes para reduzir esse número.
# 
# Base de dados e arquivos: https://drive.google.com/drive/folders/1uDesZePdkhiraJmiyeZ-w5tfc8XsNYFZ?usp=drive_link

# %%
# Importar a base de dados
import pandas as pd

tabela = pd.read_csv("cancelamentos_sample.csv")
display(tabela)


# %%
#Corrigir os dados
tabela = tabela.drop(columns= "CustomerID")
display(tabela.info())

#remover valores vazios
tabela = tabela.dropna()
display(tabela.info())


# %%
#Fazer análise dos cancelamentos

#quantas pessoas cancelaram
tabela["cancelou"].value_counts()

#em percentual
display(tabela["cancelou"].value_counts(normalize=True).map("{:.1%}".format))


# %%
import plotly.express as px

for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color="cancelou")
    grafico.show()


# %%
#Oferecer descontos em planos anuais e trimestrais pois os cancelamentos são feitos em planos mensais
tabela = tabela[tabela["duracao_contrato"]!= "Monthly"]
#As ligações no callcenter que ultrapassam 5 vezes acarretam ao cancelamento
tabela = tabela[tabela["ligacoes_callcenter"]<=4]
#As pessoas que atrasam mais de 20 dias acabam cancelando 
tabela = tabela[tabela["dias_atraso"]<=20]

display(tabela["cancelou"].value_counts())
#porcentagem
display(tabela["cancelou"].value_counts(normalize=True).map("{:.1%}".format))

# %%
#PELOS DADOS ACIMA, VIMOS QUE APÓS ESSAS ANÁLISES, SE RESOLVERMOS OS ERROS QUE FORAM IDENTIFICADOS, A TAXA DE CANCELAMENTO IRIA CAIR DE 56% PARA 18%


