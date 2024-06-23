# Imported parameters
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import csv

# Variables
# NumberOfModels = int(input("How many models you want to compare  ? "))
# NumberOfStats = int(input("How many stats of models you want to compare ? "))
# listOfStats = []
# StatsOfModels = {}
# Models = []

# Data reading

data = pd.read_csv('Apple.csv',sep=";")

"""data = pd.DataFrame(
    {'Price': [1000, 750, 500], "Repairs cost": [500, 200, 400], 'Longevity': [5, 3, 5], 'FPS': [90, 60, 30],
     'Year': [2024, 2023, 2010], 'Company': ['Apple', "Samsung", "Xiomi"], 'Pixels': [10000, 4900, 4000]})
data.head()"""

# Slice
# print(data.query('Company == "Apple"'))

# General information about dataset and how much nulls are in there
"""data.info()
data.isnull().sum()
"""
# Histograms
"""
data["Price"].hist()
data["Repairs cost"].hist()
data["Longevity"].hist()
data["FPS"].hist()
data["Year"].hist()
data["Company"].hist()
data["Pixels"].hist()
"""

# data["Model"].query('data["Model"] == "iPad"').value_counts()

# Deleting useless info
# data = data.drop(["Model name"], axis = 1)

# Describing general information of models
print(data["Price"].min(), data["Price"].max(), data["Price"].median())

# Directly removing nulls in data
data = data.mask(data.eq("None")).dropna()

# Data graphing
data_2 = pd.DataFrame(data).reindex(columns=["Model", "Price", "Year"])
data_Max_Prices = data_2.sort_values(["Model", "Price", "Year"], ascending=[False,False, False]).drop_duplicates(["Model"]).reset_index(drop=True)
# data_Max_FPS = data_2.sort_values(["Model","Max_FPS"], ascending=[False,False]).drop_duplicates(["Model"]).reset_index(drop=True)
# data_Year = data_2.sort_values(["Year","Price"], ascending=[False, False]).drop_duplicates(["Year"]).reset_index(drop=True)
# data_Price = data_2.sort_values(["Model","Max_FPS"], ascending=[False, False]).drop_duplicates(["Model"]).reset_index(drop=True)

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 8))

axes[0, 0].bar(data_Max_Prices["Model"], data_Max_Prices["Price"], color='lightblue', ec='darkblue')
axes[0, 0].set_ylabel("Price")
axes[0, 0].set_title("Bar diagram", fontsize=10)

axes[0, 1].scatter(data_Max_Prices["Year"], data_Max_Prices["Price"] )
axes[0, 1].grid(True)
axes[0, 1].set_ylabel("Price")
axes[0, 1].set_title("Scatter diagram", fontsize=10)

axes[1, 0].pie(data["Model"].value_counts(), labels=data["Model"].unique() )
axes[1, 0].set_title("Pie chart", fontsize=10)
axes[1, 0].legend()

# axes[1, 1].set_ylabel("Max FPS")
axes[1, 1].set_title("Hist diagram", fontsize=10)

plt.tight_layout()
plt.show()

