import matplotlib.pyplot as plt
import numpy as np


# Function 1
# This function allows us to read in a list of tuples, and get a description of each data frame in the list. 
# It then writes these desriptions to a new txt file called irisdatasummary.txt, which will be saved in our repository.
def datasummary(listoftuples): # we first define the function and the expected parameter that we will read in.
    with open('irisdatasummary.txt', 'w') as ids: # we then create a file called irisdatasummary which we will write to, and shorten it to ids for further use.
        for name, df in listoftuples: # this line iterates over the list of tuples, taking the first value of each tuple as the name of the data frame, and the second as the data frame itself.
            description = df.describe() # we get a description of the data within each data frame using the describe() function available in the pandas library (W3Schools, 2022).
            ids.write(f"Here is a description of the variable {name}:\n") # We clarify what the data is, using the "name" value extracted above.
            ids.write(description.to_string()) # we use another pandas function, "to_string()", to convert the data frame to string representation (GeeksforGeeks, 2019).
            ids.write("\n\n") # we add some line breaks between the description of each variable for easy reading

# Function 2
# This function allows us to read in a list of tuples and create a histogram for each data frame in the list.
# It then saves each histogram as a separate png file.
def irisdatahist(listoftuples): # we first define the function and the expected parameter that will be read in.
    for name, df in listoftuples: # as in function 1, this line iterates over the list of tuples, taking the first value of each tuple as the name of the data frame, and the second as the data frame itself.
        plt.hist(df, bins=10, color='yellow', ec='black') # we then use the hist() function to plot each data frame, using the data frame, the number of bins, the colour of the graph, and the colour of the edges as parameters (Bobbitt, 2022).
        plt.xlabel(f"{name} (cm)") # we label the x axis, using the .xlabel function and the name of the data frame as the parameter.
        plt.ylabel('Frequency') # we label the y axis as "Frequency".
        plt.title(f"{name} of Iris Flowers") # we give the histogram a title according to the x variable which is being iterated over.
        plt.savefig(f"{name}.png") # we save each figure as a separate file, using the name of the data frame as the file name.
        plt.show() # for our own reference, let's show each of them.

# Function 3
# This function allows us to read in all combinations of variable pairs and create a scatter plot for each combination.
def irisscatter(variablecombinations): # we first define the function and the expected parameter that will be read in
    for (name1, df1), (name2, df2) in variablecombinations: # this line iterates over each pair of variables (combinations) provided in the variablecombinations variable that was read in. Each iteration extracts two tuples: (name1, df1) and (name2, df2).
        plt.scatter(df1, df2) # this line creates a scatter plot using the two data frames extracted above
        plt.xlabel(name1) # we then use the first name for the x label...
        plt.ylabel(name2) # ... and the second name for the y label
        plt.title(f"{name1} vs {name2}") # We create a title, using the two variables used in each iteration.
        plt.show() # for our own reference, let's show each of them.

# Function 4
# This function allows us to read in 2 data sets, plot them, and draw the best fit line through the data.
def bestfit(x,y): # we first define the function and the expected parameters that will be read in.
    m, c = np.polyfit(x, y, 1) # the .polyfit function (from numpy) takes a set of data points (x, y) and fits a polynomial of specified degree to the data. The degree 1 here represents a straight line (Ridolfi, 2020).
    # Here, "m" represents the slope, while "c" represents the intercept of the line. Let's make this clear for ease of reference by assigning them to more easy-to-understand variables.
    slope = m
    intercept = c
    print(f'Slope: {slope}') # we print out the slope for reference
    print(f'Intercept: {intercept}') # we print out the intercept for reference

    plt.plot(x, y, 'o') # We plot the data points. When you call plt.plot with just x and y data points and a marker style (like "o" in this case), it creates a scatter plot by plotting the points without connecting them through lines. (Gruppetta, n.d.)
    plt.plot(x, slope * x + intercept, 'r-', label="Best Fit Line") # This time we're adding another plot command in the same axis to insert our best fit line, with "r-" representing a solid red line.
    plt.xlabel("X Values") # Since the x label is dependent on what the user will enter, it's easier to use a generic label.
    plt.ylabel("Y Values") # Likewise, the y label is generic.
    plt.title("Best Fit Line for Chosen Variables") # We then create a generic title.
    plt.show() # For our own reference, let's take a look.

