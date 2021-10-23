import matplotlib.pyplot as plt
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

number_of_classes = 6


def sortTeam():
    team_dict = {}
    for team in teams:
        teampd = pd.read_csv("data/" + team + ".csv")
        _, _, _, team_score = get_team_score(teampd)
        team_dict[team] = team_score
    sortedTeam = sorted(team_dict.items(), key=lambda x: x[1], reverse=True)
    return sortedTeam


def main(teams):
    for team in teams:
        with st.expander("Team " + team[0]):
            teampd = pd.read_csv("data/" + team[0] + ".csv")
            team_commit, team_task, team_attendance, team_score = get_team_score(teampd)

            st.header("Team Score: " + str(team_score) + "%")

            col1, col2, col3 = st.columns(3)
            col1.metric(label="Commit", value=str(team_commit))
            col2.metric(label="Completed Task", value=str(team_task))
            col3.metric(label="Total Attendance", value=str(team_attendance))
            st.dataframe(teampd)

            # Number of Commit plot
            fig, ax = plt.subplots()
            plt.ylabel("Number of Commits")
            plt.xticks(rotation=45, ha="right")
            ax.bar(teampd["Name"], teampd[" Number of Commit"])
            st.pyplot(fig)

            # Task plot
            fig, ax = plt.subplots()
            plt.ylabel("Completed Tasks")
            plt.xticks(rotation=45, ha="right")
            ax.bar(teampd["Name"], teampd[" Task Completed"])
            st.pyplot(fig)

            # Attendance plot
            fig, ax = plt.subplots()
            plt.ylabel("Attendance Frequency")
            plt.xticks(rotation=45, ha="right")
            ax.bar(teampd["Name"], teampd[" Class Attendance"])
            st.pyplot(fig)


def get_team_score(team):
    team_size = team.shape[0]
    team_commit = team[team[" Number of Commit"] != 0].shape[0]
    team_task = team[team[" Task Completed"] != 0].shape[0]
    team_attendance = team[" Class Attendance"].sum()
    team_score = (
        ((team_commit / team_size) * 100)
        + ((team_task / team_size) * 100)
        + ((team_attendance / (team_size * number_of_classes)) * 100)
    ) / 3

    return team_commit, team_task, team_attendance, round(team_score)


if __name__ == "__main__":
    teams = sortTeam()
    main(teams)
