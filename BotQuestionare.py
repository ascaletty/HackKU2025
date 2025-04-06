import csv
import os
import sys
import discord
import pandas as pd


def questionaire(message):
    file_name = "questionaredata/" + message.author + ".csv"
    file = open(file_name)
    file.readline()
    data = file.readline().strip().split(',')
    print(data)

    gender = None
    while gender is None:
        gender_string = input("What is your Gender: M, F or (O)ther: ").strip().upper()
        if gender_string == "M":
            gender = 1
        elif gender_string == "F":
            gender = 0
        elif gender_string == "O":
            gender = 0
        else:
            print("Invalid input. Please enter 'M' or 'F' or 'O'.")
            gender = None

    age = None
    while (age is None):
        try:
            age = int(input("Age: ").strip())
            if age < 0:
                raise
        except:
            print("Please enter a positive number.")
            age = None

    academic_pressure = None
    while (academic_pressure is None):
        try:
            academic_pressure = int(input("Academic Pressure (1-5)(int)): ").strip())
            if (academic_pressure > 5 or academic_pressure < 1):
                raise
        except:
            print("Please enter a number between 1 and 5.")
            academic_pressure = None

    CGPA = None
    while (CGPA is None):
        try:
            CGPA = float(input("What is your GPA(4.0 Scale): ").strip())
            if (CGPA < 0 or CGPA > 4):
                raise
            CGPA = CGPA / 4.0 * 10
        except:
            print("Please enter a positive number.")
            CGPA = None

    study_satisfaction = None
    while (study_satisfaction is None):
        try:
            study_satisfaction = int(input("study_satisfaction (1-5)(int)): ").strip())
            if (study_satisfaction > 5 or study_satisfaction < 1):
                raise
        except:
            print("Please enter a number between 1 and 5.")
            study_satisfaction = None

    sleep_hours_raw = float(input("How many hours a night do you sleep?: ").strip())
    while (sleep_hours_raw is None):
        try:
            sleep_hours_raw = int(input("Academic Pressure (1-5)(int)): ").strip())
            if (sleep_hours_raw > 24 or sleep_hours_raw < 0):
                raise
        except:
            print("Please enter a number between 0 and 24.")
            sleep_hours_raw = None

    if sleep_hours_raw < 5:
        Sleep_hours = 1
    elif sleep_hours_raw < 6.5:
        Sleep_hours = 2
    elif sleep_hours_raw < 8:
        Sleep_hours = 3
    elif sleep_hours_raw > 8:
        Sleep_hours = 4
    else:
        print("Invalid input. Please enter a number")

    diet = None
    while diet is None:
        diet = input("Is your diet (U)nhealthy, (H)ealthy, or (M)oderate?: ").strip().upper()
        if diet == "U":
            diet = 1
        elif diet == "M":
            diet = 2
        elif diet == "H":
            diet = 3
        else:
            print("Invalid input. Please enter 'U', 'H', or 'M'.")
            diet = None

    suicidal_thoughts = None
    while suicidal_thoughts is None:
        suicidal_thoughts = input("Have you ever experienced suicidal thoughts (Y/N): ").strip().upper()
        if suicidal_thoughts == "Y":
            suicidal_thoughts = 1
        elif suicidal_thoughts == "N":
            suicidal_thoughts = 0
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")
            suicidal_thoughts = None

    study_hours = None
    while (study_hours is None):
        try:
            study_hours = int(input("How many hours a week do you study? (int): ").strip())
            if study_hours < 0:
                raise
        except:
            print("Please enter a positive number.")
            study_hours = None

    financial_pressure = None
    while (financial_pressure is None):
        try:
            financial_pressure = int(input("How much financial pressure are you experiencing? (1-5)(int)): ").strip())
            if (financial_pressure > 5 or financial_pressure < 1):
                raise
        except:
            print("Please enter a number between 1 and 5.")
            financial_pressure = None

    family_mental_illness = None
    while family_mental_illness is None:
        family_mental_illness = input("Do you have a history of family mental illness? (Y/N): ").strip().upper()
        if family_mental_illness == 'Y':
            family_mental_illness = 1
        elif family_mental_illness == 'N':
            family_mental_illness = 0
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")
            family_mental_illness = None

    Depression = None
    while Depression is None:
        Depression = input("Are you currently diagnosed with depression? (Y/N): ").strip().upper()
        if Depression == 'Y':
            Depression = 1
        elif Depression == 'N':
            Depression = 0
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")
            Depression = None

    data = [
        gender, age, academic_pressure, CGPA, study_satisfaction, Sleep_hours, diet, suicidal_thoughts, study_hours,
        financial_pressure, family_mental_illness, Depression
    ]

    with open("questionaredata/" + file_name, "a", newline="") as file:
        writer = csv.writer(file)
        # Write header only if the file is new
        
        writer.writerow(data)


def add_to_file(file_name, data):
    file_exists = os.path.isfile("questionaredata/" + file_name)
    file = open("questionaredata/" + file_name, 'a')
    if not file_exists:
        file.write("Gender, Age, Academic Pressure, CGPA,")
        file.write("Study Satisfaction, Sleep Hours, Diet,")
        file.write("Suicidal Thoughts, Study Hours, Financial Pressure,")
        file.write("Family Mental Illness, Depression\n")
    else:
        file.write(",")
    file.write(str(data))
    file.close()
