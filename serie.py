class Serie:
    def __init__(self, qtd_series):
        self.qtd_series = qtd_series

    def get_series(self):
        lista_box_series = []
        for item in range(1, self.qtd_series + 1):
            lista_box_series.append(exec(f'series_exercicio_1_num_{item} = st.number_input("Séries {item}: ", min_value = 0, max_value = 10)'))
        return lista_box_series

    def get_reps(self):
        lista_box_reps = []
        for item in range(1, self.qtd_series + 1):
            lista_box_reps.append(exec(f'reps_exercicio_1_num_{item} = st.number_input("Núm Reps {item}: ", min_value = 0, max_value = 50)'))
        return lista_box_reps

    def get_cargas(self):
        lista_box_carga = []
        for item in range(1, self.qtd_series + 1):
            lista_box_carga.append(exec(f'carga_exercicio_1_num_{item} = st.number_input("Carga {item}: ", min_value = 0, max_value = 1000)'))
        return lista_box_carga