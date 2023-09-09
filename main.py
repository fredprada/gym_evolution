import streamlit as st
import datetime
from datetime import timedelta
from exercicio import Exercicio
from serie import Serie
from exercicio_realizado import ExercicioRealizado

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

exercicio_num = 0
exercicio_1 = Exercicio(treino_selecionado).get_exercicio()

col1, col2, col3, col4 = st.columns([3,1,1,1])
with col1:
    select_exercicio_1 = st.selectbox('Exercício 1: ', (exercicio_1))
    qtd_series_exercicio_1 = st.selectbox('Número de séries diferentes: ', ([1, 2, 3, 4, 5]))
with col2:
    series_exercicio_1 = st.number_input('Séries 1: ', min_value = 0, max_value = 10)
with col3:
    reps_exercicio_1 = st.number_input('Núm Reps 1: ', min_value = 0, max_value = 50)
with col4:
    carga_exercicio_1 = st.number_input('Carga 1: ', min_value = 0, max_value = 10000)

if st.button('Adicionar exercício'):
    exercicio_num += 1

exec(f'exercicio{exercicio_num} = ExercicioRealizado({exercicio_num})')

col1, col2, col3, col4 = st.columns([3,1,1,1])
with col1:
    exec(f'select_exercicio{exercicio_num} = st.selectbox("Exercício {exercicio_num}: ", (exercicio_{exercicio_num}))')
    exec(f'qtd_series_exercicio_{exercicio_num} = st.selectbox("Número de séries diferentes: ", ([1, 2, 3, 4, 5]))')
with col2:
    exec(f'series_exercicio_{exercicio_num} = st.number_input("Séries 1: ", min_value = 0, max_value = 10)')
    exec(f'Serie(qtd_series_exercicio_{exercicio_num}).get_series()')
with col3:
    exec(f'reps_exercicio_{exercicio_num} = st.number_input("Núm Reps 1: ", min_value = 0, max_value = 50)')
    exec(f'Serie(qtd_series_exercicio_{exercicio_num}).get_reps()')
with col4:
    exec(f'carga_exercicio_{exercicio_num} = st.number_input("Carga 1: ", min_value = 0, max_value = 10000)')
    exec(f'Serie(qtd_series_exercicio_{exercicio_num}).get_cargas()')

st.button('Salvar')