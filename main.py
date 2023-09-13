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
lista_variaveis = []
lista_series_difs = []
lista_nomes = []

def get_series(qtd_series, serie_num):
    lista_box_series = []
    for item in range(2, qtd_series + 1):
        lista_box_series.append(exec(f'series_exercicio_{serie_num}_num_{item} = st.number_input("Séries: ", min_value = 0, max_value = 10, key="serie_{serie_num}_{item}")'))
    return lista_box_series

# def get_reps(self):
#     lista_box_reps = []
#     for item in range(2, self.qtd_series + 1):
#         lista_box_reps.append(exec(f'reps_exercicio_{self.serie_num}_num_{item} = st.number_input("Núm Reps: ", min_value = 0, max_value = 50, key="reps_{self.serie_num}_{item}")'))
#     return lista_box_reps

# def get_cargas(self):
#     lista_box_carga = []
#     for item in range(2, self.qtd_series + 1):
#         lista_box_carga.append(exec(f'carga_exercicio_{self.serie_num}_num_{item} = st.number_input("Carga: ", min_value = 0, max_value = 1000, key="carga_{self.serie_num}_{item}")'))
#     return lista_box_carga

for num in range(1, exercicio_num + 1):
    col1, col2, col3, col4 = st.columns([3,1,1,1])
    with col1:
        exec(f'select_exercicio{num} = st.selectbox("Exercício ({num}): ", (lista_exercicio))')
        exec(f'qtd_series_exercicio_{num} = st.selectbox("Número de séries diferentes:", ([1, 2, 3, 4, 5]), key = "series_dif_{num}")')
    with col2:
        exec(f'series_exercicio_1_{num} = st.number_input("Séries: ", min_value = 0, max_value = 10, key = "serie_{num}")')
        get_series(f'qtd_series_exercicio_{num}', num)
    with col3:
        exec(f'reps_exercicio_1_{num} = st.number_input("Núm Reps: ", min_value = 0, max_value = 50, key = "reps_{num}")')
        exec(f'Serie(qtd_series_exercicio_{num}, {num}).get_reps()')
    with col4:
        exec(f'carga_exercicio_1_{num} = st.number_input("Carga: ", min_value = 0, max_value = 10000, key = "carga_{num}")')
        exec(f'Serie(qtd_series_exercicio_{num}, {num}).get_cargas()')
       
    exec(f'qtd_series = qtd_series_exercicio_{num}')
    
    for qtd in range(1, qtd_series + 1):
        var_series_dif = [f'series_exercicio_{qtd}_num_{num}',
                          f'reps_exercicio_{qtd}_num_{num}',
                          f'carga_exercicio_{qtd}_num_{num}']
        lista_series_difs.append(var_series_dif)
    variaveis_conjunto = [f'select_exercicio{num}',
                          f'qtd_series_exercicio_{num}',
                          f'series_exercicio_1_{num}',
                          f'reps_exercicio_1_{num}',
                          f'carga_exercicio_1_{num}']
    lista_variaveis.append(variaveis_conjunto)
    st.markdown("""---""")

lista_variaveis_completa = lista_variaveis + lista_series_difs

def flatten_list(nested_list):
    return list(itertools.chain(*nested_list))

flat_lista_variaveis_completa = flatten_list(lista_variaveis_completa)

# lista_dados_coletados = [{'var':lista_variaveis}]
# dict_info = {}
# for num in range(1, len(lista_variaveis)):
#     dict_info[f"exec(f'select_exercicio{num}')"] = exec(f'select_exercicio{num}')
#     dict_info[f"exec(f'qtd_series_exercicio_{num}')"] = exec(f'qtd_series_exercicio_{num}')

#     dict_info[f"exec(f'series_exercicio_1_{num}')"] = exec(f'series_exercicio_1_{num}')
#     dict_info[f"exec(f'reps_exercicio_1_{num}')"] = exec(f'reps_exercicio_1_{num}')
#     dict_info[f"exec(f'carga_exercicio_1_{num}')"] = exec(f'carga_exercicio_1_{num}')
    
#     dict_info[f"exec(f'series_exercicio_2_{num}')"] = exec(f'series_exercicio_2_{num}')
#     dict_info[f"exec(f'reps_exercicio_2_{num}')"] = exec(f'reps_exercicio_2_{num}')
#     dict_info[f"exec(f'carga_exercicio_2_{num}')"] = exec(f'carga_exercicio_2_{num}')
    
#     dict_info[f"exec(f'series_exercicio_3_{num}')"] = exec(f'series_exercicio_3_{num}')
#     dict_info[f"exec(f'reps_exercicio_3_{num}')"] = exec(f'reps_exercicio_3_{num}')
#     dict_info[f"exec(f'carga_exercicio_3_{num}')"] = exec(f'carga_exercicio_3_{num}')
    
#     dict_info[f"exec(f'series_exercicio_4_{num}')"] = exec(f'series_exercicio_4_{num}')
#     dict_info[f"exec(f'reps_exercicio_4_{num}')"] = exec(f'reps_exercicio_4_{num}')
#     dict_info[f"exec(f'carga_exercicio_4_{num}')"] = exec(f'carga_exercicio_4_{num}')
    
#     dict_info[f"exec(f'series_exercicio_5_{num}')"] = exec(f'series_exercicio_5_{num}')
#     dict_info[f"exec(f'reps_exercicio_5_{num}')"] = exec(f'reps_exercicio_5_{num}')
#     dict_info[f"exec(f'carga_exercicio_5_{num}')"] = exec(f'carga_exercicio_5_{num}')
#     lista_dados_coletados.append(dict_info)

lista_variaveis_valores = []

for variavel in flat_lista_variaveis_completa:
    variaveis_valores = {}  # Crie um novo dicionário para cada iteração
    valor = globals().get(variavel, None)
    if isinstance(valor, (int, str)):
        variaveis_valores[variavel] = valor
    lista_variaveis_valores.append(variaveis_valores)

botao_salvar = st.button('Salvar')
botao_ver_dados = st.button('Ver tabela com dados do banco')

if botao_salvar:
    # ETL list_to_add = func_add_row(date_of_the_game,time_played,pai,played_alone,time_of_the_game,enthusiasm_before_playing,rating,listened_to_music,rest_time,feeling_before_game,calorias)
    salvar_dados_mongodb(lista_variaveis_completa).database_insertion()

if botao_ver_dados:
    # ETL list_to_add = func_add_row(date_of_the_game,time_played,pai,played_alone,time_of_the_game,enthusiasm_before_playing,rating,listened_to_music,rest_time,feeling_before_game,calorias)
    # salvar_dados_mongodb(lista_dados_coletados).retrieve_data_from_mongodb()
    # st.sidebar.text(flat_lista_variaveis_completa)
    st.sidebar.text(lista_variaveis_completa)
    st.sidebar.text(lista_variaveis_valores)