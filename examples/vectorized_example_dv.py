"""
This file is a tutorial on the usage of the functions and modules
present in dvectorized_datavis.py.
"""
import sys
import numpy as np
sys.path.append('..')
from genocode import vectorized_datavis



SERROR = 1.5
LOWERCI = 0.27
UPPERCI = 0.39
CIVAL = 95
SIZE = 1000
BINS = np.linspace(10, 40, num=30)

#Standard deviation from standard error.
SDEV = vectorized_datavis.se_to_sd(serror=SERROR, size=SIZE)
print('For the standard error of '+str(SERROR)+' and size of '+str(SIZE)+', \
    the standard deviation is'+str(SDEV))


#Standard deviation from confidence interval.
SDEV = vectorized_datavis.ci_to_sd(lowerci=LOWERCI, upperci=UPPERCI, cival=CIVAL, \
                        size=SIZE)
print('For the confidence interval of '+str(LOWERCI)+'-'+str(UPPERCI)+' and \
    size of '+str(SIZE)+', the standard deviation is '+str(SDEV))

MEAN = np.array([24.12, 24.43, 24.82])
SDEV = np.array([3.87, 3.94, 3.95])

#The data generated from means and standard deviations for three datasets.
DATAGENERATED = vectorized_datavis.compounddata(mean=MEAN, sdev=SDEV, size=SIZE)

#Binning of data
YBIN = vectorized_datavis.databinning(datagenerated=DATAGENERATED, bins_list=BINS)
print('The bins have been created.')

#Histogram for the three datasets
vectorized_datavis.histplotting(datagenerated=DATAGENERATED, bins_list=BINS)

#Probability distribution functionf for the three datasets.
vectorized_datavis.pdfplotting(mean=MEAN, sdev=SDEV, bins_list=BINS)

#Violin plots for the three dataset.
vectorized_datavis.violinplotting(datagenerated=DATAGENERATED)

#Percentage overlap
OVERLAP = vectorized_datavis.percent_overlap(mean=MEAN, sdev=SDEV)
print('The percentage overlap for the data1 and data1 is '+str(OVERLAP[1]))
print('The percentage overlap for the data1 and data2 is '+str(OVERLAP[2]))
print('The percentage overlap for the data1 and data3 is '+str(OVERLAP[3]))
