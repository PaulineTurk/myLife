import streamlit as st
from datetime import datetime, timedelta
import pandas as pd

st.title("📅 Votre vie en cases")
st.write("Visualisez chaque jour de votre vie potentielle jusqu'à 100 ans")

# Input de la date de naissance
birth_date = st.date_input(
    "Entrez votre date de naissance",
    value=datetime(1990, 1, 1),
    min_value=datetime(1920, 1, 1),
    max_value=datetime.today()
)

if birth_date:
    # Date actuelle
    today = datetime.today().date()

    # Calcul des jours
    birth_datetime = datetime.combine(birth_date, datetime.min.time()).date()
    days_lived = (today - birth_datetime).days
    total_days = 100 * 365  # 100 ans approximatifs
    days_remaining = total_days - days_lived

    # Statistiques
    st.write(f"**Jours vécus :** {days_lived:,} jours")
    st.write(f"**Âge actuel :** {days_lived / 365:.1f} ans")
    st.write(f"**Jours restants (jusqu'à 100 ans) :** {days_remaining:,} jours")
    st.write(f"**Pourcentage de vie vécue :** {(days_lived / total_days * 100):.1f}%")

    st.write("---")

    # Options d'affichage
    display_mode = st.radio(
        "Mode d'affichage",
        ["Semaines (plus compact)", "Jours (détaillé)"],
        index=0
    )

    if display_mode == "Semaines (plus compact)":
        # Affichage par semaines
        total_weeks = 100 * 52  # 5200 semaines
        weeks_lived = days_lived // 7

        st.write(f"**Semaines vécues :** {weeks_lived} / {total_weeks}")

        # Créer le tableau de semaines
        weeks_per_row = 52
        rows = 100

        html = '<div style="display: grid; grid-template-columns: repeat(52, 10px); gap: 2px; margin-top: 20px;">'

        for i in range(total_weeks):
            if i < weeks_lived:
                color = "#000000"  # Noir pour les semaines passées
            else:
                color = "#e0e0e0"  # Gris clair pour les semaines futures

            html += f'<div style="width: 10px; height: 10px; background-color: {color}; border: 1px solid #ccc;" title="Semaine {i+1}"></div>'

        html += '</div>'
        html += f'<p style="margin-top: 20px; font-size: 12px;">Chaque carré = 1 semaine | Noir = passé | Gris = futur</p>'

        st.markdown(html, unsafe_allow_html=True)

    else:
        # Affichage par jours (limité pour ne pas surcharger)
        st.warning("⚠️ Mode jours : Affichage limité aux 10 premières années pour des raisons de performance")

        days_to_show = min(10 * 365, total_days)
        days_per_row = 365

        html = '<div style="display: grid; grid-template-columns: repeat(365, 3px); gap: 1px; margin-top: 20px;">'

        for i in range(days_to_show):
            if i < days_lived:
                color = "#000000"
            else:
                color = "#e0e0e0"

            html += f'<div style="width: 3px; height: 3px; background-color: {color};"></div>'

        html += '</div>'
        html += f'<p style="margin-top: 20px; font-size: 12px;">Chaque carré = 1 jour (10 premières années affichées) | Noir = passé | Gris = futur</p>'

        st.markdown(html, unsafe_allow_html=True)

st.write("---")
st.caption("💡 Cette visualisation vous aide à prendre conscience du temps qui passe et de l'importance de chaque jour.")