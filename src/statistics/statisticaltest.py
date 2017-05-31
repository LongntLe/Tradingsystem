import matplotlib.pyplot as py
from numpy import *


def hurst(p):
    tau = []
    lagvec = []
    #  Step through the different lags  
    for lag in range(2, 20):
        #  produce price difference with lag  
        pp = subtract(p[lag:], p[:-lag])
        #  Write the different lags into a vector  
        lagvec.append(lag)
        #  Calculate the variance of the differnce vector  
        tau.append(sqrt(std(pp)))
    # linear fit to double-log graph (gives power)
    m = polyfit(log10(lagvec), log10(tau), 1)
    # calculate hurst  
    hurst = m[0] * 2
    # plot lag vs variance  
    # py.plot(lagvec,tau,'o'); show()
    return hurst

def MDD(data, amount): # calculating maximum drawdown
        MDD = 0
        peak = amount
        trough = amount

        for i in range(len(data)):
            if (peak < data[i]):
                peak = data[i]
                trough = data[i]
            elif (trough > data[i]):
                trough = data[i]

            MDD = min(MDD, (trough-peak)/peak)
        return MDD

def MMI(data, period): # market meanness index
    nh, nl = 0
    sample = pd.DataFrame(data)
    sample = sample.ix[-period]
    m = np.median(sample)
    for i in range(period):
        if (data[i] > m) and (data[i] > data[i-1]):
            nl += 1
        elif (data[i] < m) and (data[i] < data[i-1]):
            nh += 1
    return 100*(nl+nh)/(period-1)
    
def ALMA(data,period):
    s = 0
    sigma = np.stdev(data) # needs to identify which dataframe to calculate STDEV
    for i in range(period):
        s += data[i]*np.exp(-(i-offset)**2/sigma**2) # needs to define what is i, offset and sigma
    

if __name__ == "__main__":
    #  Different types of time series for testing  
    p = log10(cumsum(random.randn(50000) + 1) + 1000)  # trending, hurst ~ 1
    # p = log10((random.randn(50000))+1000)   # mean reverting, hurst ~ 0
    # p = log10(cumsum(random.randn(50000))+1000) # random walk, hurst ~ 0.5
    print(hurst(p))
