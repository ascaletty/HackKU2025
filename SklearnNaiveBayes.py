import pandas as pd
from sklearn.datasets import load_iris
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import MinMaxScaler
from sklearn.naive_bayes import GaussianNB
df= pd.read_csv('reprocessed_data.csv')
df= df.drop('Job Satisfaction',axis=1)
df= df.drop('Work Pressure',axis=1)
df.columns =["0","1","2","3","4","5","6","7","8","9","10","11"]
ct = ColumnTransformer(
        [()]
        )
i=0
while i < 11:
    j= str(i)
    ct = ColumnTransformer(
        [("numpreprocess",MinMaxScaler(),[j])]
        )
    df[j] = ct.fit_transform(df)
    i += 1




X= df.drop('11', axis=1)
print(X)
y= df['11']
print(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)
gnb = GaussianNB()
y_pred = gnb.fit(X_train, y_train).predict(X_test)
#print("Number of mislabeled points out of a total %d points : %d" (X_test.shape[0], (y_test != y_pred).sum()))
print(df)
