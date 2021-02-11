import numpy as np
from sigmoid import *


def cost_function(theta, X, y):
    m = y.size

    # You need to return the following values correctly
    cost = 0
    grad = np.zeros(theta.shape)

    # ===================== Your Code Here =====================
    # Instructions : Compute the cost of a particular choice of theta
    #                You should set cost and grad correctly.
    #


    # ===========================================================
    z= np.dot(X,theta)
    cost = np.sum(-y*np.log(sigmoid(z))-(1-y)*np.log(1-sigmoid(z)))/m
    dt = sigmoid(z)-y
    grad = np.sum(X*np.array([dt,dt,dt]).T,axis=0)/m

    return cost, grad
