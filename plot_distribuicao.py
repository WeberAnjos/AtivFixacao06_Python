import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r'dados\dados_distribuicao.csv')
colunas = df.columns

plt.figure(figsize=(10, 6))
sns.histplot(df[colunas[0]], kde=True, color='teal')

plt.title('Gráfico de Distribuição')
plt.xlabel(colunas[0])
plt.ylabel('Frequência')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()

plt.show()
