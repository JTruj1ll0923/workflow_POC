# import json
import pandas as pd


def step(data, option=""):
    choice = ""
    if option == "":
        option = "A00"
    print(data[option]["process"])
    # print(data[option]["reason"])
    option1 = str(data[option]["option1"]).split(sep=";")
    option2 = str(data[option]["option2"]).split(sep=";")
    while choice is not option1[0] or choice is not option2[0]:
        try:
            choice = input(f"{option1[0]} or {option2[0]}")
            if choice == option1[0]:
                return option1[1]
            elif choice == option2[0]:
                return option2[1]
        except:
            "Try again"


def main():
    data = pd.read_json("steps.json")
    resolved = False
    choice = ""
    while not resolved:
        choice = step(data, choice)
    # print(data["A02A"]["process"])
    # print(data)


if __name__ == '__main__':
    main()
