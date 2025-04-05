import pandas as pd #Im using pandas to read the csv file

depression_data = pd.read_csv(r'c:\Users\terry\OneDrive\Desktop\HackKU25\Preprocssed_data.csv') 
#Here I am creating a variable called depression_data and using the pandas library to read the csv file.
#I don't know how to update the path to make it work for everyone so for yours just put in your own path, the file is in the github.

import seaborn as sns # I am using seaborn to create the correlation heatmap.
numerical_depression_data = depression_data.select_dtypes(include=['int64', 'float64']) 
#This is a new variable to select only the numerical data types from the depression_data variable.
# hi


