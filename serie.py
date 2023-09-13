import streamlit as st

class Serie:
    def __init__(self, qtd_series, serie_num):
        self.qtd_series = qtd_series
        self.serie_num = serie_num

    def get_series(self):
        lista_box_series = []
        for item in range(2, self.qtd_series + 1):
            lista_box_series.append(exec(f'series_exercicio_{self.serie_num}_num_{item} = st.number_input("Séries: ", min_value = 0, max_value = 10, key="serie_{self.serie_num}_{item}")'))
        return lista_box_series

    def get_reps(self):
        lista_box_reps = []
        for item in range(2, self.qtd_series + 1):
            lista_box_reps.append(exec(f'reps_exercicio_{self.serie_num}_num_{item} = st.number_input("Núm Reps: ", min_value = 0, max_value = 50, key="reps_{self.serie_num}_{item}")'))
        return lista_box_reps

    def get_cargas(self):
        lista_box_carga = []
        for item in range(2, self.qtd_series + 1):
            lista_box_carga.append(exec(f'carga_exercicio_{self.serie_num}_num_{item} = st.number_input("Carga: ", min_value = 0, max_value = 1000, key="carga_{self.serie_num}_{item}")'))
        return lista_box_carga
    
    def get_all_names(self):
        lista_geral = []
        lista_geral = self.get_series + self.get_all_names + self.get_reps
        return lista_geral