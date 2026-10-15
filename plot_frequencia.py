import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r'dados\dados_frequencia.csv')
colunas_validas = [col for col in df.columns if 'id' not in col.lower()]

plt.figure(figsize=(10, 6))

if len(colunas_validas) > 0:
    col_alvo = colunas_validas[0]
    sns.countplot(data=df, x=col_alvo, order=df[col_alvo].value_counts().index, palette='pastel')
    plt.xlabel(col_alvo)
else:
    col_alvo = df.columns[0]
    sns.countplot(data=df.head(10), x=col_alvo, palette='pastel')
    plt.xlabel(f'{col_alvo} (Apenas top 10)')

plt.title('Gráfico de Frequência (Contagem)')
plt.ylabel('Quantidade')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
