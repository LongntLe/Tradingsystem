import numpy as np
from scipy.stats import norm
from stock import Stock

#source: https://github.com/jeromeku/Python-Financial-Tools/blob/master/capm.py

class CAPM(object):
    def __init__(self,risk_free,market,alpha = .05):

        self.risk_free = Stock(risk_free["ticker"],risk_free["date_range"]) if type(risk_free) is dict else Stock(risk_free)
        self.market = Stock(market["ticker"],market["date_range"]) if type(market) is dict else Stock(market)

        self.alpha, self.beta = {}, {}
        self.critical_value = norm.ppf(1 - alpha / 2.0)




