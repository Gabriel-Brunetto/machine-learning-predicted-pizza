import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv('pizzas.csv')

modelo = LinearRegression()
X = df[['diametro']]
y = df[['preco']]

modelo.fit(X, y)

st.title('Previsor de Preço de Pizzas')
st.divider()
diametro = st.number_input('Digite o diâmetro da pizza (cm):', min_value=0, value=30, key='diametro_input')

if diametro:
  preco_previsto = modelo.predict([[diametro]])[0][0]
  st.write(f'O preço previsto para uma pizza de {diametro} cm é R$ {preco_previsto:.2f}')