import os

import pandas as pd


def main():
    files = os.listdir(os.path.join(os.getcwd(), "data/attendance"))
    for file in files:
        anonymize("data/attendance/" + file)
    concat(files)


def anonymize(path):
    """
    removes sensitive information inplace from the csv files.
    Needed this function only once and only kept it here for record purpose
    """
    attendance = pd.read_csv(path)

    try:
        attendance.drop(
            columns=[
                "Email address",
                "What did you learn in class today that you didn’t know about before\
                     or it wasn’t clear before?",
                "Name of team lead",
                "Timestamp",
            ],
            inplace=True,
        )

        attendance.to_csv(path)
    except KeyError:
        print("Skipped file")


def concat(files):
    frames = []
    for file in files:
        attendance = pd.read_csv("data/attendance/" + file)
        frames.append(attendance)

    combined_attendance = pd.concat(frames)
    combined_attendance["Full name"] = combined_attendance["Full name"].str.lower()
    combined_attendance.sort_values(by="Full name", inplace=True)
    combined_attendance.pop(combined_attendance.columns[0])

    combined_attendance.to_csv("data/attendance/combined.csv")


if __name__ == "__main__":
    main()
