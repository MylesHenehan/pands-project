import matplotlib.pyplot as plt
import numpy as np

def vardescruibe var):
    print (var.describe())


def irisdatahist(data, xlabel, title, filename):
    plt.hist(data, bins=10, color='yellow', edgecolor='black')
    plt.xlabel(xlabel)
    plt.ylabel('No. of Iris Flowers')
    plt.title(title)
    plt.savefig(filename)
    plt.show()

