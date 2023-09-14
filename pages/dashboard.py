import streamlit as st
import plotly.express as px
import pandas as pd
from salvar_dados import salvar_dados_mongodb
from main import move_tabela_valores

######################################################################################################################################
# Defining page properties and title, header and subheader
st.set_page_config(page_title = "📈 Dashboard", layout="wide")

lista_atletas = ['Fred','Mari']

col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
with col1:
    lista_atletas = st.selectbox('Atleta:', lista_atletas)

dados_do_banco = salvar_dados_mongodb().retrieve_data_from_mongodb()

st.json(dados_do_banco)
st.table(dados_do_banco)
# Treinos por semana
# Evolução da melhor série do exercício
# Calendário com dias que treinou
# Última carga
# Carga máxima
# Carga média
