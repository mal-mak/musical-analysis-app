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
