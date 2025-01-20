import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from musical_analysis_app.utils.features import FEATURES

features = FEATURES


def caracteristics_tab(df):
    st.header("Caractéristiques Musicales")

    col1, col2 = st.columns(2)
    with col1:
        selected_feature = st.selectbox(
            "Choisir une caractéristique", list(features.keys())
        )
        feature_by_genre = (
            df.groupby("track_genre")[selected_feature]
            .mean()
            .sort_values(ascending=False)
        )

        # Highlight the selected genre
        color_discrete_map = {
            genre: (
                "red" if genre == st.session_state.get("genre_selector") else "blue"
            )
            for genre in feature_by_genre.index
        }
        fig2 = px.bar(
            feature_by_genre,
            title=f"{features[selected_feature]} par genre",
            labels={"value": features[selected_feature], "track_genre": "Genre"},
            color=feature_by_genre.index,
            color_discrete_map=color_discrete_map,
        )
        st.plotly_chart(fig2)

    with col2:
        radar_features = [f for f in features.keys() if f != "tempo"]
        selected_genre = st.session_state.get("genre_selector")
        genre_stats = (
            df[df["track_genre"] == selected_genre][radar_features].mean()
            if selected_genre
            else pd.Series(0, index=radar_features)
        )

        fig_radar = go.Figure()
        fig_radar.add_trace(
            go.Scatterpolar(
                r=genre_stats.values,
                theta=genre_stats.index,
                fill="toself",
                name=(selected_genre if selected_genre else "Aucun genre sélectionné"),
                marker=dict(color="red"),
                text=[
                    f"{feature}: {value:.2f}" for feature, value in genre_stats.items()
                ],
                hoverinfo="text",  # Show text on hover
            )
        )
        fig_radar.update_layout(
            polar=dict(radialaxis=dict(range=[0, 1])),
            title=f"Profil musical du genre {selected_genre if selected_genre else 'Aucun'}",
        )
        st.plotly_chart(fig_radar)
