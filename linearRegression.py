# linearRegression.py
# Written by: Sidumiso Debbie Mabaso
# Date: 30 July 2020
# Function: This program performs linear regression to find the best fit line through the data.

import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_diabetes

# defining a function 
def estimate_coef(x, y): 
    # number of points 
    n = np.size(x) 
  
    # mean of x and y vector 
    m_x, m_y = np.mean(x), np.mean(y) 
  
    # calculating cross-deviation and deviation around x 
    SS_xy = np.sum(y*x) - n*m_y*m_x 
    SS_xx = np.sum(x*x) - n*m_x*m_x 
  
    # calculating regression coefficients 
    b_1 = SS_xy / SS_xx 
    b_0 = m_y - b_1*m_x 
  
    return(b_0, b_1) 
  
def plot_regression_line(x, y, b): 
    # plotting the given points as a scatter plot 
    plt.scatter(x, y, color = "red", marker = "o", s = 30) # training data
    plt.scatter(x, y, color = "green", marker = "x", s = 70) # testing data
  
    # predicted response 
    y_pred = b[0] + b[1]*x 
  
    # plotting the regression line 
    plt.plot(x, y_pred, color = "blue") 
  
    # putting labels on the axis
    plt.xlabel('x') 
    plt.ylabel('y') 
  
    # function to show plot 
    plt.show() 


# load the data
d = load_diabetes()
d_X = d.data[:, np.newaxis, 2 ]
x = d_X[:- 20 ]
y = d.target[:- 20 ]
dx_test = d_X[- 20 :]
dy_test = d.target[- 20 :]

# estimating coefficients 
b = estimate_coef(x, y) 

# plotting regression line 
plot_regression_line(x, y, b)
