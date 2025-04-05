import kagglehub
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import string
import re
import time 
start= time.perf_counter()
end= time.perf_counter()
elapsed = start - end
# Download latest version
path = kagglehub.dataset_download("thedevastator/c-ssrs-labeled-suicidality-in-500-anonymized-red")

print("Path to dataset files:", path)
data_pre= pd.read_csv('/home/ascaletty23/.cache/kagglehub/datasets/thedevastator/c-ssrs-labeled-suicidality-in-500-anonymized-red/versions/2/500_anonymized_Reddit_users_posts_labels - 500_anonymized_Reddit_users_posts_labels.csv')
print(data_pre)
list_labels = data_pre['Label'].unique()

print(list_labels)
df['Label'] = df['Label'].replace('Supportive', 2)
df['Label'] = df['Lable'].str.replace('Ideation', 4)



print(f"Elapsed time: {elapsed} seconds")




