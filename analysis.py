# Analysis of the Iris Data set


# 3. Outputs a scatter plot of each pair of variables.
# 4. Performs any other analysis you think is appropriate.
# Author: Myles Henehan

# Importing the relevant libraries for this project
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Reading in our dataset
file = 'iris/iris.data' # we will assign the path of our dataset to the variable "file"
df = pd.read_csv(file, header=None) # we then use the .read_csv function from pandas to read in our data. 
# Since there are no headers, we want the data from the first row, hence "Header=None".
print(df) # as a test, let's print it. This will result in the first and last five rows being printed.

# Since there are no headers in the source we've used, let's assign each data frame to a header.
sepallen = df[0]
sepalwidth = df[1]
petallen = df[2]
petalwidth = df[3]
species = df[4]

# Project Aim 1: Output a summary of each variable to a single text file.

# To simplify this, I have created a function called datasummary

variablelist = [sepallen, sepalwidth, petallen, petalwidth] # let's first make a list of our data frames so they are easy to manipulate.
names = ["sepallen", "sepalwidth", "petallen", "petalwidth"]

from irisfunctions import datasummary 

datasummary(variablelist, names)




# Project Aim 2: Save a Histogram of each variable to png files.

# To simplify this, I have created a function called irisdatahist.
# This function reads in the variable, the x label, the title of the histogram and the file name to be saved to. It creates a histogram and saves it as a png with this file name.

from irisfunctions import irisdatahist

#Sepal Length
irisdatahist(sepallen, 'Sepal length (cm)', 'Sepal Length of Iris Flowers', 'sepallen_histogram.png')

# Sepal Width
irisdatahist(sepalwidth, 'Sepal width (cm)', 'Sepal Width of Iris Flowers', 'sepalwidth_histogram.png')

# Petal Length
irisdatahist(petallen, 'Petal length (cm)', 'Petal Length of Iris Flowers', 'petallen_histogram.png')

# Petal Width
irisdatahist(petalwidth, 'Petal width (cm)', 'Petal Width of Iris Flowers', 'petalwidth_histogram.png')
    

# Project Aim 3: Output a scatter plot of each pair of variables

