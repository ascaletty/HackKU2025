import kagglehub
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import string
import re
# Download latest version
start_time = time.perf_counter()
end_time= time.perf_counter()
elapsed_time= end_time -start_time
path = kagglehub.dataset_download("thedevastator/c-ssrs-labeled-suicidality-in-500-anonymized-red")

print("Path to dataset files:", path)
data_csv= pd.read_csv('/home/ascaletty23/.cache/kagglehub/datasets/thedevastator/c-ssrs-labeled-suicidality-in-500-anonymized-red/versions/2/500_anonymized_Reddit_users_posts_labels - 500_anonymized_Reddit_users_posts_labels.csv')
print(data_csv)
print(f"Elapsed Time: {elapsed_time} seconds")



