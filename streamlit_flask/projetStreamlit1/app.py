import streamlit as st
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# run app with: streamlit run app.py
dfVgSales = pd.read_csv("vgsales.csv")
dfCac40 = pd.read_csv("CAC40.csv")

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
# checkBoxes = [st.checkbox(i, key=i) for i in dfVgSales]
# print('checkBoxes: ' + checkBoxes.__str__())

if st.button("Afficher tous les types"):
    st.write(dfVgSales.dtypes)
    st.write('à finir')


def multiSelectColumns():
    columns = dfVgSales.columns.tolist()
    selectedColumns = st.multiselect("Selectionner les colonnes", columns)
    dfSelected = dfVgSales[selectedColumns]
    return dfSelected

dfSelected = multiSelectColumns()
if st.button("Afficher les types séléctionné"):
    st.write(dfSelected.dtypes)

# La shape du dataset, par lignes et par colonnes
st.header("Affichage du shape")
st.write('Colonnes: ', dfVgSales.shape[1])
st.write('Lignes: ', dfVgSales.shape[0])

# Afficher les statistiques descriptives du dataset
st.header("Affichage des statistiques")
st.write(dfVgSales.describe())

# Afficher plusieurs type de graphique dans une partie visualisation avec notamment :
# * Une heatmap des corrélations avec Matplotlib et Seaborn (avec les valeurs annotés)
st.header("Affichage des Graphes:")
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(dfVgSales.corr(), cmap="BuPu", annot=True)
st.pyplot(fig)
# * Un graphique en barres afin de visualiser la taille du dataset par caractéristiques (on pourra notamment grouper les données afin d’avoir des graphiques plus précis) données afin d’avoir des graphiques plus précis)
dsGenreSales = dfVgSales[['Genre', 'Global_Sales']].copy()
dsGenreSales = dsGenreSales.groupby(['Genre']).sum()
dsGenreSales = dsGenreSales.reset_index()
dsGenreSales = dsGenreSales.sort_values(by=['Global_Sales'], ascending=False)
fig, ax = plt.subplots(figsize=(23, 8))
ax.set_title('Type de jeu le plus vendu', fontsize=30, loc='center', fontdict=dict(weight='bold'))
sns.barplot(x="Genre", y="Global_Sales", data=dsGenreSales)
st.pyplot(fig)

# Et enfin une dernière partie dite « visualisation personnalisable » qui permettra de :
# * Sélectionner le type de graphique à tracer
# Sélectionner des colonnes dans le jeux de données afin de générer le graphique
# * **(bonus)**À noter que suivant certain jeux de données il y aura des graphiques qui n’auront pas de sens capturez les dans des exceptions

selectedColumns = st.selectbox("Selectionner les colonnes", ['Heatmap', 'Bar', 'Line'])
st.write(selectedColumns)
dfSelectedForGraph = multiSelectColumns()
