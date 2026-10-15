import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'dados\dados_pizza.csv')
colunas = df.columns

plt.figure(figsize=(8, 8))
plt.pie(df[colunas[1]], labels=df[colunas[0]], autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)

plt.title('Gráfico de Pizza')
plt.tight_layout()

plt.show()
