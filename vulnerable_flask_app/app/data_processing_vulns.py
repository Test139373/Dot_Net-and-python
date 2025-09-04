import pandas as pd
import numpy as np

def pandas_read_pickle(filepath):
    # VULNERABLE: CVE-2020-14391 - Code execution in pandas
    return pd.read_pickle(filepath)

def pandas_read_hdf(filepath):
    # VULNERABLE: CVE-2020-14391
    return pd.read_hdf(filepath)

def numpy_fromfile(filename):
    # VULNERABLE: CVE-2021-34141 - Buffer overflow in numpy
    return np.fromfile(filename)