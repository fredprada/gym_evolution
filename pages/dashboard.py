import streamlit as st
import plotly.express as px
import pandas as pd
from get_dados import get_dados_mongodb
import datetime

######################################################################################################################################
# Defining page properties and title, header and subheader
st.set_page_config(page_title = "Dashboard", layout="wide", page_icon = "📈")

lista_atletas = ['Fred','Mari']

col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
with col1:
    atleta = st.selectbox('Atleta:', lista_atletas)

valores = get_dados_mongodb().retrieve_data_from_mongodb()
df_valores = valores

df_valores_filtrado = df_valores[df_valores['atleta'] == atleta]

botao_puxar_dados = st.button('Ver dados da base de dados')

if botao_puxar_dados:
    st.dataframe(df_valores_filtrado)

today = datetime.datetime.now() - datetime.timedelta(hours=3)
current_week = datetime.date.isocalendar(today)[1]
df_valores_filtrado['data'] = df_valores_filtrado['data'].astype('datetime64[ns]')
df_valores_filtrado['numero_da_semana'] = df_valores_filtrado['data'].apply(lambda x: datetime.date.isocalendar(x)[1])
treinos_essa_semana = pd.DataFrame(df_valores_filtrado[['numero_da_semana']].value_counts()).reset_index()

df_current_week = df_valores_filtrado[df_valores_filtrado['numero_da_semana'] == current_week]
treinos_essa_semana = len(df_current_week)

st.metric(label="Treinos essa semana",value = treinos_essa_semana)

col1, col2 = st.columns([1, 2])
fig = px.bar(treinos_essa_semana, x="numero_da_semana", y="qtd", text="qtd")
fig.update_traces(textposition="outside")
fig.update_layout(xaxis_title="Número da semana", yaxis_title="Dias que treinou", yaxis_range=[0, 7],width=600,height=400)
fig.update_traces(marker=dict(color='#20837b'))
col1.plotly_chart(fig, theme=None, use_container_width=True)


# Treinos por semana
# Evolução da melhor série do exercício
# Calendário com dias que treinou
# Última carga
# Carga máxima
# Carga média