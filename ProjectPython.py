# Imported parameters
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


# Variables
NumberOfModels = int(input("How many models you want to compare  ? "))
NumberOfStats = int(input("How many stats of models you want to compare ? "))
listOfStats = []
StatsOfModels = {}
Models = []

# Data reading

# Data sorting

# Functions

def CreateApropriateLists():
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
# Conclusions()