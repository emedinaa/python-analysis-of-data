
from scipy import stats
from scipy.stats import shapiro
from scipy.stats import kstest

'''
@Author : Eduardo Medina
'''
class NormalityTestHandler():
    ALPHA = 0.05

    def __init__(self):
        print("NormalityTestHandler")

    def execute(self, data):
        print("execute")

        # Normal Test
        res = stats.normaltest(data)
        result = res.statistic
        print("normaltest result", result)
        print()
        # Shapiro - Interpret the result
        stat, p = shapiro(data)
        print("shapiro p",p)
        print("shapiro stat",stat)

        if p > self.ALPHA:
            print("shapiro - Sample looks Gaussian (fail to reject H0)")
        else:
            print("shapiro - Sample does not look Gaussian (reject H0)")
        print()
        #perform Kolmogorov-Smirnov test
        kresult = kstest(data, 'norm')
        print("Kolmogorov-Smirnov result",kresult)

        if kresult.pvalue > self.ALPHA:
            print("Kolmogorov-Smirnov - Sample looks Gaussian (fail to reject H0)")
        else:
            print("Kolmogorov-Smirnov - Sample does not look Gaussian (reject H0)")

        print("-------------------------------")
        
