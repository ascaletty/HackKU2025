import kagglehub
import polars as pl
import numpy as np
import matplotlib.pyplot as plt
import string
import re
import time
import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn

#pl.set_option('future.no_silent_downcasting', True)
start= time.perf_counter()
end= time.perf_counter()
elapsed = start - end
# Download latest version
path = kagglehub.dataset_download("thedevastator/c-ssrs-labeled-suicidality-in-500-anonymized-red")

print("Path to dataset files:", path)
df= pl.read_csv('/home/ascaletty23/.cache/kagglehub/datasets/thedevastator/c-ssrs-labeled-suicidality-in-500-anonymized-red/versions/2/500_anonymized_Reddit_users_posts_labels - 500_anonymized_Reddit_users_posts_labels.csv')
list_labels = df['Label'].unique()
#print(df)
df['Label'] = df['Label'].replace_strict('Indicator', 0)
df['Label'] = df['Label'].replace_strict('Supportive', 1)
df['Label'] = df['Label'].replace_strict('Behavior', 2)
df['Label'] = df['Label'].replace_strict('Ideation', 3)
df['Label'] = df['Label'].replace_strict('Attempt', 4)
df['Post']= df['Post'].str.lower()
df['Post'] = df['Post'].str.replace(',',' ')
df['Post'] = df['Post'].str.replace('.',' ')
df['Post'] = df['Post'].str.replace(';',' ')
df['Post']= df['Post'].apply(word_tokenize)

print(df)
example_entry=df['Post'][0]
print(f"example: {example_entry}")






print(f"Elapsed time: {elapsed} seconds")




