

###################

import os
os.environ["OPENBLAS_NUM_THREADS"] = "1"

def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    N = len(L)
    if N == 0:
        return NaN
    else:
        return np.std(L)