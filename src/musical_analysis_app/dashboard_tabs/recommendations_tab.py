import streamlit as st
from musical_analysis_app.utils.features import FEATURES

features = FEATURES


def recommendations_tab(df):
    st.header("Recommandations pour Maximiser les Ventes")

    # Calcul des caractéristiques optimales basées sur les titres populaires
    popular_tracks = df[df["popularity"] > df["popularity"].quantile(0.75)]
    optimal_features = popular_tracks[list(features.keys())].mean()

    # Caractéristiques optimales pour le genre sélectionné
    popular_genre = df[df['track_genre'] == st.session_state.get("genre_selector")]
    popular_genre = popular_genre[popular_genre["popularity"] > popular_genre["popularity"].quantile(0.75)]
    optimal_genre_features = popular_genre[list(features.keys())].mean()

    col1, col2 = st.columns(2)
    with col1:
        st.write("### Caractéristiques des titres à succès")
        for feature, value in optimal_features.items():
            st.metric(label=features.get(feature, feature), value=f"{value:.2f}")

    with col2:
        st.write(f"### Caractéristiques des titres à succès du genre {st.session_state.get("genre_selector")}")
        for feature, value in optimal_genre_features.items():
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
