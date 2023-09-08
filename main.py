import streamlit as st
import datetime
from datetime import timedelta

st.title('Evolução de Treino')

hora_atual = datetime.datetime.now() - timedelta(hours=3)
lista_treinos = ['1- PEITO | OMBRO | TRÍCEPS', 
                 '2- COSTAS | BÍCEPS',
                 '3- PERNA']

exerc_peito = ['PEITO | SUPINO RETO',
               'PEITO | VOADOR']
exerc_ombro = ['OMBRO | ELEVAÇÃO LATERAL',
               'OMBRO | DESENVOLVIMENTO COM HALTER']
exerc_triceps = ['TRÍCEPS | TRÍCEPS CORDA',
                 'TRÍCEPS | TRÍCEPS MERGULHO']
exerc_costas = ['COSTAS | PUXADA ALTA FRONTAL COM PEGADA ABERTA',
                'COSTAS | REMADA BAIXA',
                'COSTAS | PULL DOWN']
exerc_biceps = ['BÍCEPS | ROSCA DIRETA',
                'BÍCEPS | ROSCA MARTELO']
exerc_perna = ['PERNA | AGACHAMENTO',
               'PERNA | EXTENSORA',
               'PERNA | FLEXORA',
               'PERNA | PANTURRILHA SENTADO',
               'PERNA | LEVANTAMENTO TERRA SUMO']

def escolha_exercicios(treino):
    global lista_exercicios
    lista_exercicios = []
    if treino == '1- PEITO | OMBRO | TRÍCEPS':
        lista_exercicios = exerc_peito + exerc_ombro + exerc_triceps
    elif treino == '2- COSTAS | BÍCEPS':
        lista_exercicios = exerc_costas + exerc_biceps
    elif treino == '3- PERNA':
        lista_exercicios = exerc_perna
    return lista_exercicios

def quantidade_de_series_diferentes(qtd_series):
    if qtd_series > 1:
        lista_box_reps = []
        lista_box_carga = []
        lista_box_series = []
        for item in range(1, qtd_series + 1):
            lista_box_series.append(exec(f'series_exercicio_1_num_{item} = st.number_input("Séries ex{item}: ", min_value = 0, max_value = 10)'))
            lista_box_reps.append(exec(f'reps_exercicio_1_num_{item} = st.number_input("Núm Reps ex{item}: ", min_value = 0, max_value = 50)'))
            lista_box_carga.append(exec(f'carga_exercicio_1_num_{item} = st.number_input("Carga ex{item}: ", min_value = 0, max_value = 1000)'))
        return lista_box_series, lista_box_reps, lista_box_carga
    else:
        reps_ex_1 = reps_exercicio_1_num_1_ = st.number_input("Núm Reps ex_1: ", min_value = 0, max_value = 50)
        carga_ex1 = carga_exercicio_1_num_1_ = st.number_input("Carga ex_1: ", min_value = 0, max_value = 1000)
        return reps_ex_1, carga_ex1


col1, col2 = st.columns([2, 1])
with col1:
    data = st.date_input('Data', value=hora_atual)
with col2:
    treino_selecionado = st.selectbox('Escolha o treino do dia:', (lista_treinos))

exercicio_1 = escolha_exercicios(treino_selecionado)
exercicio_2 = escolha_exercicios(treino_selecionado)
exercicio_3 = escolha_exercicios(treino_selecionado)
exercicio_4 = escolha_exercicios(treino_selecionado)
exercicio_5 = escolha_exercicios(treino_selecionado)

col1, col2, col3, col4 = st.columns([3,1,1,1])
with col1:
    select_exercicio_1 = st.selectbox('Exercício 1: ', (exercicio_1))
    qtd_series_exercicio_1 = st.selectbox('Número de séries (ex1): ', ([1, 2, 3, 4, 5]))
    # select_exercicio_2 = st.selectbox('Exercício 2: ', (exercicio_2))
    # select_exercicio_3 = st.selectbox('Exercício 3: ', (exercicio_3))
    # select_exercicio_4 = st.selectbox('Exercício 4: ', (exercicio_4))
    # select_exercicio_5 = st.selectbox('Exercício 5: ', (exercicio_5))
