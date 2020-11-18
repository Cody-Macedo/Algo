import streamlit as st
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# run app with: streamlit run app.py
# dfVgSales = pd.read_csv("csv/vgsales.csv")
# dfCac40 = pd.read_csv("csv/CAC40.csv")
st.title("Dataframe")

st.sidebar.title("Video Games / CAC40")


def file_selector(folder_path='csv/'):
    filenames = os.listdir(folder_path)
    selected_filename = st.sidebar.selectbox('Choisissez votre csv: ', filenames)
    return os.path.join(folder_path, selected_filename)


filename = file_selector()
st.write('Vous avez choisis: `%s`' % filename)
dfCurrent = pd.read_csv(filename)

# Afficher le dataset chargé suivant un nombre de ligne entrées par l’utilisateur

st.title("Données datagrame")
st.header("Choisir le nombre de donnée à afficher")
vgSalesNbInput = st.number_input("Entrer le nombre de donnée affiché: ", 1)
if st.button("Afficher les données"):
    st.table(dfCurrent.head(vgSalesNbInput))

# Afficher le nom des colonnes du dataset
st.header("Affichage du nom des colonnes du dataset")
st.write(dfCurrent.columns.tolist())

# Afficher le type des colonnes du dataset ainsi que les colonnes sélectionnées
st.header("Affichage du type des colonnes")
# checkBoxes = [st.checkbox(i, key=i) for i in dfCurrent]
# print('checkBoxes: ' + checkBoxes.__str__())

if st.button("Afficher tous les types"):
    st.write(dfCurrent.dtypes)
    st.write('à finir')

columns = dfCurrent.columns.tolist()
selectedColumns = st.multiselect("Selectionner les colonnes", columns)
dfSelected = dfCurrent[selectedColumns]

if st.button("Afficher les types séléctionné"):
    st.write(dfSelected.dtypes)

# La shape du dataset, par lignes et par colonnes
st.header("Affichage du shape")
st.write('Colonnes: ', dfCurrent.shape[1])
st.write('Lignes: ', dfCurrent.shape[0])

# Afficher les statistiques descriptives du dataset
st.header("Affichage des statistiques")
st.write(dfCurrent.describe())

# Afficher plusieurs type de graphique dans une partie visualisation avec notamment :
# * Une heatmap des corrélations avec Matplotlib et Seaborn (avec les valeurs annotés)
st.header("Affichage des Graphes:")
st.write("Heatmap")
if st.button("Afficher le graphe heatmap"):
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(dfCurrent.corr(), cmap="BuPu", annot=True)
    st.pyplot(fig)

# * Un graphique en barres afin de visualiser la taille du dataset par caractéristiques (on pourra notamment grouper les données afin d’avoir des graphiques plus précis) données afin d’avoir des graphiques plus précis)
# dsGenreSales = dfCurrent[['Genre', 'Global_Sales']].copy()
# dsGenreSales = dsGenreSales.groupby(['Genre']).sum()
# dsGenreSales = dsGenreSales.reset_index()
# dsGenreSales = dsGenreSales.sort_values(by=['Global_Sales'], ascending=False)
st.write("Barre")
sb = st.selectbox("Selectionner les colonnes pour le graphe", columns)
dfSelectedOneCol = dfCurrent[sb]
if st.button("Afficher le graphe en barre"):
    fig, ax = plt.subplots(figsize=(23, 8))
    sns.countplot(data=dfSelectedOneCol)
    st.pyplot(fig)


# Et enfin une dernière partie dite « visualisation personnalisable » qui permettra de :
# * Sélectionner le type de graphique à tracer
# Sélectionner des colonnes dans le jeux de données afin de générer le graphique
# * **(bonus)**À noter que suivant certain jeux de données il y aura des graphiques qui n’auront pas de sens capturez les dans des exceptions

def graphBar(df):
    fig, ax = plt.subplots(figsize=(22, 8))
    sns.barplot(data=df)
    st.pyplot(fig)


def graphHeatmap(df):
    fig, ax = plt.subplots(figsize=(22, 8))
    sns.heatmap(data=df)
    st.pyplot(fig)


def graphRelplot(df):
    fig, ax = plt.subplots(figsize=(22, 8))
    sns.relplot(data=df)
    st.pyplot(fig)


st.header("Graph select")
typeGraph = st.selectbox("Selectionner les colonnes", ['Heatmap', 'Bar', 'Line'])
st.write(typeGraph)

sc = st.multiselect("Selectionner les colonnes pour le graphe", columns)
dfSelectedToGraph = dfCurrent[sc]

if st.button("Afficher le graphe"):
    try:
        if typeGraph == "Heatmap":
            print("Heatmap")
            graphHeatmap(dfSelectedToGraph)
        if typeGraph == "Bar":
            print("Bar")
            graphBar(dfSelectedToGraph)
        if typeGraph == "Line":
            print("Line")
            graphRelplot(dfSelectedToGraph)
        else:
            print('not exist')
    except ValueError:
        print("error: " + ValueError)
