import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'dados\dados_linhas.csv')
colunas = df.columns

plt.figure(figsize=(10, 6))
plt.plot(df[colunas[0]], df[colunas[1]], marker='o', linewidth=2, color='blue')

plt.title('Gráfico de Linhas')
plt.xlabel(colunas[0])
plt.ylabel(colunas[1])
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()

plt.show()
