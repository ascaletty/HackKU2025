import kagglehub
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import string
import re
import time
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn
start= time.perf_counter()
end= time.perf_counter()
elapsed = start - end
# Download latest version
path = kagglehub.dataset_download("thedevastator/c-ssrs-labeled-suicidality-in-500-anonymized-red")

print("Path to dataset files:", path)
data_pre= pd.read_csv('/home/ascaletty23/.cache/kagglehub/datasets/thedevastator/c-ssrs-labeled-suicidality-in-500-anonymized-red/versions/2/500_anonymized_Reddit_users_posts_labels - 500_anonymized_Reddit_users_posts_labels.csv')
list_labels = data_pre['Label'].unique()

print(list_labels)
data_pre['Label'] = data_pre['Label'].replace('Indicator', 0)
data_pre['Label'] = data_pre['Label'].replace('Supportive', 1)
data_pre['Label'] = data_pre['Label'].replace('Behavior', 2)
data_pre['Label'] = data_pre['Label'].replace('Ideation', 3)
data_pre['Label'] = data_pre['Label'].replace('Attempt', 4)
data_pre['Post']= data_pre['Post'].str.lower()
data_pre['Post'].str.replace('[{}]'.format(string.punctuation), '')
print(data_pre)







print(f"Elapsed time: {elapsed} seconds")




