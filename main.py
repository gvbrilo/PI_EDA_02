#Importamos las librerías
import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf
from datetime import datetime, timedelta
sns.set()

#Le agregamos un título
st.title('**EDA OF THE S&P 500 DATASETS**')

st.markdown('#### Utilizamremos Streamlit para generar análisis de gráficos interactivos de las empresas que forman parte del SP500')


#Definimos función para guardar los datasets en dataframes.
def READCSVINDEX (symbol:str):
    try:
        df = pd.read_csv(symbol+'.csv',index_col=0)
    except:
        try:
            df = pd.read_csv('Sectores/'+symbol+'.csv',index_col=0)
        except:
            df = pd.read_csv('Empresas/'+symbol+'.csv',index_col=0)
    df.index = pd.to_datetime(df.index)
    return df