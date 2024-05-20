# Analysis of the Iris Dataset
# Author: Myles Henehan

# Importing the relevant libraries for this project
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import itertools as it # this module is very helpful as it contains the .combinations() function, which allows us to get all the combinations of our variables. We will use this for our scatter plots.

# Reading in our dataset
file = 'iris/iris.data' # we will assign the path of our dataset to the variable "file"
df = pd.read_csv(file, header=None) # we then use the .read_csv function from pandas to read in our data. 
# Since there are no headers, we want the data from the first row, hence "Header=None".
print(df) # as a test, let's print it. This will result in the first and last five rows being printed.

# Since there are no headers in the source we've used, let's assign each data frame to a variable:
sepallen = df[0]
sepalwidth = df[1]
petallen = df[2]
petalwidth = df[3]
species = df[4]

# let's first make a list of our data frames so they are easy to manipulate.
variablelist = [
    ("Sepal Length", sepallen), 
    ("Sepal Width", sepalwidth), 
    ("Petal Length", petallen), 
    ("Petal Width", petalwidth)
]


# Project Aim 1: Output a summary of each variable to a single text file.

# To simplify this, I have created a function called datasummary, which uses the describe() function.

from irisfunctions import datasummary 
datasummary(variablelist)






# Project Aim 2: Save a Histogram of each variable to png files.

# To simplify this, I have created a function called irisdatahist.
# This function reads in the variable, the x label, the title of the histogram and the file name to be saved to. It creates a histogram and saves it as a png with this file name.

from irisfunctions import irisdatahist
irisdatahist(variablelist)
    





# Project Aim 3: Output a scatter plot of each pair of variables
varcombinations = it.combinations(variablelist, 2)

from irisfunctions import irisscatter
irisscatter(varcombinations)



# Project Aim 4: Other useful analyses

# Best Fit Line
from irisfunctions import bestfit
print("To see the best fit line for a combination of variables, please choose the corresponding numbers.")
x = input("Please input your first variable: \n\n1.Sepal Length\n\n2.Sepal Width\n\n3.Petal Length\n\n4.Petal Width\n\n")
y = input("\n\nPlease input your second variable: \n\n1.Sepal Length\n\n2.Sepal Width\n\n3.Petal Length\n\n4.Petal Width\n\n")

if x == str(1):
    xvar = petallen
elif x == str(2):
    xvar = petalwidth
elif x == str(3):
     xvar = sepallen
elif x == str(4):
    xvar = sepalwidth

if y == str(1):
    yvar = petallen
elif y == str(2):
     yvar = petalwidth
elif y == str(3):
    yvar = sepallen
elif y == str(4):
    yvar = sepalwidth

bestfit(xvar,yvar)


# Pearson Correlation Coefficient
r = xvar.corr(yvar) # .corr() is a pandas function which calculates correlation between two data frames, using the Pearson correlation coefficient by default.
print("Pearson correlation coefficient:", r)



# The hidden variable
grouped = df.groupby(4) # The easiest way to showcase this is to use a .groupby() function (OpenAI, 2024)
for species, data in grouped:
    plt.hist(data[2], bins=10, alpha=0.5, label=species)
plt.legend()
plt.xlabel('Petal Length')
plt.ylabel('Frequency')
plt.title('Histogram of Petal Length by Species')
plt.show()