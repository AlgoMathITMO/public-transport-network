import pandas as pd
import numpy as np


def truncated_corr(df: pd.DataFrame, th: float = 0.5, method: str = 'pearson') -> pd.DataFrame:
    corr = df.corr(method=method)
    values = corr.values.copy()
    values[np.abs(values) < th] = np.nan
    corr = pd.DataFrame(values, index=corr.index, columns=corr.columns)
    
    return corr
