import streamlit as st
import datetime
from datetime import timedelta
from exercicio import Exercicio
from serie import Serie

st.title('Evolução de Treino')

hora_atual = datetime.datetime.now() - timedelta(hours=3)
lista_treinos = ['1- PEITO | OMBRO | TRÍCEPS', 
                 '2- COSTAS | BÍCEPS',
                 '3- PERNA']

col1, col2 = st.columns([2, 1])
with col1:
    treino_selecionado = st.selectbox('Escolha o treino do dia:', (lista_treinos))
with col2:
    data = st.date_input('Data', value=hora_atual)

exercicio_1 = Exercicio(treino_selecionado).get_exercicio()
# exercicio_2 = escolha_exercicios(treino_selecionado)
# exercicio_3 = escolha_exercicios(treino_selecionado)
# exercicio_4 = escolha_exercicios(treino_selecionado)
# exercicio_5 = escolha_exercicios(treino_selecionado)

col1, col2, col3, col4 = st.columns([3,1,1,1])
with col1:
    select_exercicio_1 = st.selectbox('Exercício 1: ', (exercicio_1))
    qtd_series_exercicio_1 = st.selectbox('Número de séries diferentes: ', ([1, 2, 3, 4, 5]))
with col2:
    series_exercicio_1 = st.number_input('Séries 1: ', min_value = 0, max_value = 10)
    Serie(qtd_series_exercicio_1).get_series()
with col3:
    reps_exercicio_1 = st.number_input('Núm Reps 1: ', min_value = 0, max_value = 50)
    Serie(qtd_series_exercicio_1).get_reps()
with col4:
    carga_exercicio_1 = st.number_input('Carga 1: ', min_value = 0, max_value = 10000)
    Serie(qtd_series_exercicio_1).get_cargas()

st.button('Salvar')