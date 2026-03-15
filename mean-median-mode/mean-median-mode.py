import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # 1. Calculate Mean
    mean = np.mean(x)
    
    # 2. Calculate Median
    median = np.median(x)
    
    # 3. Calculate Mode
    # Counter.most_common(1) returns a list like [(value, count)]
    mode = Counter(x).most_common(1)[0][0]
    
    return mean, median, mode