import csv
import os
import sys
import asyncio
import discord
import pandas as pd


async def questionnaire(message):
    if message.guild is not None:
        await intro(message)
    else:  # if the message is a dm
        file_name = "questionaredata/" + message.author.name + ".csv"
        try:
            file = open(file_name)
        except FileNotFoundError:
            g_data = await gender(message)
            if g_data is not None:
                add_to_file(file_name, g_data)
                return

        file.readline()
        data = file.readline().strip().split(',')
        data_length = len(data)
        if data[0] == '':
            g_data = await gender(message)
            if g_data is not None:
                add_to_file(file_name, g_data)
        elif data_length == 1:
            print('cool')




async def intro(message):
    await message.author.send("Hi! I'm DepressoBot, your friendly AI depression indicator!\n"
                              "But before we test you using our machine learning powered questionare, but first, "
                              "there's something we need to discuss\n"
                              "THIS IS NOT A MEDICAL DIAGNOSIS. This is just a fun questionare made for HACKKU25")
    await message.author.send("First question: what is your gender? Please respond M, F, or O")



async def gender(message):
    if message.content.strip() == "M":
        gender_i = 1
        await message.author.send("Now, what's your age?")
    elif message.content.strip() == "F":
        gender_i = 0
        await message.author.send("Now, what's your age?")
    elif message.content.strip() == "O":
        gender_i = 0
        await message.author.send("Now, what's your age?")
    else:
        await message.author.send("Invalid answer, try again!")
        await message.author.send("First question: what is your gender? Please respond M, F, or O")
        gender_i = None

    return gender_i



# async def age:
#     age = None
#     while (age is None):
#         try:
#             age = int(input("Age: ").strip())
#             if age < 0:
#                 raise
#         except:
#             print("Please enter a positive number.")
#             age = None

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
    file_exists = os.path.isfile(file_name)
    file = open(file_name, 'a')
    if not file_exists:
        file.write("Gender, Age, Academic Pressure, CGPA,")
        file.write("Study Satisfaction, Sleep Hours, Diet,")
        file.write("Suicidal Thoughts, Study Hours, Financial Pressure,")
        file.write("Family Mental Illness, Depression\n")
    else:
        file.write(",")
    file.write(str(data))
    file.close()