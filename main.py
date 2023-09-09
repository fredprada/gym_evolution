import streamlit as st
import datetime
from datetime import timedelta
from exercicio import Exercicio
from serie import Serie
# from exercicio_realizado import ExercicioRealizado

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

# exercicio_1 = Exercicio(treino_selecionado).get_exercicio()

# col1, col2, col3, col4 = st.columns([3,1,1,1])
# with col1:
#     select_exercicio_1 = st.selectbox('Exercício 1: ', (exercicio_1))
#     qtd_series_exercicio_1 = st.selectbox('Número de séries diferentes: ', ([1, 2, 3, 4, 5]))
# with col2:
#     series_exercicio_1 = st.number_input('Séries 1: ', min_value = 0, max_value = 10)
# with col3:
#     reps_exercicio_1 = st.number_input('Núm Reps 1: ', min_value = 0, max_value = 50)
# with col4:
#     carga_exercicio_1 = st.number_input('Carga 1: ', min_value = 0, max_value = 10000)

exercicio_num = st.selectbox("Quantos exercícios você vai fazer?", ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# exec(f'exercicio{exercicio_num} = ExercicioRealizado({exercicio_num})')

lista_exercicio = Exercicio(treino_selecionado).get_exercicio()

for num in range(1, exercicio_num + 1):
    col1, col2, col3, col4 = st.columns([3,1,1,1])
    with col1:
        exec(f'select_exercicio{num} = st.selectbox("Exercício ({num}): ", (lista_exercicio))')
        exec(f'qtd_series_exercicio_{num} = st.selectbox("Número de séries diferentes: {num}", ([1, 2, 3, 4, 5]))')
    with col2:
        exec(f'series_exercicio_1_{num} = st.number_input("Séries ({num}): ", min_value = 0, max_value = 10)')
        exec(f'Serie(qtd_series_exercicio_{num}).get_series({num})')
    with col3:
        exec(f'reps_exercicio_1_{num} = st.number_input("Núm Reps ({num}): ", min_value = 0, max_value = 50)')
        exec(f'Serie(qtd_series_exercicio_{num}).get_reps({num})')
    with col4:
        exec(f'carga_exercicio_1_{num} = st.number_input("Carga ({num}): ", min_value = 0, max_value = 10000)')
        exec(f'Serie(qtd_series_exercicio_{num}).get_cargas({num})')
    st.markdown("""---""")


st.button('Salvar')