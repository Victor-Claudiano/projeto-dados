import streamlit as st
import pandas as pd
import plotly.express as px

# Título
st.title("📊 Dashboard de Gastos Pessoais")

# Upload do CSV
st.sidebar.header("Importar CSV")
uploaded_file = st.sidebar.file_uploader("Escolha o arquivo", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file, parse_dates=['data'])
else:
    # Dados de exemplo
    df = pd.read_csv("dados/gastos.csv", parse_dates=['data'])

# Preprocessamento
df['mes'] = df['data'].dt.to_period('M').astype(str)

# Filtros
st.sidebar.header("Filtros")
meses = sorted(df['mes'].unique())
categorias = sorted(df['categoria'].unique())

mes_selecionado = st.sidebar.multiselect("Mês", meses, default=meses)
cat_selecionada = st.sidebar.multiselect("Categoria", categorias, default=categorias)

df_filtrado = df[(df['mes'].isin(mes_selecionado)) & (df['categoria'].isin(cat_selecionada))]

# KPIs
valor_total = df_filtrado['valor'].sum()
valor_formatado = f"R$ {valor_total:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
st.metric("Total gasto", valor_formatado)

# Gráfico de linha - evolução dos gastos
st.subheader("Evolução dos Gastos")
linha = df_filtrado.groupby('mes')['valor'].sum().reset_index()
fig_linha = px.line(linha, x='mes', y='valor', markers=True, title="Total por Mês")
st.plotly_chart(fig_linha, use_container_width=True)

# Gráfico de pizza - distribuição por categoria
st.subheader("Distribuição por Categoria")
pizza = df_filtrado.groupby('categoria')['valor'].sum().reset_index()
fig_pizza = px.pie(pizza, names='categoria', values='valor', title="Gastos por Categoria")
st.plotly_chart(fig_pizza, use_container_width=True)

# Tabela
st.subheader("Tabela de Gastos")
st.dataframe(df_filtrado.sort_values(by="data", ascending=False))

