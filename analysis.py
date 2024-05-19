# Analysis of the Iris Dataset
# Author: Myles Henehan

# Importing the relevant libraries for this project
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import itertools as it

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

variablelist = [("Sepal Length", sepallen), ("Sepal Width", sepalwidth), ("Petal Length", petallen), ("Petal Width", petalwidth)] # let's first make a list of our data frames so they are easy to manipulate.


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

import itertools as it #this module is very helpful as it contains the .combinations() function, which allows us to get all the combinations of our variables.
varcombinations = it.combinations(variablelist, 2)

from irisfunctions import irisscatter
irisscatter(varcombinations)

# Project Aim 4: Other useful analyses

# Best Fit line:
#m, c = np.polyfit(petallen, petalwidth, 1) # The .polyfit function takes a set of data points (x, y) and fits a polynomial of specified degree to the data. The degree 1 here represents a straight line.
#m, c # Here, "m" represents the slope, while "c" represents the intercept of the line. Let's make this clear for ease of reference by assigning them to more easy-to-understand variables.

#slope = m
#intercept = c
#print(f'Slope: {slope}')
#print(f'Intercept: {intercept}')

#fig, ax = plt.subplots()
#ax.plot(petallen, petalwidth, 'x')
#ax.plot(petallen, slope * petallen + intercept, 'r-') #This time we're adding another plot command to insert our best fit line, with "r-" representing a solid red line.
#ax.set_xlabel('Petal Length (cm)')
#ax.set_ylabel('Petal Width (cm)')
#plt.show()

# Pearson Correlation Coefficient
#r = petallen.corr(petalwidth) # .corr() is a pandas function which calculates correlation between two data frames, using the Pearson correlation coefficient by default.
#print("Pearson correlation coefficient:", r)


from irisfunctions import bestfit
print("To see the best fit line for any combination of variables, please choose the corresponding number")
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

