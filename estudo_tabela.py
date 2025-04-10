import pandas

tabela = pandas.read_csv('produtos.csv')
print(tabela)

# tabela.index -> linha da tabela
# tabela.columns -> coluna da tabela
# tabela.loc[linha,coluna] -> para localizar uma info na tabela
# NaN -> Not a Number -> Vazio