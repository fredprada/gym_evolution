import streamlit as st
import datetime
from datetime import timedelta
from exercicio import Exercicio

st.title('Evolução de Treino')

hora_atual = datetime.datetime.now() - timedelta(hours=3)
lista_treinos = ['1- PEITO | OMBRO | TRÍCEPS', 
                 '2- COSTAS | BÍCEPS',
                 '3- PERNA']

# exerc_peito = ['PEITO | SUPINO RETO',
#                'PEITO | VOADOR']
# exerc_ombro = ['OMBRO | ELEVAÇÃO LATERAL',
#                'OMBRO | DESENVOLVIMENTO COM HALTER']
# exerc_triceps = ['TRÍCEPS | TRÍCEPS CORDA',
#                  'TRÍCEPS | TRÍCEPS MERGULHO']
# exerc_costas = ['COSTAS | PUXADA ALTA FRONTAL COM PEGADA ABERTA',
#                 'COSTAS | REMADA BAIXA',
#                 'COSTAS | PULL DOWN']
# exerc_biceps = ['BÍCEPS | ROSCA DIRETA',
#                 'BÍCEPS | ROSCA MARTELO']
# exerc_perna = ['PERNA | AGACHAMENTO',
#                'PERNA | EXTENSORA',
#                'PERNA | FLEXORA',
#                'PERNA | PANTURRILHA SENTADO',
#                'PERNA | LEVANTAMENTO TERRA SUMO']

# def escolha_exercicios(treino):
#     global lista_exercicios
#     lista_exercicios = []
#     if treino == '1- PEITO | OMBRO | TRÍCEPS':
#         lista_exercicios = exerc_peito + exerc_ombro + exerc_triceps
#     elif treino == '2- COSTAS | BÍCEPS':
#         lista_exercicios = exerc_costas + exerc_biceps
#     elif treino == '3- PERNA':
#         lista_exercicios = exerc_perna
#     return lista_exercicios

def series_diferentes(qtd_series):
    lista_box_series = []
    for item in range(2, qtd_series + 1):
        lista_box_series.append(exec(f'series_exercicio_1_num_{item} = st.number_input("Séries {item}: ", min_value = 0, max_value = 10)'))
    return lista_box_series

def reps_diferentes(qtd_series):
    lista_box_reps = []
    for item in range(2, qtd_series + 1):
        lista_box_reps.append(exec(f'reps_exercicio_1_num_{item} = st.number_input("Núm Reps {item}: ", min_value = 0, max_value = 50)'))
    return lista_box_reps

def cargas_diferentes(qtd_series):
    lista_box_carga = []
    for item in range(2, qtd_series + 1):
        lista_box_carga.append(exec(f'carga_exercicio_1_num_{item} = st.number_input("Carga {item}: ", min_value = 0, max_value = 1000)'))
    return lista_box_carga


col1, col2 = st.columns([2, 1])
with col1:
    treino_selecionado = st.selectbox('Escolha o treino do dia:', (lista_treinos))
with col2:
    data = st.date_input('Data', value=hora_atual)

# exercicio_1 = escolha_exercicios(treino_selecionado)
exercicio_1 = Exercicio(treino_selecionado).get_exercicio()
# exercicio_2 = escolha_exercicios(treino_selecionado)
# exercicio_3 = escolha_exercicios(treino_selecionado)
# exercicio_4 = escolha_exercicios(treino_selecionado)
# exercicio_5 = escolha_exercicios(treino_selecionado)

col1, col2, col3, col4 = st.columns([3,1,1,1])
with col1:
    select_exercicio_1 = st.selectbox('Exercício 1: ', (exercicio_1))
    qtd_series_exercicio_1 = st.selectbox('Número de séries diferentes: ', ([1, 2, 3, 4, 5]))
# with col2:
#     series_exercicio_1 = st.number_input('Séries 1: ', min_value = 0, max_value = 10)
#     series_diferentes(qtd_series_exercicio_1)
# with col3:
#     reps_exercicio_1 = st.number_input('Núm Reps 1: ', min_value = 0, max_value = 50)
#     reps_diferentes(qtd_series_exercicio_1)
# with col4:
#     carga_exercicio_1 = st.number_input('Carga 1: ', min_value = 0, max_value = 10000)
#     cargas_diferentes(qtd_series_exercicio_1)

st.button('Salvar')