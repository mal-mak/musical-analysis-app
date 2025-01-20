import pandas as pd
from pathlib import Path
import streamlit as st


def load_data():
    """Charge le dataset Spotify depuis le fichier local"""
    data_dir = Path(__file__).parent.parent / "data"
    data_file = data_dir / "spotify_tracks.csv"
    return pd.read_csv(data_file)


def normalize_tempo(df):
    """Normalise le tempo entre 0 et 1"""
    tempo_min = df["tempo"].min()
    tempo_max = df["tempo"].max()
    return (df["tempo"] - tempo_min) / (tempo_max - tempo_min)


def on_genre_select():
    """Met à jour le genre sélectionné dans la session state de Streamlit.

    Cette fonction est utilisée comme callback pour le selectbox de sélection de genre.
    Elle copie la valeur du genre sélectionné depuis genre_selector vers selected_genre
    dans le session state de Streamlit.

    Note:
        Requiert que st.session_state.genre_selector soit déjà initialisé.
    """
    st.session_state.selected_genre = st.session_state.genre_selector
