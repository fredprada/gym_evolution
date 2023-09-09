# import os
# import streamlit as st
# from pymongo import MongoClient

# class SalvarDados:
#     def __init__(self, tabela_para_salvar):
#         self.tabela_para_salvar = tabela_para_salvar

#     def connect_to_mongodb():
#         global collection
#         client = os.getenv('CLIENT_TOKEN')
#         myclient = MongoClient(client)
#         db = myclient.get_database('db_evolucao_academia')
#         collection = db.collection_evolucao_academia
#         return collection

#     def database_insertion(list_to_add):
#         connect_to_mongodb()
#         st.sidebar.text('Inserção em progresso')
#         collection.insert_many(list_to_add)

#     def retrieve_data_from_mongodb():
#         collection = connect_to_mongodb()
#         data_list = []
#         data_list = [x for x in collection.find()]
#         return data_list