import streamlit as st
import plotly.express as px


def tendances_tab(df):
    st.header("Analyse des Tendances")

    duration_by_genre = df.groupby("track_genre")["duration_ms"].mean() / 1000
    color_discrete_map = {
        genre: "red" if genre == st.session_state.get("genre_selector") else "blue"
        for genre in duration_by_genre.index
    }
    fig_duration = px.bar(
        duration_by_genre,
        title="Durée moyenne par genre",
        labels={"value": "Durée (secondes)", "track_genre": "Genre"},
        color=duration_by_genre.index,
        color_discrete_map=color_discrete_map,
    )
    st.plotly_chart(fig_duration)
