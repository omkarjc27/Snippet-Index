"""
    @author: thehalfspace

    References:https://www.wikiwand.com/en/Bootstrapping_(statistics)

"""

from numpy import floor 
from numpy.random import rand

def bootstrap_resample(X, size=None):
    """ Bootstrap resample an array_like data n times
        
        Input parameters:
        ----------------
            X:  array_like
                input data to resample
            
            size: int, optional
                length of resampled array, equal to
                len(X) if size==None
                
        Returns:
        --------
            X_resample: resampled data X

    """
    n = X.shape[0]
    if n <=0:
        raise ValueError("data must contain atleast one measurement.")

    if size == None:
        size = len(X)
        
    resample_idx = floor(rand(size)*len(X)).astype(int)
    return X[resample_idx]
