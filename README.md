# pands-project

# Investigation of the Iris Dataset
Author: Myles Henehan<br/>Student Number: G00439446<br/>Module: Programming and Scripting
***

## Project Summary
This project consists of an exploration of the Iris Data Set, using Python to examine its attributes and form a conclusion about the data contained within. There will be 3 main aims to this project; the first will be to identify the variables present in the data set and export each of them to a single text file. The second aim will be to produce representations of said variables in the form of histograms, and save them as png files. Finally, we will produce a scatter plot of each combination of numerical variables. We will conclude by looking at some other areas for exploration, including the best fit line, the Pearson Correlation Coefficient, and the inclusion of a third variable on one of our scatter plots.

## Background of the Dataset
First introduced in 1936 by British statistician Ronald Fisher in his paper titled "The use of multiple measurements in taxonomic problems," the Iris Data set is a staple in the field of data analytics and statistics, and serves as a simple, straightforward source of data through which beginners can build up their data analysis skills.

## Variables within the Dataset
The data set contains 150 instances of iris flower, with 50 of each of three species - setosa, versicolor, and virginica. For each individual flower, 4 different measurements or variables have been recorded: sepal length, sepal width, petal length and petal width. This combination of categorical and numerical attributes gives students in the field of data science a succinct, yet all-encompassing set of data through which to explore data representation methods using Python.

## Contents and function of the py file
The main component of this project is a Python file called analysis.py, which carries out a number of commands to help us explore the Iris data set. It is also accompanied by a file named functions.py, which stores the main functions created for this project and used in the analysis.py file.

### 1. Reads in the dataset and assigns each data frame to a variable name
Since the dataset itself does not have headers, I have used the information in the iris.names file for reference. I have also created a list of tuples, with each tuple containing the name of each data frame and the data frame itself (for numerical variables only).

### 2. Writes a description of each of the 4 main numerical variables and stores this in a single txt file.
To do this step, I have used a custom made function, datasummary, which iterates over our list of tuples and uses the describe function from the pandas library to get important statistical data such as the mean, the standard deviation and the min and max values. Our function then writes this data to a txt file (irisdatasummary.txt) in a readable format.

### 3. Outputs histograms to show the spread of each numerical variable and saves these as png files.
For step 3, I have created another function, irisdatahist, which iterates over our tuple list and creates a separate histogram for each of our numerical variables. Our function then saves each histogram as a png file. For this step, matplotlib is extremely important as it offers functions which help us to visualise our data.

### 4. Creates a set of scatter plots, showing the relationship between each possible combination of variables.
In this step, I first used a function from the module itertools, called combinations. This function generates all the possible pairs of variables (in this case, 6). I then used our custom function, irisscatter, to create a scatter plot for each pair.

### 5. Prompts the user to read in 2 variables, and gets the best fit line and Pearson Correlation Coefficient
Having completed the main aims of this project, I wanted to make my programme more interactive, so I wrote a code that prompts the user to select 2 variables they would be interested in seeing the best fit line for. Using my custom function, bestfit, the programme then tells the user the slope and intercept for their inputted variables, and creates a scatter plot with the best fit line over it. Then, using the corr function from pandas, the programme calculates the Pearson Correlation Coefficient for this pair of variables and tells the user what kind of correlation this indicates. This method measures the extent to which the points in a scatter plot cluster around a straight line, and is widely used in statistics and data analysis to assess the relationship between two continuous variables. This coefficient can range between 0 and 1, with 0 implying no correlation, 1 implying a very positive correlation, and -1 implying a very negative correlation (Turney, 2022).

### 6. Addresses the effect of the categorical variable "species" by creating a representation which includes this as an added variable.
Finally, I wanted to showcase the effect that a hidden categorical variable can have on the spread of data. For this, I have used Petal Length as an example, as the high standard deviation in this data indicates another variable at play. Sure enough, when we plot the petal length values grouped by species, we can see that setosas tend to have a much smaller petal length, while virginicas tend to have the longest petals.

## Conclusion
Through this project, we've attained an in-depth grasp of the attributes of the Iris dataset, employing Python to conduct diverse analyses and visualisations. The project successfully accomplished several goals, encompassing variable identification and description, histogram and scatter plot creation, and explorations of additional areas such as the best fit line, the Pearson correlation coefficient, and the impact of hidden variables. This exploration has yielded significant insights into data analysis methodologies and techniques, underscoring Python's efficacy as a tool for navigating and comprehending complex datasets.

## References
- Fisher,R. A.. (1988). Iris. UCI Machine Learning Repository. https://doi.org/10.24432/C56C76.
- OpenAI. (2024). ChatGPT. OpenAI. Available at: https://openai.com/chatgpt (Accessed: 19 May 2024).
- Turney, S. (2022). "Pearson Correlation Coefficient (r) | Guide & Examples". Available at: https://www.scribbr.com/statistics/pearson-correlation-coefficient/#:~:text=The%20Pearson%20correlation%20coefficient%20(r,the%20relationship%20between%20two%20variables [Accessed 14 May 2024]
- Waskom, M. (n.d.). "Visualizing statistical relationships". Available at: https://seaborn.pydata.org/tutorial/relational.html [Accessed 14 May 2024]