import csv
import os

def personal_data():

    gender_entered = False
    while not gender_entered:
        gender_string = input("What is your Gender: M, F or (O)ther: ").strip().upper()
        if gender_string == "M":
            gender = 1
            gender_entered = True
        elif gender_string == "F":
            gender = 0
            gender_entered = True
        elif gender_string == "O":
            gender = 0
            gender_entered = True
        else:
            print("Invalid input. Please enter 'M' or 'F' or 'O'.")
        
    age = int(input("Age: ").strip())

    academic_pressure = int(input("Academic Pressure (1-5)(int)): ").strip())

    work_pressure = 0

    CGPA_raw = float(input("What is your GPA(4.0 Scale): ").strip())
    CGPA = CGPA_raw / 4.0 * 10 

    Study_Satisfaction = int(input("How satisfied are you with your studying? (1-5)): ").strip())

    Job_Satisfaction = 0

    Sleep_hours_raw = float(input("How many hours a night do you sleep? ").strip())

    if Sleep_hours_raw < 5:
        Sleep_hours = 1
    elif Sleep_hours_raw < 6.5:
        Sleep_hours = 2
    elif Sleep_hours_raw < 8:
        Sleep_hours = 3
    else:
        Sleep_hours = 4
    Diet_raw = input("Is your diet (U)nhealthy, (H)ealthy, or (M)oderate?: ").strip().upper()
    diet_entered = False
    while not diet_entered:
        if Diet_raw == "U":
            Diet = 1
            diet_entered = True
        elif Diet_raw == "M":
            Diet = 2
            diet_entered = True
        elif Diet_raw == "H":
            Diet = 3
            diet_entered = True
        else:
            print("Invalid input. Please enter 'U', 'H', or 'M'.")
            return None
    Suicidal_Thoughts_raw = input("Have you ever experienced suicidal thoughts (Y/N)").strip().upper()
    suicidal_thoughts_entered = False
    while not suicidal_thoughts_entered:
        if Suicidal_Thoughts_raw == "Y":
            Suicidal_Thoughts = 1
            suicidal_thoughts_entered = True
        elif Suicidal_Thoughts_raw == "N":
            Suicidal_Thoughts = 0
            suicidal_thoughts_entered = True
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")
            return None
    Study_hours = int(input("How many hours a week do you study? (int): ").strip())
    financial_pressure = int(input("How much financial pressure are you experiencing? (1-5)(int)): ").strip())
    family_mental_illness_raw = input("Do you have a history of family mental illness? (Y/N) ").strip().upper()
    family_mental_illness_entered = False
    while not family_mental_illness_entered:
        if family_mental_illness_raw == 'Y':
            family_mental_illness = 1
            family_mental_illness_entered = True
        elif family_mental_illness_raw == 'N':
            family_mental_illness = 0
            family_mental_illness_entered = True
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")
            return None
        
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
        gender, age, academic_pressure, work_pressure, CGPA, Study_Satisfaction,
        Job_Satisfaction, Sleep_hours, Diet, Suicidal_Thoughts, Study_hours,
        financial_pressure, family_mental_illness, Depression
    ]
    
    # Save data to a CSV file
    file_exists = os.path.isfile("terrys_data.csv")
    with open("terrys_data.csv", "a", newline="") as file:
        writer = csv.writer(file)
        # Write header only if the file is new
        if not file_exists:
            writer.writerow([
                "Gender", "Age", "Academic Pressure", "Work Pressure", "CGPA",
                "Study Satisfaction", "Job Satisfaction", "Sleep Hours", "Diet",
                "Suicidal Thoughts", "Study Hours", "Financial Pressure",
                "Family Mental Illness", "Depression"
            ])
        writer.writerow(data)
    
    return data

# Collect and save data
Terrys_data = personal_data()
