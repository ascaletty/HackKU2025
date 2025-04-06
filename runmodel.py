import pickle as pk
import pandas as pd
def runmodel(file_name):
    model= pk.load(open('models/randomforestmodel.pkl', 'rb'))
    df= pd.read_csv("questionaredata/"+ file_name)
    df.columns =["0","1","2","3","4","5","6","7","8","9","10","11"]
    userdf= df.drop('11', axis=1)
    depression_prediction_raw= model.predict(userdf)
    print(userdf)
    if depression_prediction_raw == 1:
        depression_prediction = True
        return depression_prediction
        print(depression_prediction)
    else:
        depression_prediction = False
        print(depression_prediction)
        return depression_prediction
file_name='test.csv'
runmodel(file_name)
