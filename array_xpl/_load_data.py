"""
    This module loads data from various file formats and converts it to numpy array,
    with specified data type and order.

Expected supported formats:
    - npy
    - npz
    - csv
    - json
    - txt

    
"""

import numpy as np
import pathlib

def load_csv_data(file_path: str, delimiter: str = ",", dtype=np.float64, skip_header=0):
    data = np.genfromtxt(
        file_path, 
        delimiter=delimiter, 
        dtype=dtype, 
        skip_header=skip_header
    )
    return data

