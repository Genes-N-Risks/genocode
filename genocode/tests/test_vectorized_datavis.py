"""
These are unit tests for the vectorized_datavis module
"""

import sys
import numpy as np

sys.path.append('..')

import vectorized_datavis

def test_compounddata():
    """
    Test that the data returned are numpy.ndarrays
    """
    mean = np.array([24.12, 24.43, 24.82])
    sdev = np.array([3.87, 3.94, 3.95])
    datagenerated = vectorized_datavis.compounddata(mean, sdev)
    assert isinstance(datagenerated, np.ndarray),\
    "Returned data are not numpy.ndarrays"

def test_databinning():
    """
    Test that the data returned are numpy.ndarrays
    """
    mean = np.array([24.12, 24.43, 24.82])
    sdev = np.array([3.87, 3.94, 3.95])
    datagenerated = vectorized_datavis.compounddata(mean, sdev)
    bins = np.linspace(10, 40, num=30)
    yhist = vectorized_datavis.databinning(datagenerated, bins_list=bins)
    assert isinstance(yhist, np.ndarray),\
    "Returned data are not numpy.ndarrays"

def test_pdfgen():
    """
    Test that the data returned are numpy.ndarrays
    """
    bins = np.linspace(10, 40, num=30)
    mean = np.array([24.12, 24.43, 24.82])
    sdev = np.array([3.87, 3.94, 3.95])
    pdf = vectorized_datavis.pdfgen(mean, sdev, bins_list=bins)
    assert isinstance(pdf, np.ndarray),\
    "Returned data are not numpy.ndarrays"

def test_percent_overlap():
    """
    Test that the data returned is a numpy.ndarray
    """
    mean = np.array([24.12, 24.43, 24.82])
    sdev = np.array([3.87, 3.94, 3.95])
    overlap_perc_1w = vectorized_datavis.percent_overlap\
    (mean, sdev)
    assert isinstance(overlap_perc_1w, np.ndarray),\
    "Returned data is not a numpy.ndarray"
