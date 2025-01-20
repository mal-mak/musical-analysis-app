import streamlit as st

def main():
    st.set_page_config(
        page_title="Musical Analysis Tool",
        page_icon="🎵",
    )

    st.title("🎵 Malmak's Musical Analysis Interactive Tool")
    
    st.write("""
    Bienvenue dans notre application d'analyse musicale, conçue pour 
    aider les producteurs de musique à identifier les tendances qui maximisent 
    les ventes.
    """)

    st.write("""
    Notre dashboard vous permet d'explorer :
    - Les genres musicaux les plus populaires
    - Les caractéristiques des morceaux à succès
    - Les tendances actuelles du marché
    """)

    if st.button("Accéder au Dashboard 📊"):
        st.switch_page("pages/dashboard.py")

if __name__ == "__main__":
    main() 