from inference import InferenceSuite
import scipy as sp
from scipy import stats
import matplotlib.pyplot as plt

class HurricaneModel(InferenceSuite):
    def likelihood(self, data, hypothesis):
         p = sp.stats.poisson.pmf(data, hypothesis)
         return p
        #sp.stats.poisson.rvs(rate)

    def predict(self):
        return sp.stats.poisson.rvs(self.sample())

data = sp.loadtxt('hurricanes.csv', delimiter = ',', skiprows = 1)
d1974 = data[114:124]
d2015 = data[155:165]
uni_total = {}
for i in range (21):
    uni_total[i] = 1/20
#print(d1974)
#print(d2015)
#print(uni_total)
i1974 = HurricaneModel(uni_total)
i2015 = HurricaneModel(uni_total)

major_1974 = HurricaneModel(uni_total)
major_2015 = HurricaneModel(uni_total)

for i in (d1974):
    i1974.update(i[2])
    major_1974.update(i[3])
for j in (d2015):
    i2015.update(j[2])
    major_2015.update(j[3])

total_pred_1974,total_pred_2015,major_pred_1974,major_pred_2015 = [],[],[],[]
for k in range(1000):
    total_pred_1974.append(i1974.predict())
    total_pred_2015.append(i2015.predict())
    major_pred_1974.append(major_1974.predict())
    major_pred_2015.append(major_2015.predict())

plt.hist(total_pred_1974, bins = sp.arange(20) - 0.5, color = 'blue', alpha = 0.6, edgecolor = 'black', linewidth = 1.2)
plt.hist(total_pred_2015, bins = sp.arange(20) - 0.5, color = 'yellow', alpha = 0.6, edgecolor = 'black', linewidth = 1.2)
plt.hist(major_pred_1974, bins = sp.arange(20) - 0.5, color = 'red', alpha = 0.6, edgecolor = 'black', linewidth = 1.2)
plt.hist(major_pred_2015, bins = sp.arange(20) - 0.5, color = 'green', alpha = 0.6, edgecolor = 'black', linewidth = 1.2)
plt.xticks(sp.arange(20))
plt.title("Predicted hurricanes, total and major")
plt.legend(['Total hurricanes 1965-1974','Total hurricanes 2006-2015', 'Major hurricanes 1965-1974','Major hurricanes 2006-2015'])
plt.savefig("hist.png")
plt.close('all')
