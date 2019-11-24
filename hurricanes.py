from inference import InferenceSuite
import scipy as sp
from scipy import stats

class HurricaneModel(InferenceSuite):
    def likelihood(self, data, hypothesis):
         p = sp.stats.poisson.pmf(data, hypothesis)
        #sp.stats.poisson.rvs(rate)

    def predict(self):
        return sp.stats.poisson.rvs(self.d)
