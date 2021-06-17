import pandas as pd
import numpy as np


def jaccard_coef(s1: set, s2: set):
    coef = len(s1.intersection(s2))
    
    if coef != 0:
        coef /= len(s1.union(s2))
        
    return coef


def get_bootstrap_confidence_interval(
        values: np.ndarray,
        alpha: float = 0.05,
        n_samples: int = 2000,
) -> tuple:
    n = len(values)
    bootstrap_means = []
    
    for _ in range(n_samples):
        samples = np.random.choice(values, size=n, replace=True)
        bootstrap_means.append(samples.mean())
        
    t1, t2 = np.quantile(bootstrap_means, [alpha / 2, 1 - alpha / 2])
    
    return t1, t2
