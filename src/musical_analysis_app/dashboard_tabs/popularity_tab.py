import streamlit as st
import plotly.express as px


def popularity_tab(df):

    st.header("Analyse de la Popularité")

    # Popularité par genre
    genre_popularity = (
        df.groupby("track_genre")["popularity"].mean().sort_values(ascending=False)
    )

    color_discrete_map = {
        genre: "red" if genre == st.session_state.get("genre_selector") else "blue"
        for genre in genre_popularity.index
    }

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
