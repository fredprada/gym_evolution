import streamlit as st
import plotly.express as px
import pandas as pd
from get_dados import get_dados_mongodb
import datetime
from exercicio import Exercicio

# [OK] Treinos por semana
# [NOK] Evolução da melhor série do exercício
# [NOK] Calendário com dias que treinou
# [NOK] Última carga
# [NOK] Carga máxima
# [NOK] Carga média

######################################################################################################################################
# Defining page properties and title, header and subheader
st.set_page_config(page_title = "Dashboard", layout="wide", page_icon = "📈")

lista_atletas = ['Fred','Mari']
lista_treinos = ['1- PEITO | OMBRO | TRÍCEPS', 
                 '2- COSTAS | BÍCEPS',
                 '3- PERNA']

col1, col2, col3, col4 = st.columns([1, 2, 1, 1])
with col1:
    atleta = st.selectbox('Atleta:', lista_atletas)
with col2:
    treino_selecionado = st.selectbox('Escolha o treino:', (lista_treinos))

valores = get_dados_mongodb().retrieve_data_from_mongodb()
df_valores = valores

df_valores_filtrado = df_valores[df_valores['atleta'] == atleta]

# botao_puxar_dados = st.button('Ver dados da base de dados')

# if botao_puxar_dados:
#     st.dataframe(df_valores_filtrado)

#######################################################################################
# Metrica treinos por semana
today = datetime.datetime.now() - datetime.timedelta(hours=3)
current_week = datetime.date.isocalendar(today)[1]
df_valores_filtrado['data'] = df_valores_filtrado['data'].astype('datetime64[ns]')
df_valores_filtrado['numero_da_semana'] = df_valores_filtrado['data'].apply(lambda x: datetime.date.isocalendar(x)[1])
df_current_week = df_valores_filtrado[df_valores_filtrado['numero_da_semana'] == current_week]
treinos_essa_semana = len(df_current_week['data'].drop_duplicates())
st.metric(label="Treinos essa semana",value = treinos_essa_semana)

#######################################################################################
# Gráfico treinos por semana
df_treinos_por_semana = pd.DataFrame(df_valores_filtrado[['numero_da_semana']].drop_duplicates().value_counts()).reset_index()

col1, col2 = st.columns([3, 1])
fig = px.bar(df_treinos_por_semana, x="numero_da_semana", y="count", text="count")
fig.update_traces(textposition="outside")
fig.update_layout(xaxis_title="N° da semana", 
                  yaxis_title=None, 
                  yaxis_range=[0, 7],
                  width=900,
                  height=250)
fig.update_traces(marker=dict(color='#20837b'))
fig.update_layout(title=dict(text='Treinos por semana', font=dict(size=22)))
col1.plotly_chart(fig, theme=None, use_container_width=True)

#######################################################################################
# Evolução da maior carga por exercício


lista_exercicio = Exercicio(treino_selecionado).get_exercicio()

def get_max_carga(treino_selecionado):
    df_agupado_por_treino = pd.DataFrame(df_valores_filtrado[df_valores_filtrado['treino'] == treino_selecionado])
    def max_valor(lista):
        return max(lista)
    df_agupado_por_treino['max_carga'] = df_agupado_por_treino['carga_exercicio_1'].apply(max_valor)
    # resultado = df_agupado_por_treino.groupby('select_exercicio1')['max_carga'].max().reset_index()
    return df_agupado_por_treino

