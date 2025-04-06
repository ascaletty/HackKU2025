import csv
import os
import sys 
file_name = sys.argv[1]
def personal_data():

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
        
    age = int(input("Age: ").strip())

    academic_pressure = int(input("Academic Pressure (1-5)(int)): ").strip())


    CGPA_raw = float(input("What is your GPA(4.0 Scale): ").strip())
    CGPA = CGPA_raw / 4.0 * 10 

    Study_Satisfaction = int(input("How satisfied are you with your studying? (1-5)): ").strip())

    Sleep_hours_raw = float(input("How many hours a night do you sleep?: ").strip())

    if Sleep_hours_raw < 5:
        Sleep_hours = 1
    elif Sleep_hours_raw < 6.5:
        Sleep_hours = 2
    elif Sleep_hours_raw < 8:
        Sleep_hours = 3
    elif Sleep_hours_raw >8:
        Sleep_hours = 4
    else:
        print("Invalid input. Please enter a number")


    Diet = None
    while Diet is None:
        Diet = input("Is your diet (U)nhealthy, (H)ealthy, or (M)oderate?: ").strip().upper()
        if Diet == "U":
            Diet = 1
        elif Diet == "M":
            Diet = 2
        elif Diet == "H":
            Diet = 3
        else:
            print("Invalid input. Please enter 'U', 'H', or 'M'.")
            Diet = None
        
    Suicidal_Thoughts = None
    while Suicidal_Thoughts is None:
        Suicidal_Thoughts = input("Have you ever experienced suicidal thoughts (Y/N): ").strip().upper()
        if Suicidal_Thoughts == "Y":
            Suicidal_Thoughts = 1
        elif Suicidal_Thoughts == "N":
            Suicidal_Thoughts = 0
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")
            Suicidal_Thoughts = None
        
    Study_hours = int(input("How many hours a week do you study? (int): ").strip())

    financial_pressure = int(input("How much financial pressure are you experiencing? (1-5)(int)): ").strip())

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
        gender, age, academic_pressure, CGPA, Study_Satisfaction, Sleep_hours, Diet, Suicidal_Thoughts, Study_hours,
        financial_pressure, family_mental_illness, Depression
    ]
    
    # Save data to a CSV file
    file_exists = os.path.isfile(file_name)
    with open(file_name, "a", newline="") as file:
        writer = csv.writer(file)
        # Write header only if the file is new
        if not file_exists:
            writer.writerow([
                "Gender", "Age", "Academic Pressure", "CGPA",
                "Study Satisfaction", "Sleep Hours", "Diet",
                "Suicidal Thoughts", "Study Hours", "Financial Pressure",
                "Family Mental Illness", "Depression"
            ])
        writer.writerow(data)
    
    return data

# Collect and save data
Terrys_data = personal_data()
