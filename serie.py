import streamlit as st

class Serie:
    def __init__(self, qtd_series):
        self.qtd_series = qtd_series

    def get_series(self, serie_num):
        lista_box_series = []
        for item in range(2, self.qtd_series + 1):
            lista_box_series.append(exec(f'series_exercicio_{serie_num}_num_{item} = st.number_input("Séries: ", min_value = 0, max_value = 10, key="serie_{serie_num}_{item}")'))
        return lista_box_series

    def get_reps(self, serie_num):
        lista_box_reps = []
        for item in range(2, self.qtd_series + 1):
            lista_box_reps.append(exec(f'reps_exercicio_{serie_num}_num_{item} = st.number_input("Núm Reps: ", min_value = 0, max_value = 50, key="reps_{serie_num}_{item}")'))
        return lista_box_reps

    def get_cargas(self, serie_num):
        lista_box_carga = []
        for item in range(2, self.qtd_series + 1):
            lista_box_carga.append(exec(f'carga_exercicio_{serie_num}_num_{item} = st.number_input("Carga: ", min_value = 0, max_value = 1000, key="carga_{serie_num}_{item}")'))
        return lista_box_carga