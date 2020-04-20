"""
    @author: thehalfspace

    References: https://www.wikiwand.com/en/Jackknife_resampling

"""

from numpy import  mean, zeros, delete

def jackknife_resample(X):
    """ Bootstrap resample an array_like data n times
        
        Input parameters:
        ----------------
            X:  array_like
                input data to resample
                
        Returns:
        --------
            X_resample: array_like, 
                returns resampled data where the ith row
                is the original sample with ith measurement
                deleted.

    """
    n = X.shape[0]
    if n <=0:
        raise ValueError("data must contain atleast one measurement.")

    resamples = zeros((n,n-1))

    for i in range(n):
        resamples[i] = delete(X,i)
    
    return resamples
