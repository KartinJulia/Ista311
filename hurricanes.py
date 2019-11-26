from inference import InferenceSuite
import scipy as sp
from scipy import stats

class HurricaneModel(InferenceSuite):
    def likelihood(self, data, hypothesis):
         p = sp.stats.poisson.pmf(data, hypothesis)
         return p
        #sp.stats.poisson.rvs(rate)

    def predict(self):
        return sp.stats.poisson.rvs(self.sample())

data = sp.loadtxt('hurricanes.csv', delimiter = ',', skiprows = 1)
print(data[16:20])
#i1974 = HurricaneModel(data)
#i2015 = HurricaneModel(data)
