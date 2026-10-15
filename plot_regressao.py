import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r'dados\dados_regressao.csv')
colunas = df.columns

plt.figure(figsize=(10, 6))
sns.regplot(data=df, x=colunas[0], y=colunas[1], scatter_kws={'alpha':0.6}, line_kws={'color':'red'})

plt.title('Gráfico de Regressão Linear')
plt.xlabel(colunas[0])
plt.ylabel(colunas[1])
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()

plt.show()