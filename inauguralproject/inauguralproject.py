import numpy as np 
from math import log 
# question 1 
def function(c ,l, nu, e):
    return log(c)- nu *(l**(1+1/e))/(1+1/e)

def solve(function):   
    ## constaints and bounds 
    c = m + wl - (tau0 * w * l + tau1 * max(w*l - kappa, 0))
    ## parameters 
    m = 1
    nu = 10
    e = 0.3
    tau0 = 0.4
    tau1 = 0.1
    kappa = 0.4
    return c




def square(x): 
    """ square numpy array
    
    Args:
    
        x (ndarray): input array
        
    Returns:
    
        y (ndarray): output array
    
    """
    
    y = x**2
    return y