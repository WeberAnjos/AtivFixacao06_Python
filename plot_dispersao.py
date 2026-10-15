import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'dados\dados_dispersao.csv')
colunas = df.columns

plt.figure(figsize=(10, 6))
plt.scatter(df[colunas[0]], df[colunas[1]], color='purple', alpha=0.7, edgecolors='black')

plt.title('Gráfico de Dispersão')
plt.xlabel(colunas[0])
plt.ylabel(colunas[1])
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()

plt.show()
