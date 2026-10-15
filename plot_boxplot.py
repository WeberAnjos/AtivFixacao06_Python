import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r'dados\dados_boxplot.csv')

plt.figure(figsize=(10, 6))
df_numerico = df.select_dtypes(include=['number'])
sns.boxplot(data=df_numerico, palette='Set2')

plt.title('Gráfico de Boxplot')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()

plt.show()
