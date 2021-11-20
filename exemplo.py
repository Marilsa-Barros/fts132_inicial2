# Passo 1: importar base de dados
import pandas as pd
from Tools.scripts.dutree import display

tabela = pd.read_csv("telecom_users.csv")

# Passo 2: visualizar a base de dados
tabela = tabela.drop("Unnamed: 0", axis=1)
tabela = tabela.drop("IDCliente", axis=1)
display(tabela)
# - entender quais as informações estão disponiveis
# - discubrir as cagadas da base de dados

# Passo 3: tratamento de dados
# - valores que estão sendo desconhecios de forma errada
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")
# - valores vazios
# - deletar as colunas vazias
tabela = tabela.dropna(how="all", axis=1)
# - deletar as linhas vazias
tabela = tabela.dropna(how="any", axis=0)

print(tabela.info())

# Passo 4: análise inicial
# como estão os nossos cancelamentos?
print(tabela["Churn"].value_counts())
print(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format))
