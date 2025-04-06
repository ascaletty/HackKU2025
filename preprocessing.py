import pandas as pd #Im using pandas to read the csv file
import sys 
file_path = sys.argv[1]
depression_data = pd.read_csv('reprocessed_data.csv') 
#print(depression_data.head()) #This is just to see the first 5 rows of the data.
#Here I am creating a variable called depression_data and using the pandas library to read the csv file.
#I don't know how to update the path to make it work for everyone so for yours just put in your own path, the file is in the github.

import seaborn as sns # I am using seaborn to create the correlation heatmap.
import matplotlib.pyplot as plt # for the plotting
numerical_depression_data = depression_data.select_dtypes(include=['int64', 'float64']) 
#This is a new variable to select only the numerical data types from the depression_data variable.

#depression_data.drop('City',axis=1, inplace=True)
#print(depression_data)
correlation_matrix = numerical_depression_data.corr()  # Calculate the correlation matrix

# Plot the heatmap
'''
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='cubehelix_r', fmt='.2f')
plt.title('Correlation Matrix')
plt.show()
'''

#Terry's Branch
from sklearn.ensemble import RandomForestClassifier  # Import RandomForestClassifier
from sklearn.metrics import accuracy_score  # Import accuracy_score

# Define features (X) and target (y)
X = depression_data.drop(columns=['Depression'])  # Replace 'Depression' with the actual target column name
y = depression_data['Depression']  # Replace 'Depression' with the actual target column name


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

import pickle as pk
pk.dump(model, open('rfcmodel.pkl', 'wb')) #This is to save the model in a pickle file.

# Load Terry's data with the correct header
terrys_depression_data = pd.read_csv(file_path, header=0)  # Ensure the first row is treated as the header
print("Terry's Data (After Loading):")
print(terrys_depression_data)

# Check if the dataset is empty
if terrys_depression_data.empty:
    raise ValueError("Terry's data is empty. Please check the CSV file.")

# Rename columns to match the training data
column_mapping = {
    "Gender": "Gender",
    "Age": "Age",
    "Academic Pressure": "Academic Pressure",
    "Work Pressure": "Work Pressure",
    "CGPA": "CGPA",
    "Study Satisfaction": "Study Satisfaction",
    "Job Satisfaction": "Job Satisfaction",
    "Sleep Hours": "Sleep Duration",  # Match training data column name
    "Diet": "Dietary Habits",  # Match training data column name
    "Suicidal Thoughts": "Have you ever had suicidal thoughts ?",  # Match training data column name
    "Study Hours": "Study Time",  # Match training data column name
    "Financial Pressure": "Financial Stress",  # Match training data column name
    "Family Mental Illness": "Family History of Mental Illness",  # Match training data column name
    "Depression": "Depression"  # Target column
}

# Apply the column mapping
terrys_depression_data.rename(columns=column_mapping, inplace=True)

# Drop the 'Depression' column if it exists
if 'Depression' in terrys_depression_data.columns:
    terrys_depression_data_without_depression = terrys_depression_data.drop(columns=['Depression'])
else:
    terrys_depression_data_without_depression = terrys_depression_data

# Ensure all columns in the training data are present in Terry's data
for col in X.columns:
    if col not in terrys_depression_data_without_depression.columns:
        print(f"Column '{col}' is missing in Terry's data. Adding it with default value 0.")
        terrys_depression_data_without_depression[col] = 0  # Add missing columns with default value

# Ensure the column order matches the training data
terrys_depression_data_without_depression = terrys_depression_data_without_depression[X.columns]

# Check if the dataset is still empty after processing
if terrys_depression_data_without_depression.empty:
    raise ValueError("Terry's data is empty after processing. Please check the input data.")

# Use the model to make predictions
terrys_depression_prediction_raw = model.predict(terrys_depression_data_without_depression)
if terrys_depression_prediction_raw == [1]:
    terrys_depression_prediction = "Yes"
else:
    terrys_depression_prediction = "No"
# Print the prediction result
print(f"Terry's Depression Prediction: {terrys_depression_prediction}")

