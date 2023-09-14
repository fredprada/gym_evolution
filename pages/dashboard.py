import streamlit as st
import plotly.express as px
import pandas as pd

######################################################################################################################################
# Defining page properties and title, header and subheader
st.set_page_config(page_title = "📈 Dashboard", layout="wide")

lista_atletas = ['Fred','Mari']
lista_atletas = st.selectbox('Atleta:', lista_atletas)