from pymongo import MongoClient
import os
import streamlit as st
import pandas as pd

class SalvarDados:
    def __init__(self, tabela_para_salvar):
        self.tabela_para_salvar = tabela_para_salvar

    def connect_to_mongodb(self):
        global collection
        client = os.getenv('CLIENT_TOKEN')
        myclient = MongoClient(client)
        db = myclient.get_database('db_evolucao_academia')
        collection = db.collection_evolucao_academia
        return collection

    def database_insertion(self):
        self.connect_to_mongodb()
        st.sidebar.text('Inserção em progresso')
        collection.insert_many(self.tabela_para_salvar)

    def retrieve_data_from_mongodb(self):
        collection = self.connect_to_mongodb()
        data_list = []
        data_list = [x for x in collection.find()]
        df_data_list = pd.DataFrame(data_list)
        return df_data_list