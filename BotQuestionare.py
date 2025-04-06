import csv
import os
import sys
import asyncio
import discord
import pandas as pd
from runmodel import runmodel

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
            return

        file.readline()
        data = file.readline().strip().split(',')
        data_length = len(data)
        if data[0] == '':
            i_data = await gender(message) # input data gathers whatever data is needed
            if i_data is not None:
                add_to_file(file_name, i_data)
        elif data_length == 1:
            i_data = await age(message)
            if i_data is not None:
                add_to_file(file_name, i_data)
        elif data_length == 2:
            i_data = await academic_pressure(message)
            if i_data is not None:
                add_to_file(file_name, i_data)
        elif data_length == 3:
            i_data = await CGPA(message)
            if i_data is not None:
                add_to_file(file_name, i_data)
        elif data_length == 4:
            i_data = await study_satisfaction(message)
            if i_data is not None:
                add_to_file(file_name, i_data)
        elif data_length == 5:
            i_data = await sleep_hours(message)
            if i_data is not None:
                add_to_file(file_name, i_data)
        elif data_length == 6:
            i_data = await diet(message)
            if i_data is not None:
                add_to_file(file_name, i_data)
        elif data_length == 7:
            i_data = await suicidal_thoughts(message)
            if i_data is not None:
                add_to_file(file_name, i_data)
        elif data_length == 8:
            i_data = await study_hours(message)
            if i_data is not None:
                add_to_file(file_name, i_data)
        elif data_length == 9:
            i_data = await financial_pressure(message)
            if i_data is not None:
                add_to_file(file_name, i_data)
        elif data_length == 10:
            i_data = await family_mental_illness(message)
            if i_data is not None:
                add_to_file(file_name, i_data)
        elif data_length == 11:
            i_data = await depression(message)
            if i_data is not None:
                add_to_file(file_name, i_data)
                result = runmodel(file_name)
                if result:
                    await message.author.send('You at risk for depression, here are some resources to get a much more '
                                              'accurate diagnose, along with understanding potential symptoms:\n'
                                              'https://www.nimh.nih.gov/health/publications/depression')
                elif not result:
                    await message.author.send('You are at a low risk of depression')
                file.close()
                os.remove(file_name)
        elif data_length == 12:
            file.close()
            os.remove(file_name)





async def intro(message):
    await message.author.send("Hi! I'm DepressoBot, your friendly AI depression indicator!\n"
                              "But before we test you using our machine learning powered questionare, but first, "
                              "there's something we need to discuss\n"
                              "THIS IS NOT A MEDICAL DIAGNOSIS. This is just a fun questionare made for HACKKU25")
    await message.author.send("First question: what is your gender? Please respond M, F, or O")


#Question 1
async def gender(message):
    if message.content.strip().upper() == "M":
        gender_i = 1
        await message.author.send("Now, what's your age?")
    elif message.content.strip().upper() == "F":
        gender_i = 0
        await message.author.send("Now, what's your age?")
    elif message.content.strip().upper() == "O":
        gender_i = 0
        await message.author.send("Now, what's your age?")
    else:
        await message.author.send("Invalid answer, try again!")
        await message.author.send("First question: what is your gender? Please respond M, F, or O")
        gender_i = None

    return gender_i

#Question 2
async def age(message):
    try:
        age = int(message.content.strip())
        if(age < 0 or age > 123):
            raise
        await message.author.send("Alright, now how pressured do you feel to perform well academically from 1-5?")
    except:
        await message.author.send("Please enter a positive age as a whole number.")
        await message.author.send("Now, what's your age?")
        age = None

    return age

#Question 3
async def academic_pressure(message):
    try:
        academic_pressure = int(message.content.strip())
        if (academic_pressure > 5 or academic_pressure < 1):
            raise
        await message.author.send("What is your current GPA? (4.0 Scale)")
    except:
        await message.author.send("I'm sorry, please enter a whole number from 1 to 5")
        await message.author.send("Alright, now how pressured do you feel to perform well academically from 1-5?")
        academic_pressure = None
    
    return academic_pressure

#Question 4
async def CGPA(message):
    try:
        CGPA = float(message.content.strip())
        if (CGPA < 0 or CGPA > 4):
                raise
        CGPA = CGPA / 4.0 * 10
        await message.author.send("Ok, from a scale of 1-5 how satisfied would you say you currently are about your studies?")
    except:
        await message.author.send("Please enter a valid GPA on the 4.0 scale (0.0 - 4.0).")
        await message.author.send("What is your current GPA? (4.0 Scale)")
        CGPA = None

    return CGPA

