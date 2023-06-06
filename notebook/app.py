import streamlit as st
import yfinance as yf
from datetime import date
import pandas as pd
from prophet import Prophet
from prophet.plot import plot_plotly, plot_components_plotly
from plotly import graph_objects as go

data_inicio = '2017-01-01'
data_fim = date.today().strftime('%Y-%m-%d')

st.title('Análise de ações')

#criando a side bar
st.sidebar.header('Escolha a ação')

n_dias = st.slider('Quantidade de dias a ser prevista', 30, 365)

#Coletando o nome e sigla da ação escolhida
def pegar_dados_acao():
    path = '/home/bruno/repos/B3_Prediction_share_bmg_2023/dataset/all_bovespa.parquet'
    return pd.read_parquet(path)

df = pegar_dados_acao()

acao = df['nome_acao']
acao_escolhida = st.sidebar.selectbox('Escolha uma ação', acao)

