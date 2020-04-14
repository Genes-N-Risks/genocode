"""
This file is a tutorial on the usage of the functions and modules
present in datavis.py.
"""

import numpy as np
import datavis

MEAN1 = 24.12
SDEV1 = 3.87
MEAN2 = 24.43
SDEV2 = 3.94
MEAN3 = 24.82
SDEV3 = 3.95
SERROR = 1.5
LOWERCI = 0.27
UPPERCI = 0.39
CIVAL = 95
SIZE = 1000
BINS = np.linspace(10, 40, num=30)

#Standard deviation from standard error.
SDEV = datavis.se_to_sd(serror=SERROR, size=SIZE)
print('For the standard error of '+str(SERROR)+' and size of '+str(SIZE)+', \
    the standard deviation is'+str(SDEV))


#Standard deviation from confidence interval.
SDEV = datavis.ci_to_sd(lowerci=LOWERCI, upperci=UPPERCI, cival=CIVAL, \
                        size=SIZE)
print('For the confidence interval of '+str(LOWERCI)+'-'+str(UPPERCI)+' and \
    size of '+str(SIZE)+', the standard deviation is '+str(SDEV))


#The data generated from means and standard deviations for three datasets.
DATAGENERATED1, DATAGENERATED2, DATAGENERATED3 = datavis.compounddata(\
                                                    mean1=MEAN1, sdev1=SDEV1, \
                                                    mean2=MEAN2, sdev2=SDEV2, \
                                                    mean3=MEAN3, sdev3=SDEV3, \
                                                    size=SIZE)

#Binning of data
YBIN1, YBIN2, YBIN3 = datavis.databinning(datagenerated1=DATAGENERATED1, \
                                datagenerated2=DATAGENERATED2, \
                                datagenerated3=DATAGENERATED3, bins_list=BINS)
print('The bins have been created.')

#Histogram for the three datasets
datavis.histplotting(datagenerated1=DATAGENERATED1, \
                    datagenerated2=DATAGENERATED2, \
                    datagenerated3=DATAGENERATED3, bins_list=BINS)

#Probability distribution functionf for the three datasets.
datavis.pdfplotting(mean1=MEAN1, sdev1=SDEV1, mean2=MEAN2, sdev2=SDEV2, \
                    mean3=MEAN3, sdev3=SDEV3, bins_list=BINS)

#Violin plots for the three dataset.
datavis.violinplotting(datagenerated1=DATAGENERATED1, \
                        datagenerated2=DATAGENERATED2, \
                        datagenerated3=DATAGENERATED3)

#Percentage overlap
OVERLAP_11_PERC, OVERLAP_12_PERC, OVERLAP_13_PERC = datavis.percent_overlap(\
                                                        mean1=MEAN1, \
                                                        sdev1=SDEV1, \
                                                        mean2=MEAN2, \
                                                        sdev2=SDEV2, \
                                                        mean3=MEAN3, \
                                                        sdev3=SDEV3)
print('The percentage overlap for the data1 and data1 is '+str(OVERLAP_11_PERC))
print('The percentage overlap for the data1 and data2 is '+str(OVERLAP_12_PERC))
print('The percentage overlap for the data1 and data3 is '+str(OVERLAP_11_PERC))
