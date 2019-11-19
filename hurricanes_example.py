'''
Example prediction and plotting code for the hurricane analysis.
Creates two prediction histograms. The first is for the total number of hurricanes 
'''

import scipy as sp
import matplotlib.pyplot as plt
from hurricanes import HurricaneModel

def main():

    data = sp.loadtxt('hurricanes.csv', delimiter = ',', skiprows = 1)
    print("Data loaded.")

    # Initialize and fit the model
    all_years_total = HurricaneModel(sp.linspace(0, 20, 201)) # lambda between 0 and 20
    print("Model for total hurricanes initialized. Fitting model...")
    for i in range(data.shape[0]):
        all_years_total.update(data[i,2])
    all_years_major = HurricaneModel(sp.linspace(0, 20, 201))
    print("Model for major hurricanes initialized. Fitting model...")
    for i in range(data.shape[0]):
        all_years_major.update(data[i, 3])

    # Generate predictions

    print("Generating predictions: total hurricanes...")
    total_pred = []
    for i in range(1000):
        total_pred.append(all_years_total.predict())

    print("Generating predictions: major hurricanes...")
    major_pred = []
    for i in range(1000):
        major_pred.append(all_years_major.predict())

    # Plot the predictions

    print("Plotting histogram...")
    plt.hist(total_pred, bins = sp.arange(20) - 0.5, color = 'blue', alpha = 0.6, edgecolor = 'black', linewidth = 1.2)
    plt.hist(major_pred, bins = sp.arange(20) - 0.5, color = 'red', alpha = 0.6, edgecolor = 'black', linewidth = 1.2)
    plt.xticks(sp.arange(20))
    plt.title("Predicted hurricanes, total and major")
    plt.legend(['Total hurricanes', 'Major hurricanes'])
    plt.savefig("example_hist.png")
    plt.close('all')

if __name__ == '__main__':
    main()