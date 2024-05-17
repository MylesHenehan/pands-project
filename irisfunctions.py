import matplotlib.pyplot as plt
import numpy as np



def datasummary(listoftuples):
    with open('Irisdatasummary.txt', 'w') as ivd: #function starts by creating a file called irisdatasummary which we will write to
        for name, df in listoftuples:
            description = df.describe()
            ivd.write(f"Here is a description of the variable {name}:\n")
            ivd.write(description.to_string())
            ivd.write("\n\n")


def irisdatahist(listoftuples):
    for name, df in listoftuples:
        plt.hist(df, bins=10, color='yellow', edgecolor='black')
        plt.xlabel(f"{name} (cm)")
        plt.ylabel('Quantity')
        plt.title(f"{name} of Iris flowers")
        plt.savefig(f"{name}.png")
        plt.show()

def irisscatter(variablecombinations):
    for (name1, df1), (name2, df2) in variablecombinations:
        plt.figure()  # Create a new figure for each scatter plot
        plt.scatter(df1, df2)
        plt.xlabel(name1)
        plt.ylabel(name2)
        plt.title(f"{name1} vs {name2}")
        plt.show()

