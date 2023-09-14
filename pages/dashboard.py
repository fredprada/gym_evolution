import streamlit as st
import plotly.express as px
import pandas as pd
from salvar_dados import salvar_dados_mongodb
from get_dados import get_dados_mongodb

######################################################################################################################################
# Defining page properties and title, header and subheader
st.set_page_config(page_title = "📈 Dashboard", layout="wide")

lista_atletas = ['Fred','Mari']

col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
with col1:
    atleta = st.selectbox('Atleta:', lista_atletas)

valores = get_dados_mongodb().retrieve_data_from_mongodb()
df_valores = valores

df_valores_filtrado = df_valores[df_valores['atleta'] == atleta]

botao_puxar_dados = st.button('Ver dados da base de dados')

if botao_puxar_dados:
    st.dataframe(df_valores)






# Treinos por semana
# Evolução da melhor série do exercício
# Calendário com dias que treinou
# Última carga
# Carga máxima
# Carga média
