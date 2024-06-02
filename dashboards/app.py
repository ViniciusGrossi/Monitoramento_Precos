import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import sqlite3

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('data/quotes.db')

# Carregar os dados da tabela 'mercadolivre_items' em um DataFrame pandas
df = pd.read_sql_query("SELECT * FROM mercadolivre_items", conn)

# Fechar a conexão com o banco de dados
conn.close()

def filtrar_avaliacoes_zeradas(df):
    return df[df['reviews_rating_number'] > 0]
#FILTROS
# Sidebar com filtros
st.sidebar.header('Vinicius Grossi')
st.sidebar.header('Filtros')

incluir_zeradas = st.sidebar.checkbox('Incluir avaliações zeradas', value=True)
if not incluir_zeradas:
    df = filtrar_avaliacoes_zeradas(df)
# Filtro por Faixa de Preço
min_price, max_price = st.sidebar.slider('Selecione a faixa de preço', float(df['price'].min()), float(df['price'].max()), (float(df['price'].min()), float(df['price'].max())))
df = df[(df['price'] >= min_price) & (df['price'] <= max_price)]
#Filtro por Marca
show_brands_filter = st.sidebar.checkbox('Filtrar por Marcas')
if show_brands_filter:
    selected_brands = st.sidebar.multiselect('Selecione as marcas', df['brand'].unique(),['OLYMPIKUS','FILA', 'MIZUNO','NEW BALANCE','ASICS'])
    df = df[df['brand'].isin(selected_brands)]
# Filtro por Avaliação
min_rating, max_rating = st.sidebar.slider('Selecione a faixa de avaliações', float(df['reviews_rating_number'].min() > 0), float(df['reviews_rating_number'].max()), (float(df['reviews_rating_number'].min()), float(df['reviews_rating_number'].max())))
df = df[(df['reviews_rating_number'] >= min_rating) & (df['reviews_rating_number'] <= max_rating)]


st.title('Pesquisa de Mercado - Tênis Esportivos no Mercado Livre')
# Melhorar o layout com colunas para KPIs
st.subheader("KPIs Principais")
col1, col2, col3 = st.columns(3)

# KPI 1: Número total de itens
total_items = df.shape[0]
col1.metric(label="Número Total de Itens", value=total_items)

# KPI 2: Número de marcas únicas
unique_brands = df['brand'].nunique()
col2.metric(label="Número de Marcas Únicas", value=unique_brands)

# KPI 3: Preço médio novo (em reais)
average_price = df['price'].mean()
col3.metric(label="Preço Médio Novo (R$)", value=f"{average_price:.2f}")

tab1, tab2, tab3 = st.tabs(['Preços', 'Marcas', 'Avaliações'])
with tab1:
    # Qual o preço médio por marca
    st.subheader('Preço médio por marca')
    col1, col2 = st.columns([4, 2])
    average_price_by_brand = df.groupby('brand')['price'].mean().sort_values(ascending=False)
    col1.bar_chart(average_price_by_brand)
    col2.write(average_price_by_brand)

    # Análise de Distribuição de Preços
    col1, col2 = st.columns([4, 2])
    st.subheader('Distribuição de Preços')
    fig = px.histogram(df['price'].dropna(), nbins=30, labels={'value':'Preço (R$)'}, title='Histograma de Preços')
    col1.plotly_chart(fig)

    st.subheader('Boxplot de Preços')
    col1, col2 = st.columns([8, 2])
    fig = px.box(df['price'].dropna(), labels={'value':'Preço (R$)'}, title='Boxplot de Preços')
    st.plotly_chart(fig)
    st.write(df['price'].describe())

    # Correlação entre Preço e Avaliações
    st.subheader('Correlação entre Preço e Avaliações')
    correlation = df[['price', 'reviews_rating_number']].corr().iloc[0, 1]
    st.write(f"A correlação entre preço e nota das avaliações é: {correlation:.2f}")
    fig = px.scatter(df, x='price', y='reviews_rating_number', labels={'price':'Preço (R$)', 'reviews_rating_number':'Nota das Avaliações'})
    st.plotly_chart(fig)

    # Identificação de Outliers
    st.subheader('Identificação de Outliers')
    col1, col2 = st.columns([4, 2])
    fig = px.box(df, x='price', points='all', labels={'x':'Preço (R$)'}, title='Outliers no Preço')
    col1.plotly_chart(fig)
    col2.write(df[df['price'] > df['price'].quantile(0.99)][['brand', 'price']])

with tab2:
    st.subheader('Preço médio por marca')
    col1, col2 = st.columns([4, 2])
    average_price_by_brand = df.groupby('brand')['price'].mean().sort_values(ascending=False)
    col1.bar_chart(average_price_by_brand)
    col2.write(average_price_by_brand)

    # Quais marcas são mais encontradas até a 50ª página
    st.subheader('Marcas mais encontradas até a 50ª página')
    col1, col2 = st.columns([4, 2])
    top_50_pages_brands = df['brand'].value_counts().sort_values(ascending=False)
    col1.bar_chart(top_50_pages_brands.head(20))
    col2.write(top_50_pages_brands)

    # Qual a satisfação por marca
    st.subheader('Satisfação por marca')
    col1, col2 = st.columns([4, 2])
    satisfaction_by_brand = df.groupby('brand')['reviews_rating_number'].mean().sort_values(ascending=False)
    col1.bar_chart(satisfaction_by_brand.head(20))
    col2.write(satisfaction_by_brand)
    
    # Correlação entre Marcas e Avaliações
    st.subheader('Correlação entre Marca e Avaliações')
    average_rating_by_brand = df.groupby('brand')['reviews_rating_number'].mean()
    correlation = average_rating_by_brand.corr(df.groupby('brand')['price'].mean())
    st.write(f"A correlação entre preço e nota das avaliações é: {correlation:.2f}")
    fig = px.scatter(df, x='brand', y='reviews_rating_number', labels={'brand':'Marca', 'reviews_rating_number':'Nota das Avaliações'})
    st.plotly_chart(fig)

with tab3:
    # Análise de Avaliações
    st.subheader('Distribuição de Avaliações')
    fig = px.histogram(df['reviews_rating_number'].dropna(), nbins=30, labels={'value':'Número de Avaliações'}, title='Histograma de Avaliações')
    st.plotly_chart(fig)

    fig = px.box(df['reviews_rating_number'].dropna(), labels={'value':'Número de Avaliações'}, title='Boxplot de Avaliações')
    st.plotly_chart(fig)
    st.write(df['reviews_rating_number'].describe())

    # Identificação de Outliers
    fig = px.box(df, x='reviews_rating_number', points='all', labels={'x':'Número de Avaliações'}, title='Outliers nas Avaliações')
    st.plotly_chart(fig)
   