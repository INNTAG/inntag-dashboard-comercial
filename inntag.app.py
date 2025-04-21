
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dashboard Comercial Inntag", layout="wide")

# Carregar dados
@st.cache_data
def load_data():
    return pd.read_csv("Leads_Inntag_2025_Publicacao.csv")

df = load_data()

# Filtros laterais
st.sidebar.header("🔍 Filtros")
responsaveis = st.sidebar.multiselect("Responsável", sorted(df["Responsavel"].dropna().unique()))
cidades = st.sidebar.multiselect("Cidade", sorted(df["Cidade"].dropna().unique()))
faixas = st.sidebar.multiselect("Faixa de Consumo", sorted(df["Faixa_Consumo"].dropna().unique()))

# Aplicar filtros
if responsaveis:
    df = df[df["Responsavel"].isin(responsaveis)]
if cidades:
    df = df[df["Cidade"].isin(cidades)]
if faixas:
    df = df[df["Faixa_Consumo"].isin(faixas)]

st.title("📊 Dashboard Comercial – Inntag Energia Solar")

# Métricas principais
col1, col2, col3, col4 = st.columns(4)
col1.metric("Leads Totais", len(df))
col2.metric("Atividades Vencidas", int(df["Qtd_Atividades_Vencidas"].sum()))
col3.metric("Sem Atividade", len(df[df["Qtd_Atividades"] == 0]))
col4.metric("Consumo Médio", f'{df["Consumo_Medio"].mean():.0f} kWh')

# Gráfico de distribuição de propostas
st.subheader("📌 Distribuição de Propostas por Quantidade")
propostas = df["Qtd_Propostas"].value_counts().sort_index()
st.bar_chart(propostas)

# Exibir dados
st.subheader("📄 Tabela de Leads Filtrados")
st.dataframe(df.reset_index(drop=True))
