import streamlit as st
import plotly.express as px
from musical_analysis_app.utils.features import FEATURES

features = FEATURES


def recommendations_tab(df):
    st.header("Recommandations pour Maximiser les Ventes")

    # Calcul des caractéristiques optimales basées sur les titres populaires
    popular_tracks = df[df["popularity"] > df["popularity"].quantile(0.75)]
    optimal_features = popular_tracks[list(features.keys())].mean()

    st.write("### Caractéristiques des titres à succès")
    for feature, value in optimal_features.items():
        st.metric(label=features.get(feature, feature), value=f"{value:.2f}")

    st.write("### Conclusions")
    st.write(
        """
    Pour maximiser les chances de succès, considérez :
    1. Les genres les plus populaires
    2. Les caractéristiques moyennes des titres à succès
    3. La durée optimale pour chaque genre
    """
    )
