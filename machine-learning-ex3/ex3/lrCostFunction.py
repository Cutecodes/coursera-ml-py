import numpy as np
from sigmoid import *


def lr_cost_function(theta, X, y, lmd):
    m = y.size

    # You need to return the following values correctly
    cost = 0
    grad = np.zeros(theta.shape)

    # ===================== Your Code Here =====================
    # Instructions : Compute the cost of a particular choice of theta
    #                You should set cost and grad correctly.
    #


    # =========================================================
    
    z= np.dot(X,theta)
    theta2=theta**2
    theta2[0]=0
    cost = np.sum(-y*np.log(sigmoid(z))-(1-y)*np.log(1-sigmoid(z)))/m+np.sum(theta2)*lmd/2/m
    dt = sigmoid(z)-y
    grad = np.sum(X*np.array([dt for i in range(X.shape[1])]).T,axis=0)/m+lmd*theta/m
    grad[0]-=lmd*theta[0]/m

    return cost, grad
