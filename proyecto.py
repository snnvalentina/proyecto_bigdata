import streamlit as st
import pandas as pd

# Título de la app
st.title('Proyecto Big Data')
#poner un dividor
st.write('---')
data_set = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vTV-suRQ2Wa43ty1TqWgQp__u8Fa71CJjR3XMlqubpN4c8WNTBBCbkIC_cMvxyFBy4pJkF6sw_qZpRg/pub?gid=1970058776&single=true&output=csv')
print(data_set)


#base de datos
st.write('## Datos de la base de datos pura')
st.write(data_set)
st.write('---')

#limpieza de datos
data_set['Income'].fillna(data_set['Income'].mean(), inplace=True)
data_set = data_set.astype(str)
data_set = data_set.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
data_set = data_set[data_set['Marital_Status'] != 'YOLO']

#base de datos
st.write('## Datos de la base de datos limpia')
st.write(data_set)
st.write('---')


#exploracion estadistica
st.write('## Exploracion estadistica')
st.write(data_set.describe())
st.write('---')

st.write('## Exploracion grafica')
st.write('### Fecha de cumpleaños respecto a al nivel de educacion')
st.bar_chart(data_set, x='Year_Birth', y='Education')

st.write('### Estado civil respecto a al nivel de educacion')
st.bar_chart(data_set, x='Education', y='Marital_Status')

st.write('### Estado civil respecto a al nivel de ingresos')
st.bar_chart(data_set, x='Income', y='Marital_Status')


st.write('## Segmentacion de clientes')
st.write('#### Segmentacion por edad y nivel de educacion')
st.bar_chart(data_set, x='Year_Birth', y='Education', color='Marital_Status')