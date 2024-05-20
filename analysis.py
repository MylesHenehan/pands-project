# Analysis of the Iris Dataset
# Author: Myles Henehan

# Importing the relevant libraries/modules for this project
import pandas as pd # we will need this for a range of functions across the project
import matplotlib.pyplot as plt # we will need this for plotting our data.
import numpy as np # we will need this for the polyfit() function that we use for the line of best fit
import itertools as it # this module is very helpful as it contains the .combinations() function, which allows us to get all the combinations from our variable list. We will use this for our scatter plots.

# Reading in our dataset
file = 'iris/iris.data' # we first assign the path of our dataset to the variable "file"
df = pd.read_csv(file, header=None) # we then use the .read_csv function from pandas to read in our data. 
# Since there are no headers, we want the data from the first row, hence "Header=None".
print(df) # as a test, let's print it. This will result in the first and last five rows being printed.

# Since there are no headers in the source we've used, let's assign each data frame to a variable:
sepallen = df[0]
sepalwidth = df[1]
petallen = df[2]
petalwidth = df[3]
species = df[4]

# let's then make a list of our data frames so they are easy to manipulate.
variablelist = [
    ("Sepal Length", sepallen), 
    ("Sepal Width", sepalwidth), 
    ("Petal Length", petallen), 
    ("Petal Width", petalwidth)
]


# Project Aim 1: Output a summary of each variable to a single text file.

# To simplify this, I have created a function called datasummary, which employs the describe() function to summarise the data and saves it to a txt.

from irisfunctions import datasummary 
datasummary(variablelist)



# Project Aim 2: Save a Histogram of each variable to png files.

# To simplify this, I have created a function called irisdatahist. This function reads in a list of tuples and iterates over it to create a histogram for each variable.
from irisfunctions import irisdatahist
irisdatahist(variablelist)
    





# Project Aim 3: Output a scatter plot of each pair of variables
# To simplify this, I have created a function called irisscatter, which takes in all combinations of pairs generated from our variable list, and creates a scatter plot of each combination.

varcombinations = it.combinations(variablelist, 2) # this function generates all combinations of length 2 (i.e. pairs) from the list we provided.

from irisfunctions import irisscatter
irisscatter(varcombinations) # now we can use our irisscatter function, reading in the varcombinations to get our 6 possible scatter plots.



# Project Aim 4: Other useful analyses...

# A. Best Fit Line
# To simplify this, I have created a function called bestfit, which reads in 2 variables and plots them in a scatter plot with the best fit line plotted on top.
from irisfunctions import bestfit
print("To see the best fit line for a combination of variables, please select the corresponding number for each variable.") # first, we give the user instructions.

x = input("Please input your first variable: \n\n1.Sepal Length\n\n2.Sepal Width\n\n3.Petal Length\n\n4.Petal Width\n\n") # then we ask them to input each variable by typing the corresponding number.
y = input("\n\nPlease input your second variable: \n\n1.Sepal Length\n\n2.Sepal Width\n\n3.Petal Length\n\n4.Petal Width\n\n")

# Below, we use an if condition to ensure that for whichever number the user selects, the right data frames are used for the x and y values.
if x == str(1):
    xvar = petallen
elif x == str(2):
    xvar = petalwidth
elif x == str(3):
     xvar = sepallen
elif x == str(4):
    xvar = sepalwidth
else:
    raise ValueError("Invalid input for the first variable. Please enter a number between 1 and 4.") # Additionally, I want to let the user know if they enter an incorrect number.

if y == str(1):
    yvar = petallen
elif y == str(2):
     yvar = petalwidth
elif y == str(3):
    yvar = sepallen
elif y == str(4):
    yvar = sepalwidth
else:
    raise ValueError("Invalid input for the second variable. Please enter a number between 1 and 4.")

bestfit(xvar,yvar) # finally, we use these values as the parameters for our function in order to get a plot with the best fit line for whichever plot the user would like to see.


# B. Pearson Correlation Coefficient
r = xvar.corr(yvar) # .corr() is a pandas function which calculates correlation between two data frames, using the Pearson correlation coefficient by default (Kulcsar, 2022).
print(f"The Pearson correlation coefficient for this pair of variables is {r}")

# We then use an if statement to tell the user if their chosen variables display a positive or negative correlation:
if r >= 0.7:
    print("This indicates a strong positive correlation.")
elif 0.3 <= r < 0.7:
    print("This indicates a moderate positive correlation.")
elif 0 < r < 0.3:
    print("This indicates a weak positive correlation.")
elif r <= -0.7:
    print("This indicates a strong negative correlation.")
elif -0.7 < r <= -0.3:
    print("This indicates a moderate negative correlation.")
elif -0.3 < r < 0:
    print("This indicates a weak negative correlation.")
else:
    print("There is no correlation.")



# C. The hidden variable
# The easiest way to showcase categorical variables affecting the data is to use a .groupby() function (OpenAI, 2024)
df.columns = ['sepallen', 'sepalwidth', 'petallen', 'petalwidth', 'species'] # I quickly added the headings of our data frames to a simple list to make the code below more clear.
grouped = df.groupby('species') # this function splits the data into groups according to some criteria, in this case by the types in data frame "species"
for species, data in grouped: # this line iterates over the pairs of variables (species and data).
    plt.hist(data['petallen'], bins=10, alpha=0.5, label=species) # in this case, I want to look at Petal Length.
plt.legend()
plt.xlabel("Petal Length")
plt.ylabel("Frequency")
plt.title("Histogram of Petal Length by Species")
plt.show() # after putting in our labels, legend, and title, now we can take a look at the histogram to see how the extra variable affects our spread.