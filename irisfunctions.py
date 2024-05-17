import matplotlib.pyplot as plt
import numpy as np



def datasummary(listoftuples):
    with open('Irisdatasummary.txt', 'w') as ivd: #function starts by creating a file called irisdatasummary which we will write to
        for name, df in listoftuples:
            description = df.describe()
            ivd.write(f"Here is a description of the variable {name}:\n")
            ivd.write(description.to_string())
            ivd.write("\n\n")

        

def irisdatahist(data, xlabel, title, filename):
    plt.hist(data, bins=10, color='yellow', edgecolor='black')
    plt.xlabel(xlabel)
    plt.ylabel('No. of Iris Flowers')
    plt.title(title)
    plt.savefig(filename)
    plt.show()

def irisscatter(variablecombinations):
    for (name1, df1), (name2, df2) in variablecombinations:
        plt.figure()  # Create a new figure for each scatter plot
        plt.scatter(df1, df2)
        plt.xlabel(name1)
        plt.ylabel(name2)
        plt.title(f"{name1} vs {name2}")
        plt.show()


