"""Functions used in Exercise 8 of Geol 197 GDAM"""

# Import any modules needed in your functions here
import math as m
import numpy as np

# Define your new functions below
def gaussian(mean, stddev, x):
    
    """
    Function for calculating gaussian distribution

    Parameters
    ------------
    x: <list>
        list of values for which the normal distribution will be calculated
    mean: <numerical>
        average
    stddev: <numerical>
        standard deviation

    Returns
    -------------
    <list>
        list of calculated normal distribution for x
    """
    
    #create new list to store calculated values
    normal = []
    
    #iterate for all values in x
    for y in x:
        
        #gaussian function formula
        gauss = (np.exp(-(y-mean)**2/(2*stddev**2)))/(stddev*np.sqrt(2*np.pi))
        
        #add to list
        normal.append(gauss)
        
    #return list of calculated values
    return normal


def linregress(x,y):
    """
    Function for calculating linear regression

    Parameters
    -------
    x: array
        x values
    y: array
        y values

    Returns
    -------
    slope (B): float
    y-intercept (A): float
    """

    #for n in range(len(x)):
    delta = (len(x)*(x**2).sum()) - (x.sum()**2)
    A = (((x**2).sum()*y.sum())-(x.sum()*(x*y).sum()))/delta
    B = ((len(x)*(x*y).sum())-(x.sum()*y.sum()))/delta
    
    return A, B

def pearson(x,y):
    """
    Function for calculating correlation coefficient (r)

    Parameters
    ---------------
    x: array
        contains x values
    y: array
        contains y values

    Returns
    ---------------
    correlation coefficient (r): float

    """
    topsum = 0
    bottomsumx = 0
    bottomsumy = 0

    if isinstance(x, np.ndarray) and isinstance(y, np.ndarray):
        for i in range(len(x)):
            topsum +=  ((x[i] - x.mean())*(y[i] - y.mean()))
            bottomsumx += (x[i] - x.mean())**2
            bottomsumy += (y[i] - y.mean())**2
        r = topsum / (np.sqrt(bottomsumx * bottomsumy))
        return r
        
    else:
        for i in range(len(x)):
            topsum +=  ((x.iloc[i] - x.mean())*(y.iloc[i] - y.mean()))
            bottomsumx += (x.iloc[i] - x.mean())**2
            bottomsumy += (y.iloc[i] - y.mean())**2
        
        r = topsum / (np.sqrt(bottomsumx * bottomsumy))
        return r

def chi_squared(obs, exp, std):
    """
    Function that computes goodness-of-fit of a line

    Parameters
    ----------
    obs: array
    
    exp: array
    
    std: array

    Returns
    ----------
    cs: float
    
    """
    summation = 0

    for i in range (len(obs)):
        summation += ((obs[i]-exp[i])**2)/(std[i]**2)

    cs = summation/len(obs)

    return cs


