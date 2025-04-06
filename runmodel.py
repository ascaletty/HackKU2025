import pickle as pk
import pandas as pd
def runmodel(file_name):
    model= pk.load(open('models/naive_bayes.pkl', 'rb'))
    df= pd.read_csv(file_name)
    df.columns =["0","1","2","3","4","5","6","7","8","9","10","11"]
    userdf= df.drop('11', axis=1)
    depression_prediction_raw= model.predict(userdf)
    if depression_prediction_raw == 1:
        depression_prediction = True
        return depression_prediction
    else:
        depression_prediction = False
        return depression_prediction
