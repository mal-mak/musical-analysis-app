import streamlit as st
import plotly.express as px


def popularity_tab(df):
    """
    Display the 'Analyse de la Popularité' tab with a bar chart visualizing genre popularity.

    This function generates a bar chart that shows the average popularity score (from 0 to 100)
    for each genre, allowing users to compare the popularity of different music genres.

    Parameters:
    df (pandas.DataFrame): The dataframe containing the music track data, including
                            the columns 'track_genre' and 'popularity'.

    The function uses Plotly for visualizations and Streamlit to render the UI.
    """

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
