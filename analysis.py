# [Placeholder]
# 1. Outputs a summary of each variable to a single text file,
# 2. Saves a histogram of each variable to png files, and
# 3. Outputs a scatter plot of each pair of variables.
# 4. Performs any other analysis you think is appropriate.
# Author: Myles Henehan

# Let's start by importing the relevant libraries 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Now we need to read in our dataset
file = 'iris/iris.data' # we will assign the path of our dataset to the variable "file"
df = pd.read_csv(file, header=None) # we then use the .read_csv function from pandas to read in our data. Since there is no header, we want the data from the first row, hence "Header=None".
print(df) # as a test, let's print it. This will result in the first and last five rows being printed.

sepallen = df[0]
sepalwidth = df[1]
petallen = df[2]
petalwidth = df[3]
species = df[4]

# I also want to convert them to NumPy arrays, as this will make the data easier to deal with later on.
#sepallen = sepallen.to_numpy()
#sepalwidth = sepalwidth.to_numpy()
#petallen = petallen.to_numpy()
#petalwidth = petalwidth.to_numpy()
#species = species.to_numpy()


# Creating our histograms

# Sepal Length
plt.hist(sepallen, bins=10, color='yellow', edgecolor='black') # this function plots a histogram, specifying the data series, the number of bins to sort the data into, and the colour of the edges of the bars.
plt.xlabel('Sepal length (cm)') # Again, we add our data labels.
plt.ylabel('No. of Iris Flowers')
plt.title('Sepal Length of Iris Flowers')
plt.savefig('sepallen_histogram.png')

# Sepal Width
plt.hist(sepalwidth, bins=10, color='yellow', edgecolor='black')
plt.xlabel('Sepal width (cm)') 
plt.ylabel('No. of Iris Flowers')
plt.title('Sepal Width of Iris Flowers')
plt.savefig('sepalwidth_histogram.png')

# Petal Length
plt.hist(petallen, bins=10, color='yellow', edgecolor='black')
plt.xlabel('Petal length (cm)') 
plt.ylabel('No. of Iris Flowers')
plt.title('Petal Length of Iris Flowers')
plt.savefig('petallen_histogram.png')

# Petal Width
plt.hist(petalwidth, bins=10, color='yellow', edgecolor='black')
plt.xlabel('Petal width (cm)') 
plt.ylabel('No. of Iris Flowers')
plt.title('Petal Width of Iris Flowers')
plt.savefig('petalwidth_histogram.png')


# Simplying this code by creating a function
def irishist(data, xlabel, title, filename)
    


