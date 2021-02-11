import matplotlib.pyplot as plt
import numpy as np

def plot_data(X, y):
    plt.figure()

    # ===================== Your Code Here =====================
    # Instructions : Plot the positive and negative examples on a
    #                2D plot, using the marker="+" for the positive
    #                examples and marker="o" for the negative examples
    #
    for i in range(y.shape[0]):
        if 1==y[i]:
            plt.scatter(X[i][0],X[i][1],c='y',marker='+')
        else:
            plt.scatter(X[i][0],X[i][1],c='b',marker='o')
    #plt.xlabel('Exam 1 score')
    #plt.ylabel('Exam 2 score')
    plt.pause(0.5)  