def get_dataframes_from_treino(treino_selecionado):
    if treino_selecionado == '1- PEITO | OMBRO | TRÍCEPS':
        df_agupado_por_treino = get_max_carga(treino_selecionado)
        ##################################################################################################################
        # PEITO, OMBRO E TRICEPS
        df1 = df_agupado_por_treino[df_agupado_por_treino['select_exercicio1'] == 'PEITO | SUPINO RETO']
        df1 = df1[['data','max_carga']]
        titulo1 = 'Supino Reto'

        df2 = df_agupado_por_treino[df_agupado_por_treino['select_exercicio1'] == 'OMBRO | ELEVAÇÃO LATERAL']
        df2 = df2[['data','max_carga']]
        titulo2 = 'Elevação Lateral'
        
        df3 = df_agupado_por_treino[df_agupado_por_treino['select_exercicio1'] == 'OMBRO | DESENVOLVIMENTO COM HALTER']
        df3 = df3[['data','max_carga']]
        titulo3 = 'Desenvolvimento'
        
        df4 = df_agupado_por_treino[df_agupado_por_treino['select_exercicio1'] == 'OMBRO | REMADA ALTA']
        df4 = df4[['data','max_carga']]
        titulo4 = 'Remada Alta'
        
        df5 = df_agupado_por_treino[df_agupado_por_treino['select_exercicio1'] == 'TRÍCEPS | TRÍCEPS CORDA']
        df5 = df5[['data','max_carga']]
        titulo5 = 'Tríceps Corda'
        return df1, df2, df3, df4, df5, titulo1, titulo2, titulo3, titulo4, titulo5
    
    elif treino_selecionado == '2- COSTAS | BÍCEPS':
        df_agupado_por_treino = get_max_carga(treino_selecionado)
        ##################################################################################################################
        # COSTAS E BICEPS
        df1 = df_agupado_por_treino[df_agupado_por_treino['select_exercicio1'] == 'COSTAS | PUXADA ALTA FRONTAL COM PEGADA ABERTA']
        df1 = df1[['data','max_carga']]
        titulo1 = 'Puxada Alta'

        df2 = df_agupado_por_treino[df_agupado_por_treino['select_exercicio1'] == 'COSTAS | REMADA BAIXA']
        df2 = df2[['data','max_carga']]
        titulo2 = 'Remada Baixa'

        df3 = df_agupado_por_treino[df_agupado_por_treino['select_exercicio1'] == 'COSTAS | PULL DOWN']
        df3 = df3[['data','max_carga']]
        titulo3 = 'Pull Down'
        
        df4 = df_agupado_por_treino[df_agupado_por_treino['select_exercicio1'] == 'BÍCEPS | ROSCA DIRETA']
        df4 = df4[['data','max_carga']]
        titulo4 = 'Rosca Direta'

        df5 = df_agupado_por_treino[df_agupado_por_treino['select_exercicio1'] == 'BÍCEPS | ROSCA MARTELO']
        df5 = df5[['data','max_carga']]
        titulo5 = 'Rosca Martelo'
        return df1, df2, df3, df4, df5, titulo1, titulo2, titulo3, titulo4, titulo5
   
    elif treino_selecionado == '3- PERNA':
        df_agupado_por_treino = get_max_carga(treino_selecionado)
        ##################################################################################################################
        # PERNA
        df1 = df_agupado_por_treino[df_agupado_por_treino['select_exercicio1'] == 'PERNA | AGACHAMENTO']
        df1 = df1[['data','max_carga']]
        titulo1 = 'Agachamento'
        
        df2 = df_agupado_por_treino[df_agupado_por_treino['select_exercicio1'] == 'PERNA | EXTENSORA']
        df2 = df2[['data','max_carga']]
        titulo2 = 'Extensora'
        
        df3 = df_agupado_por_treino[df_agupado_por_treino['select_exercicio1'] == 'PERNA | FLEXORA']
        df3 = df3[['data','max_carga']]
        titulo3 = 'Flexora'
        
        df4 = df_agupado_por_treino[df_agupado_por_treino['select_exercicio1'] == 'PERNA | PANTURRILHA SENTADO']
        df4 = df4[['data','max_carga']]
        titulo4 = 'Panturrilha'
        
        df5 = df_agupado_por_treino[df_agupado_por_treino['select_exercicio1'] == 'PERNA | LEVANTAMENTO TERRA SUMO']
        df5 = df5[['data','max_carga']]
        titulo5 = 'Terra'
        return df1, df2, df3, df4, df5, titulo1, titulo2, titulo3, titulo4, titulo5

df1, df2, df3, df4, df5, titulo1, titulo2, titulo3, titulo4, titulo5 = get_dataframes_from_treino(treino_selecionado)
    
col1, col2, col3 = st.columns([1, 1, 1])
df_list = [df1, df2, df3]
df_list_2 = [df4, df5]
titulos_list = [titulo1, titulo2, titulo3]
titulos_list_2 = [titulo4, titulo5]
cols = [col1, col2, col3]
cols_2 = [col1, col2]
for df, titulo, col in zip(df_list, titulos_list, cols):
    fig = px.line(df, 
                x='data', 
                y='max_carga',
                text='max_carga',
                markers=True,
                width=1000, 
                height=300)
    fig.update_traces(textposition='top center', 
                    textfont_size=16)
    fig.update_layout(yaxis_title=None,
                    xaxis_title=None,
                    yaxis={'visible': False},
                   yaxis_range=[int(min(df['max_carga']))-2, int(max(df['max_carga']))+2])
    fig.update_layout(title=dict(text=titulo, font=dict(size=22)))
    fig.update_traces(marker=dict(color='#20837b'),
                      line=dict(color='#20837b'))
    col.plotly_chart(fig, theme=None, use_container_width=True)

col1, col2, _ = st.columns([1, 1, 1])
for df, titulo, col in zip(df_list_2, titulos_list_2, cols_2):
    fig = px.line(df, 
                x='data', 
                y='max_carga',
                text='max_carga',
                markers=True, 
                width=1000, 
                height=300)
    fig.update_traces(textposition='top center', 
                    textfont_size=16)
    fig.update_layout(yaxis_title=None,
                    xaxis_title=None,
                    yaxis={'visible': False},
                   yaxis_range=[int(min(df['max_carga']))-2, int(max(df['max_carga']))+2])
    fig.update_layout(title=dict(text=titulo, font=dict(size=22)))
    fig.update_traces(marker=dict(color='#20837b'),
                      line=dict(color='#20837b'))
    col.plotly_chart(fig, theme=None, use_container_width=True)