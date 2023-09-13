import streamlit as st
import datetime
from datetime import timedelta
from exercicio import Exercicio
from serie import Serie
from salvar_dados import salvar_dados_mongodb
from pymongo import MongoClient
import os
import itertools

st.set_page_config(page_title = "Evolução academia", page_icon = "💪")

hora_atual = datetime.datetime.now() - timedelta(hours=3)
lista_treinos = ['1- PEITO | OMBRO | TRÍCEPS', 
                 '2- COSTAS | BÍCEPS',
                 '3- PERNA']
lista_marombas = ['Fred','Mari']

col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
with col1:
    treino_selecionado = st.selectbox('Escolha o treino do dia:', (lista_treinos))
with col2:
    maromba = st.selectbox('Quem ta treinando?', (lista_marombas))
with col3:
    data = st.date_input('Data', value=hora_atual, format="DD/MM/YYYY",)
with col4:
    exercicio_num = st.selectbox("Qtd de exercícios", ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

st.markdown("""---""")

lista_exercicio = Exercicio(treino_selecionado).get_exercicio()

valores = {}

for num in range(1, exercicio_num + 1):
    col1, col2, col3, col4 = st.columns([3, 1, 1, 1])
    with col1:
        select_exercicio = st.selectbox(f'Exercício ({num}): ', (lista_exercicio))
        qtd_series_exercicio = st.selectbox("Número de séries diferentes:", ([1, 2, 3, 4, 5]), key=f"series_dif_{num}")
        valores[f'select_exercicio{num}'] = select_exercicio
        valores[f'qtd_series_exercicio_{num}'] = qtd_series_exercicio

    series_values = []
    reps_values = []
    carga_values = []

    for serie_num in range(1, qtd_series_exercicio + 1):
        with col2:
            series = st.number_input(f'Séries {serie_num}: ', min_value=0, max_value=10, key=f'series_{num}_{serie_num}')
            series_values.append(series)
        with col3:
            reps = st.number_input(f'Núm Reps {serie_num}: ', min_value=0, max_value=50, key=f'reps_{num}_{serie_num}')
            reps_values.append(reps)
        with col4:
            carga = st.number_input(f'Carga {serie_num}: ', min_value=0, max_value=10000, key=f'carga_{num}_{serie_num}')
            carga_values.append(carga)

    valores[f'series_exercicio_{num}'] = series_values
    valores[f'reps_exercicio_{num}'] = reps_values
    valores[f'carga_exercicio_{num}'] = carga_values
    st.markdown("""---""")

botao_salvar = st.button('Salvar')
botao_ver_dados = st.button('Ver tabela com dados do banco')

if botao_salvar:
    salvar_dados_mongodb([valores]).database_insertion()

if botao_ver_dados:
    st.sidebar.text(valores)
    st.sidebar.table(valores)
    st.sidebar.dataframe(valores)