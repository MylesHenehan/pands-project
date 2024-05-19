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
Since the dataset itself does not have headers, we are using the information in the iris.names file for reference.

### 2. Writes a description of each of the 4 main numerical variables and stores this in a single txt file.

### 3. Outputs histograms to show the spread of each numerical variable and saves these as png files.

### 4. Creates a set of scatter plots, showing the relationship between each possible combination of variables.

### 5. Prompts the user to read in 2 variables, and gets the best fit line between them to offer a visualisation of the trend.
 - When looking at scatter plots, it can often be useful to work out the best fit line to visualise the overall trend in the data. For example, when you look at Petal Length versus Petal Width above, you can see quite a linear progression of the data. Let's use a best fit line to demonstrate this. In order to plot this, we will first need to determine the slope of the line and the point at which it intercepts the y axis, and then use the y = mx + c method.

### 6. Gets the Pearson correlation coefficient of said 2 variables
This method measures the extent to which the points in a scatter plot cluster around a straight line, and is widely used in statistics and data analysis to assess the relationship between two continuous variables. This coefficient can range between 0 and 1, with 0 implying no correlation, 1 implying a very positive correlation, and -1 implying a very negative correlation (Turney, 2022).

### 7. Addresses the effect of the categorical variable species by creating a representation which includes this as a third variable.
Sometimes when plotting data, the data can appear in clusters. In this case, it is common that a categorical variable is affecting the data. Let's look at Petal Length histogram as an example. [Placeholder]

## Conclusion

## References
- Fisher,R. A.. (1988). Iris. UCI Machine Learning Repository. https://doi.org/10.24432/C56C76.
- OpenAI. (2024). ChatGPT. OpenAI. Available at: https://openai.com/chatgpt (Accessed: 19 May 2024).
- Turney, S. (2022). "Pearson Correlation Coefficient (r) | Guide & Examples". Available at: https://www.scribbr.com/statistics/pearson-correlation-coefficient/#:~:text=The%20Pearson%20correlation%20coefficient%20(r,the%20relationship%20between%20two%20variables [Accessed 14 May 2024]
- Waskom, M. (n.d.). "Visualizing statistical relationships". Available at: https://seaborn.pydata.org/tutorial/relational.html [Accessed 14 May 2024]