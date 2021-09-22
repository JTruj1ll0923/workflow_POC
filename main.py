# import json
import pandas as pd


class Notes:
    def __init__(self):
        pass

    steps = []
    notes = []

    def add_notes(self, note_to_add):
        if note_to_add != 'nan':
            self.notes.append(note_to_add.replace('\n', ''))

    def print_notes(self):
        for note in self.notes:
            print(note, end=" ")


def step(data, notes, option=""):
    choice = ""
    if option == "":
        option = "A00"
    if data[option]["reason"] == "Resolved":
        notes.add_notes(data[option]["notes"])
        return "Resolved"
    elif data[option]["reason"] == "Not Created Yet":
        return "Not Created Yet"
    print(data[option]["process"])
    # print(data[option]["reason"])
    option1 = str(data[option]["option1"]).split(sep=";")
    option2 = str(data[option]["option2"]).split(sep=";")
    notes.add_notes(str(data[option]["notes"]))
    while choice is not option1[0] or choice is not option2[0]:
        try:
            choice = input(f"{option1[0]} or {option2[0]}")
            if choice == option1[0]:
                return option1[1]
            elif choice == option2[0]:
                return option2[1]
        except:
            print("Try again")


def main():
    data = pd.read_json("steps.json")
    notes = Notes()
    resolved = False
    resolutions = ["Resolved", "Not Created Yet"]
    choice = ""
    while not resolved:
        choice = step(data, notes, choice)
        if choice in resolutions:
            resolved = True
            notes.print_notes()


if __name__ == '__main__':
    main()
