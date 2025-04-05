import pandas as pd #Im using pandas to read the csv file

depression_data = pd.read_csv('reprocessed_data.csv') 
print(depression_data.head()) #This is just to see the first 5 rows of the data.
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