#Question 5
async def study_satisfaction(message):
    try:
        study_satisfaction = int(message.content.strip())
        if (study_satisfaction > 5 or study_satisfaction < 1):
            raise
        await message.author.send("How many hours do you sleep per night?")
    except:
        await message.author.send("I'm sorry, please enter a whole number from 1 to 5")
        await message.author.send("Ok, from a scale of 1-5 how satisfied would you say you currently are about your studies?")
        study_satisfaction = None
    
    return study_satisfaction

#Question 6
async def sleep_hours(message):
    try:
        sleep_hours_raw = int(message.content.strip())
        if (sleep_hours_raw > 24 or sleep_hours_raw < 0):
            raise

        if sleep_hours_raw < 5:
            sleep_hours = 1
        elif sleep_hours_raw < 6.5:
            sleep_hours = 2
        elif sleep_hours_raw <= 8:
            sleep_hours = 3
        elif sleep_hours_raw > 8:
            sleep_hours = 4
        else:
            raise

        await message.author.send("Now, how would you describe your diet, (U)unhealthy, (M)oderate, or (H)ealthy?")
    except:
        await message.author.send("Enter a valid number.")
        await message.author.send("How many hours do you sleep per night?")
        sleep_hours = None
    
    return sleep_hours

#Question 7
async def diet(message):
    content = message.content.strip().upper()
    try:
        if content == 'U':
            diet = 1
        elif content == 'M':
            diet = 2
        elif content == 'H':
            diet = 3
        else:
            raise
        await message.author.send("Have you ever experienced suicidal thoughts (Y/N).")

    except:
        await message.author.send("Invalid input, please enter either a U, M, or H")
        await message.author.send("Now, how would you describe your diet, (U)unhealthy, (M)oderate, or (H)ealthy?")
        diet = None

    return diet

#Question 8
async def suicidal_thoughts(message):
    content = message.content.strip().upper()
    try:
        if content == "Y":
            suicidal_thoughts = 1
        elif content == "N":
            suicidal_thoughts = 0
        else:
            raise
        await message.author.send("Alright, now how many hours a week do you spend on studying?")
    except:
        await message.author.send("Please enter either a Y or an N.")
        await message.author.send("Have you ever experienced suicidal thoughts (Y/N).")
        suicidal_thoughts = None

    return suicidal_thoughts

#Question 9
async def study_hours(message):
    try:
        study_hours = int(message.content.strip())
        if(study_hours < 0 or study_hours > 168):
            raise
        await message.author.send("From a scale from 1-5, how much financial pressure are you under?")
    except:
        await message.author.send("Please enter a positive whole number.")
        await message.author.send("Alright, now how many hours a week do you spend on studying?")
        study_hours = None

    return study_hours

#Question 10
async def financial_pressure(message):
    try:
        financial_pressure = int(message.content.strip())
        if (financial_pressure > 5 or financial_pressure < 1):
            raise
        await message.author.send("Does your family have a history of depression (Y/N)?")
    except:
        await message.author.send("I'm sorry, please enter a whole number from 1 to 5")
        await message.author.send("From a scale from 1-5, how much financial pressure are you under?")
        financial_pressure = None
    
    return financial_pressure

#Question 11
async def family_mental_illness(message):
    content = message.content.strip().upper()
    try:
        if content == "Y":
            family_mental_illness = 1
        elif content == "N":
            family_mental_illness = 0
        else:
            raise
        await message.author.send("Finally, are you currently diagnosed with depression? (Y/N)")
    except:
        await message.author.send("Please enter either a Y or an N.")
        await message.author.send("Does your family have a history of depression (Y/N)?")
        family_mental_illness = None

    return family_mental_illness

#Question 12
async def depression(message):
    content = message.content.strip().upper()
    try:
        if content == "Y":
            depression = 1
        elif content == "N":
            depression = 0
        else:
            raise
        await message.author.send("Thank you very much.")
    except:
        await message.author.send("Please enter either a Y or an N.")
        await message.author.send("Finally, are you currently diagnosed with depression? (Y/N)")
        depression = None

    return depression

#Function to append new data to a users csv file
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
