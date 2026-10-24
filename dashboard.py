import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout="wide", page_title="Dashboard - Atividade 06")

with st.sidebar:
    st.header("👤 Informações do Aluno")
    st.markdown("**Nome:** Seu Nome Completo")
    st.markdown("**Número da Chamada:** 00")
    st.markdown("**Turma:** Sua Turma (Ex: 3º Ano A)")
    st.markdown("---")
    st.caption("Desenvolvido para a Atividade 06.")

st.title("📊 Dashboard de Visualização de Dados — Atividade 06")
st.markdown("Abaixo estão dispostos os gráficos gerados a partir dos conjuntos de dados fornecidos, acompanhados de suas respectivas análises preliminares.")
st.markdown("---")


col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("1. Gráfico de Linhas")
    try:
        df_linhas = pd.read_csv(r'dados\dados_linhas.csv')
        colunas = df_linhas.columns
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(df_linhas[colunas[0]], df_linhas[colunas[1]], marker='o', linewidth=2, color='blue')
        ax.set_title('Gráfico de Linhas')
        ax.set_xlabel(colunas[0])
        ax.set_ylabel(colunas[1])
        ax.grid(True, linestyle='--', alpha=0.5)
        plt.tight_layout()
        st.pyplot(fig)
        st.info("**Análise:** Ideal para identificar tendências, evoluções ou comportamentos de variáveis ao longo de um eixo contínuo (geralmente temporal).")
    except Exception as e:
        st.error(f"Erro ao carregar dados_linhas.csv: {e}")

with col2:
    st.subheader("2. Gráfico de Barras")
    try:
        df_barras = pd.read_csv(r'dados\dados_barras.csv')
        fig, ax = plt.subplots(figsize=(6, 4))
        colunas_numericas = df_barras.select_dtypes(include=['number']).columns
        
        if len(colunas_numericas) > 0:
            col_y = colunas_numericas[0]
            hue_col = 'regiao' if 'regiao' in df_barras.columns else None
            sns.barplot(data=df_barras, x='categoria', y=col_y, hue=hue_col, palette='Blues_d', ax=ax)
            ax.set_ylabel(col_y)
        else:
            sns.countplot(data=df_barras, x='categoria', hue='regiao' if 'regiao' in df_barras.columns else None, palette='Blues_d', ax=ax)
            ax.set_ylabel('Quantidade (Contagem)')
            
        ax.set_title('Gráfico de Barras')
        ax.set_xlabel('Categoria')
        plt.xticks(rotation=45)
        ax.grid(axis='y', linestyle='--', alpha=0.5)
        plt.tight_layout()
        st.pyplot(fig)
        st.info("**Análise:** Permite comparar volumes ou frequências entre categorias discretas de forma visual direta, facilitando a identificação do maior/menor elemento.")
    except Exception as e:
        st.error(f"Erro ao carregar dados_barras.csv: {e}")

with col3:
    st.subheader("3. Gráfico de Boxplot")
    try:
        df_boxplot = pd.read_csv(r'dados\dados_boxplot.csv')
        fig, ax = plt.subplots(figsize=(6, 4))
        df_numerico = df_boxplot.select_dtypes(include=['number'])
        sns.boxplot(data=df_numerico, palette='Set2', ax=ax)
        ax.set_title('Gráfico de Boxplot')
        ax.grid(axis='y', linestyle='--', alpha=0.5)
        plt.tight_layout()
        st.pyplot(fig)
        st.info("**Análise:** Excelente para avaliar a distribuição estatística dos dados, destacando a mediana, os quartetos e a presença de possíveis valores discrepantes (*outliers*).")
    except Exception as e:
        st.error(f"Erro ao carregar dados_boxplot.csv: {e}")

st.markdown("---")


col4, col5, col6 = st.columns(3)

with col4:
    st.subheader("4. Gráfico de Dispersão")
    try:
        df_dispersao = pd.read_csv(r'dados\dados_dispersao.csv')
        colunas = df_dispersao.columns
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.scatter(df_dispersao[colunas[0]], df_dispersao[colunas[1]], color='purple', alpha=0.7, edgecolors='black')
        ax.set_title('Gráfico de Dispersão')
        ax.set_xlabel(colunas[0])
        ax.set_ylabel(colunas[1])
        ax.grid(True, linestyle='--', alpha=0.5)
        plt.tight_layout()
        st.pyplot(fig)
        st.info("**Análise:** Utilizado para mapear a relação ou correlação visual entre duas variáveis numéricas independentes, expondo agrupamentos ou dispersões.")
    except Exception as e:
        st.error(f"Erro ao carregar dados_dispersao.csv: {e}")

