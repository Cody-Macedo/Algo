import streamlit as st
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# run app with: streamlit run app.py
dfVgSales = pd.read_csv("vgsales.csv")

# Afficher le dataset chargé suivant un nombre de ligne entrées par l’utilisateur
st.title("Video Games")
st.header("Choisir le nombre de donnée à afficher")
vgSalesNbInput = st.number_input("Entrer le nombre de donnée affiché: ", 1)
if st.button("Afficher les données"):
    st.table(dfVgSales.head(vgSalesNbInput))

# Afficher le nom des colonnes du dataset
st.header("Affichage du nom des colonnes du dataset")
st.write(dfVgSales.columns.tolist())

# Afficher le type des colonnes du dataset ainsi que les colonnes sélectionnées
st.header("Affichage du type des colonnes")
checkBoxes = [st.checkbox(i, key=i) for i in dfVgSales]
print('checkBoxes: ' + checkBoxes)
if st.button("Afficher les types"):
    st.write(dfVgSales.dtypes)
    st.write('à finir')
# La shape du dataset, par lignes et par colonnes

# Afficher les statistiques descriptives du dataset
