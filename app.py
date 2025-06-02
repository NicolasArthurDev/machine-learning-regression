import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("pizza.csv")
x = df[["diametro"]]
y = df[["preco"]]

modelo_diametro = LinearRegression()
modelo_diametro.fit(x, y) 

modelo_preco = LinearRegression()
modelo_preco.fit(y, x) 

# Web
st.title("Projeto Machine Learning: Prevendo o valor ou diâmetro da pizza")
st.divider()

opcao = st.radio("Qual você quer calcular?",["Diâmetro", "Preço"])

if opcao == "Diâmetro":
    diametro = st.number_input("Digite o tamanho do diâmetro da pizza:", min_value=0)
    if diametro:
        preco_previsto = modelo_diametro.predict([[diametro]])[0][0]
        st.write(f"O valor da pizza com o diâmetro de {diametro:.2f} cm é de R${preco_previsto:.2f}")
if opcao == "Preço":
    preco = st.number_input(f"Digite o valor que deseja para calcularmos o tamanho do diâmetro da pizza:", min_value=0)
    
    if preco:
        diametro_previsto = modelo_preco.predict([[preco]])[0][0]
        st.write(f"Se o valor da pizza for R${preco:.2f}, o diâmetro será {diametro_previsto:.2f} cm")

