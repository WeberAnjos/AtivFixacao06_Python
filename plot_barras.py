import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r'dados\dados_barras.csv')

plt.figure(figsize=(10, 6))

colunas_numericas = df.select_dtypes(include=['number']).columns

if len(colunas_numericas) > 0:
    col_y = colunas_numericas[0]
    hue_col = 'regiao' if 'regiao' in df.columns else None
    sns.barplot(data=df, x='categoria', y=col_y, hue=hue_col, palette='Blues_d')
    plt.ylabel(col_y)
else:
    sns.countplot(data=df, x='categoria', hue='regiao' if 'regiao' in df.columns else None, palette='Blues_d')
    plt.ylabel('Quantidade (Contagem)')

plt.title('Gráfico de Barras')
plt.xlabel('Categoria')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()

plt.show()
