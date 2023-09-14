from pymongo import MongoClient
import os
import streamlit as st
import pandas as pd
from salvar_dados import salvar_dados_mongodb

class get_dados_mongodb:
    def __init__(self):
        pass

    def retrieve_data_from_mongodb(self):
        collection = salvar_dados_mongodb("valor").connect_to_mongodb()
        data_list = []
        data_list = [x for x in collection.find()]
        df_data_list = pd.DataFrame(data_list)
        return df_data_list