with col2:
    quantidade_de_series_diferentes(qtd_series_exercicio_1)[0]
    # series_exercicio_2 = st.number_input('Núm Séries ex2: ', min_value = 0, max_value = 10)
    # series_exercicio_3 = st.number_input('Núm Séries ex3: ', min_value = 0, max_value = 10)
    # series_exercicio_4 = st.number_input('Núm Séries ex4: ', min_value = 0, max_value = 10)
    # series_exercicio_5 = st.number_input('Núm Séries ex5: ', min_value = 0, max_value = 10)
with col3:
    quantidade_de_series_diferentes(qtd_series_exercicio_1)[1]
    # reps_exercicio_2 = st.number_input('Núm Reps ex2: ', min_value = 0, max_value = 50)
    # reps_exercicio_3 = st.number_input('Núm Reps ex3: ', min_value = 0, max_value = 50)
    # reps_exercicio_4 = st.number_input('Núm Reps ex4: ', min_value = 0, max_value = 50)
    # reps_exercicio_5 = st.number_input('Núm Reps ex5: ', min_value = 0, max_value = 50)
with col4:
    quantidade_de_series_diferentes(qtd_series_exercicio_1)[2]
    # carga_exercicio_2 = st.number_input('Carga (kg) ex2: ', min_value = 0, max_value = 10000)
    # carga_exercicio_3 = st.number_input('Carga (kg) ex3: ', min_value = 0, max_value = 10000)
    # carga_exercicio_4 = st.number_input('Carga (kg) ex4: ', min_value = 0, max_value = 10000)
    # carga_exercicio_5 = st.number_input('Carga (kg) ex5: ', min_value = 0, max_value = 10000)



#################################################################################################################
# col1, col2 = st.columns([3,2])
# with col1:
#     situacao = st.text_area('Situação', help='Onde? Quando? Com quem? O que estava fazendo?')
#     pensamento_automatico = st.text_area('Pensamento automático', help="""O que estava passando pela minha cabeça?
#                                                                         O que isso significa pra mim, ao futuro e à minha vida?
#                                                                         O que diz ao meu respeito?
#                                                                         Quais imagens ou lembranças eu tenho?
#                                                                         """)
#     evidencias_fav = st.text_area('Evidências que favorecem o pensamento automático', help='Fatos que favorecem o pensamento')
# with col2:
#     humor_antes_1 = st.text_input('Humor', key='humor_antes_txt1', help='Qual emoção estava sentindo?')
#     intensidade_antes_1 = st.slider('Qual intensidade?', 0, 100, 1, key='humor_antes_slider1')
#     humor_antes_2 = st.text_input('Humor', key='humor_antes_txt2', help='Qual emoção estava sentindo?')
#     intensidad_antes_2 = st.slider('Qual intensidade?', 0, 100, 1, key='humor_antes_slider2')

# st.markdown('### Validação dos pensamentos automáticos:')

# col1, col2 = st.columns([3, 2])
# with col1:
#     evidencias_desfav = st.text_area('Evidências que desfavorecem o pensamento automático', help='Fatos que desfavorecem o pensamento')
#     pensamentos_alternativos = st.text_area('Pensamentos alternativos', help="""Diante das evidências, que outros pensamentos alternativos posso ter?
#                                                                                 Qual a o nível de acreditação que tenho nesse pensamento?""")
# with col2:
#     humor_depois_1 = st.text_input('Humor (após RPD)', key='humor_depois_txt1', help='Após o preenchimento da tabela como está meu humor agora?')
#     intensidade_depois_1 = st.slider('Qual intensidade?', 0, 100, 1, key='humor_depois_slider1')
#     humor_depois_2 = st.text_input('Humor (após RPD)', key='humor_depois_txt2', help='Após o preenchimento da tabela como está meu humor agora?')
#     intensidade_depois_2 = st.slider('Qual intensidade?', 0, 100, 1, key='humor_depois_slider2')

# st.button('Salvar')
