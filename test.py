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


#

# third variable
grouped = df.groupby(4) # The easiest way is to use a .groupby() function (OpenAI, 2024)

for species, data in grouped:
    plt.hist(data[2], bins=10, alpha=0.5, label=species)

plt.legend()
plt.xlabel('Petal Length')
plt.ylabel('Frequency')
plt.title('Histogram of Petal Length by Species')
plt.show()