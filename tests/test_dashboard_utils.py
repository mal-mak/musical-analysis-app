import unittest
import pandas as pd
import streamlit as st
from unittest.mock import patch
from pathlib import Path
from musical_analysis_app.utils.dashboard_utils import (
    load_data,
    normalize_tempo,
    on_genre_select,
)


class TestUtils(unittest.TestCase):
    def setUp(self):
        """Initialise les données de test"""
        # Créer un DataFrame de test
        self.test_df = pd.DataFrame({"tempo": [60, 120, 180]})

        # Mock pour session_state
        if not hasattr(st, "session_state"):
            setattr(st, "session_state", {})

    def test_normalize_tempo(self):
        """Teste la fonction de normalisation du tempo"""
        # Calculer les valeurs normalisées
        normalized = normalize_tempo(self.test_df)

        # Vérifier que les valeurs sont bien normalisées entre 0 et 1
        self.assertAlmostEqual(normalized.min(), 0.0)
        self.assertAlmostEqual(normalized.max(), 1.0)
        self.assertAlmostEqual(
            normalized.iloc[1], 0.5
        )  # La valeur du milieu doit être 0.5

    @patch("pandas.read_csv")
    def test_load_data(self, mock_read_csv):
        """Teste la fonction de chargement des données"""
        # Configuration du mock
        mock_df = pd.DataFrame({"test": [1, 2, 3]})
        mock_read_csv.return_value = mock_df

        # Appeler la fonction
        result = load_data()

        # Vérifier que read_csv a été appelé
        self.assertTrue(mock_read_csv.called)

        # Vérifier que le résultat est un DataFrame
        self.assertIsInstance(result, pd.DataFrame)

        # Vérifier que le DataFrame retourné correspond à notre mock
        pd.testing.assert_frame_equal(result, mock_df)

    def test_on_genre_select(self):
        """Teste la fonction de mise à jour du genre sélectionné"""
        # Configuration du state initial
        st.session_state.genre_selector = "Rock"

        # Appeler la fonction
        on_genre_select()

        # Vérifier que le genre a été correctement copié
        self.assertEqual(st.session_state.selected_genre, "Rock")

        # Tester avec un autre genre
        st.session_state.genre_selector = "Jazz"
        on_genre_select()
        self.assertEqual(st.session_state.selected_genre, "Jazz")

    def tearDown(self):
        """Nettoie l'environnement après chaque test"""
        # Réinitialiser session_state
        if hasattr(st, "session_state"):
            st.session_state.clear()


if __name__ == "__main__":
    unittest.main()