with col5:
    st.subheader("5. Gráfico de Distribuição")
    try:
        df_dist = pd.read_csv(r'dados\dados_distribuicao.csv')
        colunas = df_dist.columns
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.histplot(df_dist[colunas[0]], kde=True, color='teal', ax=ax)
        ax.set_title('Gráfico de Distribuição')
        ax.set_xlabel(colunas[0])
        ax.set_ylabel('Frequência')
        ax.grid(axis='y', linestyle='--', alpha=0.5)
        plt.tight_layout()
        st.pyplot(fig)
        st.info("**Análise:** Revela a densidade e o formato de frequência de uma variável, permitindo entender se os dados seguem uma distribuição normal ou assimétrica.")
    except Exception as e:
        st.error(f"Erro ao carregar dados_distribuicao.csv: {e}")

with col6:
    st.subheader("6. Gráfico de Frequência")
    try:
        df_freq = pd.read_csv(r'dados\dados_frequencia.csv')
        colunas_validas = [col for col in df_freq.columns if 'id' not in col.lower()]
        fig, ax = plt.subplots(figsize=(6, 4))
        
        if len(colunas_validas) > 0:
            col_alvo = colunas_validas[0]
            sns.countplot(data=df_freq, x=col_alvo, order=df_freq[col_alvo].value_counts().index, palette='pastel', ax=ax)
            ax.set_xlabel(col_alvo)
        else:
            col_alvo = df_freq.columns[0]
            sns.countplot(data=df_freq.head(10), x=col_alvo, palette='pastel', ax=ax)
            ax.set_xlabel(f'{col_alvo} (Apenas top 10)')
            
        ax.set_title('Gráfico de Frequência (Contagem)')
        ax.set_ylabel('Quantidade')
        ax.grid(axis='y', linestyle='--', alpha=0.5)
        plt.xticks(rotation=45)
        plt.tight_layout()
        st.pyplot(fig)
        st.info("**Análise:** Demonstra a contagem absoluta de ocorrências de classes nominais/categóricas ordenadas da maior para a menor recorrência.")
    except Exception as e:
        st.error(f"Erro ao carregar dados_frequencia.csv: {e}")

st.markdown("---")


col7, col8, col9 = st.columns(3)

with col7:
    st.subheader("7. Mapa de Calor (Heatmap)")
    try:
        df_heatmap = pd.read_csv(r'dados\dados_heatmap.csv')
        df_numerico = df_heatmap.select_dtypes(include=['number'])
        fig, ax = plt.subplots(figsize=(6, 5))
        sns.heatmap(df_numerico, annot=True, cmap='viridis', fmt='.2f', ax=ax)
        ax.set_title('Mapa de Calor (Heatmap)')
        plt.tight_layout()
        st.pyplot(fig)
        st.info("**Análise:** Permite analisar a intensidade das relações (como matrizes de correlação) por meio de gradientes de cor e anotações numéricas diretas.")
    except Exception as e:
        st.error(f"Erro ao carregar dados_heatmap.csv: {e}")

with col8:
    st.subheader("8. Gráfico de Pizza")
    try:
        df_pizza = pd.read_csv(r'dados\dados_pizza.csv')
        colunas = df_pizza.columns
        fig, ax = plt.subplots(figsize=(5, 5))
        ax.pie(df_pizza[colunas[1]], labels=df_pizza[colunas[0]], autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
        ax.set_title('Gráfico de Pizza')
        plt.tight_layout()
        st.pyplot(fig)
        st.info("**Análise:** Mostra a proporção e a composição percentual de partes em relação a um todo. Recomendado para poucas categorias de comparação.")
    except Exception as e:
        st.error(f"Erro ao carregar dados_pizza.csv: {e}")

with col9:
    st.subheader("9. Gráfico de Regressão")
    try:
        df_reg = pd.read_csv(r'dados\dados_regressao.csv')
        colunas = df_reg.columns
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.regplot(data=df_reg, x=colunas[0], y=colunas[1], scatter_kws={'alpha':0.6}, line_kws={'color':'red'}, ax=ax)
        ax.set_title('Gráfico de Regressão Linear')
        ax.set_xlabel(colunas[0])
        ax.set_ylabel(colunas[1])
        ax.grid(True, linestyle='--', alpha=0.5)
        plt.tight_layout()
        st.pyplot(fig)
        st.info("**Análise:** Além da dispersão, traça uma reta estimada para prever comportamentos ou indicar a força e direção de uma tendência linear contínua.")
    except Exception as e:
        st.error(f"Erro ao carregar dados_regressao.csv: {e}")
