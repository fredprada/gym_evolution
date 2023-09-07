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
        lista_exercicios = [lista_exercicios.extend(l) for l in (exerc_peito,exerc_ombro,exerc_triceps)]
    elif treino == '2- COSTAS | BÍCEPS':
        lista_exercicios = [lista_exercicios.extend(l) for l in (exerc_costas,exerc_biceps)]
    elif treino == '3- PERNA':
        lista_exercicios = exerc_perna
    return lista_exercicios

treino_selecionado = st.selectbox('Escolha o treino do dia:', (lista_treinos))

exercicio_1 = escolha_exercicios(treino_selecionado)

col1, _ = st.columns(2)
with col1:
    data = st.date_input('Data', value=hora_atual)

col1, col2, col3, col4 = st.columns([3,1,1,1])
with col1:
    select_exercicio_1 = st.selectbox('Exercício: ', (exercicio_1))




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
