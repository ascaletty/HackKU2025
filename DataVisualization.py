import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#If we are to print the csv outright there are no restrictions on number of rows or columns
pd.set_option('display.max_rows', None, 'display.max_columns', None)

df = pd.read_csv("Preprocssed_data.csv") #df unprocessed
dfp = pd.read_csv("reprocessed_data.csv") #df processed

def main():
    choice = 0
    while (choice >= 0):
        print_menu()
        try:
            choice = int(input("Enter your choice: "))
        except:
            print("Please enter an integer.")
            choice = 0
        choice_handler(choice)

def choice_handler(choice):
    if choice == 1:
        heat_map()

def print_menu():
    print("\nChoices: ")
    print("\tCorrelation Heatmap (1)")
    print("\tExit program (-1)\n")

def heat_map():
    corrs = df.corr(numeric_only=True)
    plt.subplots(figsize=(10, 8))
    sns.heatmap(corrs, annot=True, vmin=-1, vmax=1)
    plt.show()

def bar_graph():
    corrs = df.corr(numeric_only=True)
    bar_data = get_bar_data()
    plt.bar

def get_bar_data(catagory, min, max):
    ...


main()