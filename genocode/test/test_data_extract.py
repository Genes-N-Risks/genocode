"""
These are the unit tests for the data_extract.py module
"""

import sys

sys.path.append('..')

import pandas as pd
import data_extract

def test_txt_to_csv():
    """
    Test that the output dataframe is a pandas DataFrame
    Test that the data types are strings
    """
    data_frame = data_extract.txt_to_csv\
    ('../../genocode/data/23andMe_data.txt', '../../genocode/data/23andMe_data.csv')
    assert isinstance(data_frame, pd.core.frame.DataFrame),\
    "Returned dataset is not a pandas dataframe"
    assert isinstance(data_frame['rsid'][1], str),\
    "data in the dataset are not strings"
