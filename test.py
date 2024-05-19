# to try out creating a function that reads in 2 data frames and creates the best fit line for them.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import itertools as it

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

variablelist = [("Sepal Length", sepallen), ("Sepal Width", sepalwidth), ("Petal Length", petallen), ("Petal Width", petalwidth)]


def bestfit(x,y):

    m, c = np.polyfit(x, y, 1) # The .polyfit function takes a set of data points (x, y) and fits a polynomial of specified degree to the data. The degree 1 here represents a straight line.
    m, c # Here, "m" represents the slope, while "c" represents the intercept of the line. Let's make this clear for ease of reference by assigning them to more easy-to-understand variables.

    slope = m
    intercept = c
    print(f'Slope: {slope}')
    print(f'Intercept: {intercept}')

    fig, ax = plt.subplots()
    ax.plot(x, y, 'x')
    ax.plot(x, slope * x + intercept, 'r-') #This time we're adding another plot command to insert our best fit line, with "r-" representing a solid red line.
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    plt.show()