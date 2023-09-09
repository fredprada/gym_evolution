import streamlit as st
import datetime
from datetime import timedelta
from exercicio import Exercicio
from serie import Serie

st.set_page_config(page_title = "Evolução academia", page_icon = "💪")#, layout="wide")
st.title('Evolução academia 💪')

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
    exercicio_num = st.selectbox("Quantos ex você vai fazer?", ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

st.markdown("""---""")

lista_exercicio = Exercicio(treino_selecionado).get_exercicio()

for num in range(1, exercicio_num + 1):
    col1, col2, col3, col4 = st.columns([3,1,1,1])
    with col1:
        exec(f'select_exercicio{num} = st.selectbox("Exercício ({num}): ", (lista_exercicio))')
        exec(f'qtd_series_exercicio_{num} = st.selectbox("Número de séries diferentes:", ([1, 2, 3, 4, 5]), key = "series_dif_{num}")')
    with col2:
        exec(f'series_exercicio_1_{num} = st.number_input("Séries: ", min_value = 0, max_value = 10, key = "serie_{num}")')
        exec(f'Serie(qtd_series_exercicio_{num}).get_series({num})')
    with col3:
        exec(f'reps_exercicio_1_{num} = st.number_input("Núm Reps: ", min_value = 0, max_value = 50, key = "reps_{num}")')
        exec(f'Serie(qtd_series_exercicio_{num}).get_reps({num})')
    with col4:
        exec(f'carga_exercicio_1_{num} = st.number_input("Carga: ", min_value = 0, max_value = 10000, key = "carga_{num}")')
        exec(f'Serie(qtd_series_exercicio_{num}).get_cargas({num})')
    st.markdown("""---""")

st.button('Salvar')