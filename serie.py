import streamlit as st

class Serie:
    def __init__(self, qtd_series, serie_num):
        self.qtd_series = qtd_series
        self.serie_num = serie_num

    @st.cache_data
    def get_series(_self):
        lista_box_series = []
        for item in range(2, _self.qtd_series + 1):
            lista_box_series.append(exec(f'series_exercicio_{_self.serie_num}_num_{item} = st.number_input("Séries: ", min_value = 0, max_value = 10, key="serie_{_self.serie_num}_{item}")'))
        return lista_box_series

    @st.cache_data
    def get_reps(_self):
        lista_box_reps = []
        for item in range(2, _self.qtd_series + 1):
            lista_box_reps.append(exec(f'reps_exercicio_{_self.serie_num}_num_{item} = st.number_input("Núm Reps: ", min_value = 0, max_value = 50, key="reps_{_self.serie_num}_{item}")'))
        return lista_box_reps

    @st.cache_data
    def get_cargas(_self):
        lista_box_carga = []
        for item in range(2, _self.qtd_series + 1):
            lista_box_carga.append(exec(f'carga_exercicio_{_self.serie_num}_num_{item} = st.number_input("Carga: ", min_value = 0, max_value = 1000, key="carga_{_self.serie_num}_{item}")'))
        return lista_box_carga