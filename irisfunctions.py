import matplotlib.pyplot as plt
import numpy as np


def datasummary(listofvars, names):
    with open('Irisdatasummary.txt', 'w') as ivd: #function starts by creating a file called irisdatasummary which we will write to
        for l in listofvars:
            ivd.write(f"Here is a description of the variable {str(names)}:\n")
            description = l.describe()
            ivd.write(description.to_string())
            ivd.write("\n\n")

        

def irisdatahist(data, xlabel, title, filename):
    plt.hist(data, bins=10, color='yellow', edgecolor='black')
    plt.xlabel(xlabel)
    plt.ylabel('No. of Iris Flowers')
    plt.title(title)
    plt.savefig(filename)
    plt.show()


def scatterplots(x_variable, y_variables, irisdict): #Create scatter plots with each variable as the x-axis against the specified y variables.
    
   # Parameters:
    #    x_variable (str): The variable to use as the x-axis.
    #    y_variables (list of str): The list of variables to use as the y-axis.
    #    irisdict (dict): The dictionary containing the Iris dataset.
   
    # Create a figure with subplots
    fig, axs = plt.subplots(1, len(y_variables), figsize=(15, 5))
    
    # Plot each variable against the x_variable
    for i, var in enumerate(y_variables):
        axs[i].scatter(irisdict[x_variable], irisdict[var])
        axs[i].set_xlabel(x_variable)
        axs[i].set_ylabel(var)
        axs[i].set_title(f"{x_variable} vs {var}")
    
    # Adjust layout
    plt.tight_layout()
    
    # Show the plot
    plt.show()


