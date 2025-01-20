import streamlit as st
from musical_analysis_app.utils.dashboard_utils import on_genre_select
import plotly.express as px


def popularity_tab(df):

    st.header("Analyse de la Popularité")

    # Popularité par genre
    genre_popularity = (
        df.groupby("track_genre")["popularity"].mean().sort_values(ascending=False)
    )

    comment = """
    # Genre selection with callback
    def on_genre_select():
        st.session_state.selected_genre = st.session_state.genre_selector
"""
    # Add genre selection
    selected_genre = st.selectbox(
        "Sélectionner un genre",
        options=genre_popularity.index,
        key="genre_selector",
        on_change=on_genre_select,
    )

    # Create color map based on selected genre
    color_discrete_map = {
        genre: "red" if genre == st.session_state.get("genre_selector") else "blue"
        for genre in genre_popularity.index
    }

    # Create bar chart
    fig1 = px.bar(
        genre_popularity,
        title="Popularité moyenne par genre",
        labels={"value": "Popularité (0-100)", "track_genre": "Genre"},
        color=genre_popularity.index,
        color_discrete_map=color_discrete_map,
    )

    fig1.update_layout(
        yaxis_range=[0, 100],
        showlegend=False,
    )

    st.plotly_chart(fig1, use_container_width=True)
