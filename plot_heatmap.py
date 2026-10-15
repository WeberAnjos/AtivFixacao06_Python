import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r'dados\dados_heatmap.csv')

df_numerico = df.select_dtypes(include=['number'])

plt.figure(figsize=(10, 8))
sns.heatmap(df_numerico, annot=True, cmap='viridis', fmt='.2f')
plt.title('Mapa de Calor (Heatmap)')
plt.tight_layout()

plt.show()
