import numpy as np

from utils.normality_test_handler import NormalityTestHandler
from utils.statistics_handler import StatisticsHandler
from utils.plot_handler import PlotHandler

# sample data
data = np.array([100,0,50,10,18,50,80,35,120,30,20,40, 25, 32, 20, 15, 10, 34, 28,
                 11, 9, 25, 19, 92, 81, 43 , 27, 93])

normality = NormalityTestHandler()
normality.execute(data)

sh = StatisticsHandler()
sh.getMeasures(data)

# histogram plot
#pyplot.hist(data, edgecolor= 'black', linewidth=1)
#pyplot.show()

#quantile quantile
#n_stats.probplot(data, dist='norm',plot=pyplot)
#pyplot.show()

#Plots
ph = PlotHandler()
# box
ph.box(data, "Pre Test - Metric")
# histogram
#ph.histogram(data)
# quantile
#ph.quantile(data)

# mean xxxx
# median xxxx
# std xxxx
# min xxxx
# max xxxx

# coverage normal test : xxxx

# shapiro xxxxx //Gaussian or not Gaussian

# kresult statistic=xxxx, pvalue=xxxx, statistic_location=xxx, statistic_sign=xxx
# Gaussian or not Gaussian
