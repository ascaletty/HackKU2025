import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier  
from sklearn.metrics import accuracy_score  
import pickle as pk
from sklearn.model_selection import train_test_split, KFold, cross_val_score 
depression_data = pd.read_csv('reprocessed_data.csv')

X = depression_data.drop(columns=['Depression'])  # Replace 'Depression' with the actual target column name
y = depression_data['Depression']  # Replace 'Depression' with the actual target column name

def RFPredictionModel():

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    return [model, accuracy]

def RFPredictionModelWithKFold():

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    kf = KFold(n_splits=10, shuffle=True, random_state=42)  
    cv_scores = cross_val_score(model, X, y, cv=kf, scoring='precision')
    
    return [model, cv_scores.mean(), cv_scores.std()]


my_model = RFPredictionModelWithKFold()
print(my_model[1])