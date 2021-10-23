import pandas as pd
import streamlit as st

st.title("Cohort 7 Leaderboard")

teams = [
    "Annan",
    "Johnson-Sirleaf",
    "Kaunda",
    "Kenyatta",
    "Konare",
    "Lumumba",
    "Maathai",
    "Machel",
    "Makeba",
    "Mandela",
    "Nkrumah",
    "Nyerere",
    "Ransome-Kuti",
    "Sankara",
    "Selassie",
]

for team in teams:
    with st.expander("Team " + team):
        teampd = pd.read_csv("data/" + team + ".csv")
        st.dataframe(teampd)
