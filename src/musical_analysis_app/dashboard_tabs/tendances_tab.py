import streamlit as st
import plotly.express as px


def tendances_tab(df):
    """
    Display the 'Analyse des Tendances' tab with insights on the average duration
    of tracks by genre, helping identify trends in track length across genres.

    This function calculates and visualizes the average track duration for each genre
    and highlights the selected genre for comparison. The analysis helps to uncover
    trends in the duration of tracks that might be associated with genre-specific
    popularity or success.

    Parameters:
    df (pandas.DataFrame): The dataframe containing the music track data, including
                            the 'track_genre' and 'duration_ms' columns.

    The function uses Streamlit to display a bar chart showing the average track duration
    by genre, with a specific color for the genre selected by the user.
    """
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
