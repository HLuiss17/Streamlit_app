
import csv
import streamlit as st
import pandas as pd
st.title("Mi primera Aplicacion")
st.sidebar.title("Parametros")
num1=st.slider("Seleccione valor 1",min_value=0,max_value=10,value=3)
num2=st.slider("Seleccione valor 2",min_value=0,max_value=10,value=3)
st.write("La suma de los dos numeros es:",num1+num2)

archivo_cargado = st.sidebar.file_uploader("Cargue su base de datos",type=[".xlsx",".xls"])
if archivo_cargado is not None:
    df=pd.read_excel(archivo_cargado)
    st.write(df)
    csv=df.to_csv()
    st.download_button(label="Descargar archivo csv",data=csv)



