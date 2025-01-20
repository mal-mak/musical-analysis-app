import streamlit as st
from musical_analysis_app.utils.dashboard_utils import (
    load_data,
    normalize_tempo,
    on_genre_select,
)
from musical_analysis_app.dashboard_tabs.popularity_tab import popularity_tab
from musical_analysis_app.dashboard_tabs.caracteristics_tab import caracteristics_tab
from musical_analysis_app.dashboard_tabs.recommendations_tab import recommendations_tab
from musical_analysis_app.dashboard_tabs.tendances_tab import tendances_tab


def main():
    """
    The main function that sets up and runs the musical analysis dashboard.

    This function initializes the Streamlit app with a set of interactive tabs that allow users to
    explore different aspects of musical track data, including popularity, musical
    characteristics, trends, and recommendations to maximize sales.

    The function does the following:
    - Configures the page layout and title.
    - Loads the dataset and normalizes the tempo feature.
    - Displays a genre selection widget for users to highlight a specific genre.
    - Organizes and displays various analysis tabs:
        - "Popularité" (Popularity): Analyzes average popularity by genre.
        - "Caractéristiques" (Characteristics): Analyzes musical features by genre.
        - "Tendances" (Trends): Analyzes average track duration by genre.
        - "Recommandations" (Recommendations): Provides recommendations for maximizing
          track sales based on characteristics of popular tracks.

    Each tab presents its analysis using Streamlit components and Plotly charts.

    The function runs within a Streamlit app and interacts with the data using pandas,
    while also making use of Plotly for creating interactive visualizations.

    :raises ValueError: If the genre selection is invalid or data is missing.
    :return: None
    :rtype: None
    """
    # Function implementation goes here
    st.set_page_config(page_title="Dashboard Musical", page_icon="📊", layout="wide")

    st.title("Dashboard d'Analyse Musicale")

    # Chargement des données
    with st.spinner("Chargement des données..."):
        df = load_data()

    # Normalisation du tempo
    df["tempo_normalized"] = normalize_tempo(df)

    # Popularité par genre
    genre_popularity = (
        df.groupby("track_genre")["popularity"].mean().sort_values(ascending=False)
    )

    # Genre selection for highlights
    st.selectbox(
        "Sélectionner un genre",
        options=genre_popularity.index,
        key="genre_selector",
        on_change=on_genre_select,
    )

    # Tabs pour organiser les analyses
    tab1, tab2, tab3, tab4 = st.tabs(
        ["Popularité", "Caractéristiques", "Tendances", "Recommandations"]
    )

    with tab1:
        popularity_tab(df)

    with tab2:
        caracteristics_tab(df)

    with tab3:
        tendances_tab(df)

    with tab4:
        recommendations_tab(df)


if __name__ == "__main__":
    main()
