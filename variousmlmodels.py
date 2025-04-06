# Imports
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier  
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split, KFold, cross_val_score
import pickle as pk
import sys
#file_path = sys.argv[1]
#with open("questionaredata/"+file_path)
 #   userdf = pd.read_csv("questionaredata/" +file_path)
#userdfnodep= userdf.drop('11', axis=1)

# Load dataset 
depression_data = pd.read_csv('reprocessed_data.csv')
X = depression_data.drop(columns=['Depression'])  # Features
y = depression_data['Depression']  # Target


def LogisticRegressionModel():
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    model = LogisticRegression(random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Logistic Regression Accuracy: {accuracy:.2f}")
    return model


def SVMModel():
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    model = SVC(kernel='rbf', random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"SVM Accuracy: {accuracy:.2f}")
    return model


def KNNModel():
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    model = KNeighborsClassifier(n_neighbors=5)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"KNN Accuracy: {accuracy:.2f}")
    return model


def DecisionTreeModel():
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Decision Tree Accuracy: {accuracy:.2f}")
    return model

# Naive Bayes
def NaiveBayesModel():
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    model = GaussianNB()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Naive Bayes Accuracy: {accuracy:.2f}")
    return model


def NeuralNetworkModel():
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    model = MLPClassifier(hidden_layer_sizes=(100,), max_iter=500, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Neural Network Accuracy: {accuracy:.2f}")
    return model

def RFPredictionModel():

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)

    return [model, accuracy, precision]

def RFPredictionModelWithKFold():

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    kf = KFold(n_splits=10, shuffle=True, random_state=42)  
    cv_scores = cross_val_score(model, X, y, cv=kf, scoring='accuracy')
    
    return [model, cv_scores.mean(), cv_scores.std()]

def main():
    # Train and evaluate models
    logistic_model = LogisticRegressionModel()
    svm_model = SVMModel()
    knn_model = KNNModel()
    decision_tree_model = DecisionTreeModel()
    naive_bayes_model = NaiveBayesModel()
    neural_network_model = NeuralNetworkModel()
    rf_model = RFPredictionModel()
    
main()
