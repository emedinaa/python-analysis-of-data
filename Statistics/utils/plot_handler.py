from matplotlib import pyplot
import scipy.stats as n_stats

'''
@Author : Eduardo Medina
'''

class PlotHandler():

    def __init__(self):
        print("PlotHandler")

    def histogram(self, data):
        print("PlotHandler - histogram")
        pyplot.hist(data)
        pyplot.show()

    def quantile(self,data) :
        print("PlotHandler - quantile")
        n_stats.probplot(data, dist='norm',plot=pyplot)
        pyplot.show()
    
    def box(self, data, title:str=""):
        print("PlotHandler - box")
        pyplot.figure(figsize =(10, 7))
        #fig, ax = pyplot.subplots(figsize=(10, 7), layout='constrained')
        #ax.set_title(title)  # Add a title to the axes.
        pyplot.boxplot(data)
        pyplot.title(title)
        pyplot.show()
    
    def box_comparative(self, data,columns, pre_data, post_data, title:str):
        print("PlotHandler - box comparative")
        # Box plot of Post Test and Pre Test (different measures od IQ)
        pyplot.figure(figsize=(4, 3))
        data.boxplot(column=columns)

        # Boxplot of the difference
        pyplot.figure(figsize=(4, 3))
        pyplot.boxplot(post_data - pre_data)
        pyplot.xticks((1, ), (title, ))

        # show plot
        pyplot.show()