# Functions
"""def CreateApropriateLists():
    arg = 0
    while arg < NumberOfModels:
        NameOfModel = input("What is the name of compared model ? ")
        Models.append(NameOfModel)
        arg += 1
    print(Models)


def MakingStats():
    arg = 0
    i = 0
    while arg < len(Models):
        StatsOfModels[Models[arg]] = []
        arg += 1
    while i < NumberOfStats:
        listOfStats.append(input("What is the name of stat for chosen Models"))
        i += 1
    print(StatsOfModels)
    print(listOfStats)

    for argum in Models:
        for element in listOfStats:
            StatsOfModels[argum].append(float(input(f"What is numerical value for  {element} of {argum} ? ")))
    print(StatsOfModels)


def CreateGraph():
    barLabels = Models[:]
    i = 0
    while i < NumberOfStats:
        listOfStats.append(input("What is the name of stat for chosen Models"))
        i += 1

    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 8))
    Y_axis_0 = []
    Y_axis_1 = []
    Y_axis_2 = []
    Y_axis_3 = []

    #Data distrubution
    i = 0
    while i < 5:
        Y_axis_0.append(StatsOfModels[listOfStats[i]][0])
        Y_axis_1.append(StatsOfModels[listOfStats[i]][1])
        Y_axis_2.append(StatsOfModels[listOfStats[i]][2])
        Y_axis_3.append(StatsOfModels[listOfStats[i]][3])
        i += 1

    # Bar Plot 1
    axes[0, 0].bar(barLabels, Y_axis_0, color='blue')
    axes[0, 0].set_title(f'{listOfStats[0]}')

    # Bar Plot 2
    axes[0, 1].bar(barLabels, Y_axis_1, color='orange')
    axes[0, 1].set_title(f'{listOfStats[1]}')

    # Bar Plot 3
    axes[1, 0].bar(barLabels, Y_axis_2, color='green')
    axes[1, 0].set_title(f'{listOfStats[2]}')

    # Bar Plot 4
    axes[1, 1].bar(barLabels, Y_axis_3, color='red')
    axes[1, 1].set_title(f'{listOfStats[3]}')

    # Adjusting layout
    plt.tight_layout()

    # Show the plots
    plt.show()


def Conclusions():
    # Data
    Y_axis_0 = StatsOfModels[listOfStats[0]]
    Y_axis_1 = StatsOfModels[listOfStats[1]]
    Y_axis_2 = StatsOfModels[listOfStats[2]]
    Y_axis_3 = StatsOfModels[listOfStats[3]]

    # Maximum
    print(f"Maximum stat {listOfStats[0]} = {max(Y_axis_0)} has {Models[StatsOfModels[listOfStats[3]].index(max(Y_axis_0))]}")
    print(f"Maximum stat {listOfStats[1]} = {max(Y_axis_1)} has {Models[StatsOfModels[listOfStats[3]].index(max(Y_axis_1))]}")
    print(f"Maximum stat {listOfStats[2]} = {max(Y_axis_2)} has {Models[StatsOfModels[listOfStats[3]].index(max(Y_axis_2))]}")
    print(f"Maximum stat {listOfStats[3]} = {max(Y_axis_3)} has {Models[StatsOfModels[listOfStats[3]].index(max(Y_axis_3))]}")

    #Minimum
    print(f"Minimum stat {listOfStats[0]} = {min(Y_axis_0)} has {Models[StatsOfModels[listOfStats[3]].index(max(Y_axis_0))]}")
    print(f"Minimum stat {listOfStats[1]} = {min(Y_axis_1)} has {Models[StatsOfModels[listOfStats[3]].index(max(Y_axis_1))]}")
    print(f"Minimum stat {listOfStats[2]} = {min(Y_axis_2)} has {Models[StatsOfModels[listOfStats[3]].index(max(Y_axis_2))]}")
    print(f"Minimum stat {listOfStats[3]} = {min(Y_axis_3)} has {Models[StatsOfModels[listOfStats[3]].index(max(Y_axis_3))]}")

    #Best of many
    max_model_0 = Models[StatsOfModels[listOfStats[3]].index(max(Y_axis_0))]
    max_model_1 = Models[StatsOfModels[listOfStats[3]].index(max(Y_axis_1))]
    max_model_2 = Models[StatsOfModels[listOfStats[3]].index(max(Y_axis_2))]
    max_model_3 = Models[StatsOfModels[listOfStats[3]].index(max(Y_axis_3))]
    Max_list = [max_model_0, max_model_1, max_model_2, max_model_3]
    Max_set = {max_model_0, max_model_1, max_model_2, max_model_3}
    Best_of_many = set(Max_list).difference(Max_set)
    print(f"Model that has most best attributes is {Best_of_many}")



CreateApropriateLists()
MakingStats()
CreateGraph()
Conclusions()
"""
