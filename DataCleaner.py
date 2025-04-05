import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score
from imblearn.under_sampling import RandomUnderSampler
import joblib

pd.set_option('display.max_rows', None, 'display.max_columns', None)

df = pd.read_csv("Preprocssed_data.csv")

#df.describe().to_csv('output.csv', index=False)

df["Gender"] = df["Gender"].replace({"Male": 1, "Female": 0})

df_selected = df[["Gender", "Age", "Academic Pressure", "Work Pressure", "CGPA", "Study Satisfaction", "Job Satisfaction", "Sleep Duration", "Dietary Habits", "Have you ever had suicidal thoughts ?", "Work/Study Hours", "Financial Stress", "Family History of Mental Illness", "Depression"]]

df_selected.to_csv('reprocessed_data.csv', index=False)
