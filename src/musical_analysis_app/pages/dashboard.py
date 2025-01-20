import streamlit as st
import pandas as pd
import plotly.express as px
import os
from pathlib import Path

def load_data():
    """Charge le dataset Spotify depuis le fichier local"""
    data_dir = Path(__file__).parent.parent / "data"
    data_file = data_dir / "spotify_tracks.csv"
    
    return pd.read_csv(data_file)

def main():
    st.set_page_config(page_title="Dashboard Musical", page_icon="📊", layout="wide")
    
    st.title("Dashboard d'Analyse Musicale")

    # Chargement des données
    with st.spinner('Chargement des données...'):
        df = load_data()

    # 1. Analyse des genres musicaux et leur popularité
    st.header("Popularité par Genre Musical")
    genre_popularity = df.groupby('track_genre')['popularity'].mean().sort_values(ascending=False)
    fig1 = px.bar(genre_popularity, 
                  title="Popularité moyenne par genre")
    st.plotly_chart(fig1)

    # 2. Caractéristiques des morceaux par genre
    st.header("Caractéristiques par Genre")
    features = ['danceability', 'energy', 'tempo']
    selected_feature = st.selectbox("Choisir une caractéristique", features)
    
    feature_by_genre = df.groupby('track_genre')[selected_feature].mean().sort_values(ascending=False)
    fig2 = px.bar(feature_by_genre,
                  title=f"{selected_feature.capitalize()} moyenne par genre")
    st.plotly_chart(fig2)

    # 3. Corrélation popularité/caractéristiques
    st.header("Impact des Caractéristiques sur la Popularité")
    correlation = df[features + ['popularity']].corr()['popularity'].sort_values(ascending=False)
    fig3 = px.bar(correlation,
                  title="Corrélation avec la popularité")
    st.plotly_chart(fig3)

    # Conclusions
    st.header("Conclusions")
    st.write("""
    - Les genres les plus populaires sont...
    - Les caractéristiques qui influencent le plus la popularité sont...
    - Recommandations pour maximiser les ventes...
    """)

if __name__ == "__main__":
    main() 