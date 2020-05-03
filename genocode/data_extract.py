"""
This file contains functions for data
extraction, conversion, and cleaning
"""

import pandas as pd

def txt_to_csv(txt_filepath, csv_filepath):
    """
    converts a .txt data file to a .csv
    data file and cleans the formatting
    Parameters:
        txt_filepath (required): The .txt file to be converted
        csv_filepath (required): The .csv output data to be written
    Returns:
        pandas.core.frame.DataFrame: A pandas DataFrame.
    """
    fopen = open(txt_filepath, mode='r+')
    fread = fopen.readlines()
    x_line = '# rsid'
    n_rows = 0
    for line in fread:
        n_rows += 1
        if x_line in line:
            break
    data = pd.read_csv(txt_filepath, '\s+', skiprows=n_rows, \
                       names=['rsid', 'chromosome', 'position', 'genotype'])
    data = data.replace('--', 'NaN')
    data.to_csv(csv_filepath, index=False)
    data_clean = pd.read_csv(csv_filepath, \
                             dtype={'rsid': str, 'chromosome': str, \
                                    'position': str, 'genotype': str})
    data_frame = pd.DataFrame(data_clean)
    return data_frame
