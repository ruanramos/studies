import pandas as pd
import matplotlib

df1 = pd.DataFrame({'Ruan': [8, 9, 5.4], 'Igor': [10, 9.8, 7.8]})
df2 = pd.DataFrame(data=[['casa', 'cachorro', 'comida'], ['anaconda', 'dog', 'cat']], columns=['a', 'b', 'c'])
df3 = pd.DataFrame(data=['casa', 'cachorro', 'comida'], columns=['a'])

print(df1)
print(df2)
print(df3)

df1['Ruan'].plot()