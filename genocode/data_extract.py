"""
This file contains functions for data
extraction, conversion, and cleaning
"""

import pandas as pd

def txt_to_csv(txt_file, csv_file):
    """
    converts a .txt data file to a .csv
    data file and cleans the formatting
    Parameters:
        txt_file (required): The .txt file to be converted
        csv_file (required): The .csv output data to be written
    Returns:
        pandas.core.frame.DataFrame: A pandas DataFrame.
    """
    data = pd.read_csv(txt_file, '\s+', skiprows=20, \
                       names=['rsid', 'chromosome', 'position', 'genotype'])
    data = data.replace('--', 'NaN')
    data.to_csv(csv_file, index=False)
    data_frame = pd.DataFrame(data)
    return data_frame
