'''
Test script for the inference assignment.
'''

import math
import numpy as np
import scipy as sp
import inference as inf
from locomotivedicts import *


make_plots = True

if make_plots:
    import matplotlib.pyplot as plt



benford_dict = {1: 0.301,
           2: 0.176,
           3: 0.125,
           4: 0.097,
           5: 0.079,
           6: 0.067,
           7: 0.058,
           8: 0.051,
           9: 0.046}

coin_dist = inf.InferenceSuite({0.05: 1.776936254020483e-07,
 0.1: 1.020680059927112e-05,
 0.15000000000000002: 0.00010370268890118822,
 0.2: 0.0005161364846248703,
 0.25: 0.0017304824149697391,
 0.3: 0.004501199064278561,
 0.35000000000000003: 0.00978677470803995,
 0.4: 0.01858091344649533,
 0.45: 0.031652285416210756,
 0.5: 0.0492226109146948,
 0.55: 0.07063269482986463,
 0.6000000000000001: 0.09406587432288259,
 0.6500000000000001: 0.11641818926960812,
 0.7000000000000001: 0.1334244315226275,
 0.7500000000000001: 0.14016907561254888,
 0.8: 0.13213094006396672,
 0.8500000000000001: 0.10693027505822388,
 0.9000000000000001: 0.06696681873181767,
 0.9500000000000001: 0.023157210956020278})

cookie_seq = ['c', 's', 'v', 'v', 'c']

aprobs = [0.3, 0.4615384615384615, 0.72, 0.8852459016393442, 0.7677725118483412]
bprobs = [1 - p for p in aprobs]

pos = {'healthy': 0.38983050847457623, 'sick': 0.6101694915254237}
neg = {'healthy': 0.9161425576519916, 'sick': 0.08385744234800838}

def dist_close(d1, d2):
    if d1.keys() != d2.keys():
        return False
    for key in d1:
        if not math.isclose(d1[key], d2[key]):
            return False
    return True

class Coin(inf.InferenceSuite):
    def likelihood(self, data, hypothesis):
        if data == "H":
            return hypothesis
        else:
            return 1 - hypothesis

def test_distribution():
    print("\nRunning tests on InferenceSuite class.\n")
    fail_count = 0
    test_dist = inf.InferenceSuite(benford_dict)
    
    mapest = test_dist.map()
    if mapest is not None:
        print("Testing MAP estimate on Benford's distribution: expect 1, got", mapest)
        if mapest != 1:
            fail_count += 1
    else:
        print("MAP estimate not implemented yet. Skipping test.")
        fail_count += 1

    meanest = test_dist.mean()
    if meanest is not None:
        print("Testing mean on Benford's distribution: expect 3.441, got", meanest)
        if not math.isclose(meanest, 3.441):
            fail_count += 1
        else:
            print("Test successful.")
    else:
        print("Mean not implemented yet. Skipping test.")
        fail_count += 1

    print("Testing quantile on coin distribution.")
    q1 = coin_dist.quantile(0.25)
    print("Testing quantile: expect 0.6, got", q1)
    if not math.isclose(0.6, q1):
        print("Test failed.")
        fail_count += 1
    else:
        print("Test successful.")
    q2 = coin_dist.quantile(0.9)
    print("Testing quantile: expect 0.85, got", q2)
    if not math.isclose(0.85, q2):
        print("Test failed.")
        fail_count += 1
    else:
        print("Test successful.")
    return fail_count

def test_subclass():
    print("Testing inference on a subclass.")
    c = Coin(np.arange(0.05, 1.0, 0.05))
    flips = ["T", "H", "H", "H", "H", "T", "H", "H"]
    for flip in flips:
        c.update(flip)
    if not dist_close(c.d, coin_dist.d):
        if make_plots:
            ax = plt.figure()
            plt.plot(list(c.d.keys()), list(c.d.values()))
            plt.plot(list(coin_dist.d.keys()), list(coin_dist.d.values()))
            plt.xlabel("Heads probability")
            plt.ylabel("Posterior probability")
            plt.legend(["Output", "Expected Output"])
            plt.savefig("inference_plots.png")
            print("Updating failed to produce correct probabilities.\nPlot saved as inference_plots.png.")
        else:
            print("Updating failed to produce correct probabilities.")
        return 1
    else:
        if make_plots:
            ax = plt.figure()
            plt.plot(list(c.d.keys()), list(c.d.values()))
            plt.plot(list(coin_dist.d.keys()), list(coin_dist.d.values()))
            plt.xlabel("Heads probability")
            plt.ylabel("Posterior probability")
            plt.legend(["Output", "Expected Output"])
            plt.savefig("inference_plots.png")
            print("Inference successful.\nPlot saved as inference_plots.png.")
        else:
            print("Inference successful.")
        return 0

def test_diagnosis():
    print("\nRunning tests on Diagnostic subclass.\n")
    fail_count = 0
    test_dist = inf.Diagnostic({'sick':0.08, 'healthy': 0.92})
    test_dist.update('+')
    print("Positive test result: expected",  pos, "and got", test_dist.d)
    if dist_close(test_dist.d, pos):
        print("Test successful.")
    else:
        print("Test failed.")
        fail_count += 1
    
    test_dist = inf.Diagnostic({'sick':0.08, 'healthy': 0.92})
    test_dist.update('-')
    print("Negative test result: expected", neg, "and got", test_dist.d)
    if dist_close(test_dist.d, neg):
        print("Test successful.")
    else:
        print("Test failed.")
        fail_count += 1
    return fail_count

def test_cookie():
    print("\nRunning tests on Cookie subclass.\n")
    fail_count = 0
    test_dist = inf.Cookie([0.3,0.3,0.4],[0.7,0.1,0.2])
    if test_dist.d != {1:0.5, 2:0.5}:
        print("Cookie test: initial distribution incorrect")
    for i in range(len(cookie_seq)):
        test_dist.update(cookie_seq[i])
        print("After update " + str(i+1) + ":", test_dist.d)
        print("Expected:", {1:aprobs[i], 2:bprobs[i]})
        if not math.isclose(test_dist.d[1], aprobs[i]):
            fail_count += 1
        if not math.isclose(test_dist.d[2], bprobs[i]):
            fail_count += 1
    return fail_count

def test_train():

    fail_count = 0
    print("\nRunning tests on Locomotive subclass.\n")

    print("Testing uniform prior.")
    t = inf.Locomotive(np.arange(1,1001))
    t.update(178)

    if not dist_close(t.d, unif_first):
        print("Incorrect probabilities after 1 update from uniform prior. Check plots to diagnose.")
        fail_count += 1

    if make_plots:
        ax = plt.figure()
        plt.plot(list(t.d.keys()), list(t.d.values()))
        plt.plot(list(unif_first.keys()), list(unif_first.values()))
        plt.title("Uniform prior, 1 update")
        plt.xlabel("N")
        plt.ylabel("Posterior probability")
        plt.legend(["Output", "Expected Output"])
        plt.savefig("unif_1.png")

    t.update(77)
    if not dist_close(t.d, unif_second):
        print("Incorrect probabilities after 2 updates from uniform prior. Check plots to diagnose.")
        fail_count += 1

    if make_plots:
        ax = plt.figure()
        plt.plot(list(t.d.keys()), list(t.d.values()))
        plt.plot(list(unif_second.keys()), list(unif_second.values()))
        plt.title("Uniform prior, 2 updates")
        plt.xlabel("N")
        plt.ylabel("Posterior probability")
        plt.legend(["Output", "Expected Output"])
        plt.savefig("unif_2.png")

    print("Testing power-law prior.")
    n = np.arange(1,1001)
    p = [k ** -1.1 for k in n]
    t = inf.Locomotive(dict(zip(n,p)))
    t.normalize()
    if make_plots:
        ax = plt.figure()
        plt.plot(list(t.d.keys()), list(t.d.values()))
        plt.plot(list(power_first.keys()), list(power_first.values()))
        plt.title("Power-law prior, no updates")
        plt.xlabel("N")
        plt.ylabel("Posterior probability")
        plt.legend(["Output", "Expected Output"])
        plt.savefig("power_1.png")

    if not dist_close(t.d, power_first):
        print("Incorrect probabilities after initialization from power-law prior. Check plots to diagnose.")
        fail_count += 1

    t.update(178)
    if make_plots:
        ax = plt.figure()
        plt.plot(list(t.d.keys()), list(t.d.values()))
        plt.plot(list(power_second.keys()), list(power_second.values()))
        plt.title("Power-law prior, 1 update")
        plt.xlabel("N")
        plt.ylabel("Posterior probability")
        plt.legend(["Output", "Expected Output"])
        plt.savefig("power_2.png")

    if not dist_close(t.d, power_second):
        print("Incorrect probabilities after 1 update from power-law prior. Check plots to diagnose.")
        fail_count += 1

    t.update(77)
    if make_plots:
        ax = plt.figure()
        plt.plot(list(t.d.keys()), list(t.d.values()))
        plt.plot(list(power_third.keys()), list(power_third.values()))
        plt.title("Power-law prior, 2 updates")
        plt.xlabel("N")
        plt.ylabel("Posterior probability")
        plt.legend(["Output", "Expected Output"])
        plt.savefig("power_3.png")
    
    if not dist_close(t.d, power_third):
        print("Incorrect probabilities after 2 updates from power-law prior. Check plots to diagnose.")
        fail_count += 1

    if fail_count == 0:
        print("All tests passed on Locomotive class.")

    return fail_count

#def test_tanks(filename):

def main():

    dist_failures = test_distribution()
    dist_failures += test_subclass()
    print("Ran 6 tests on InferenceSuite class, failed", dist_failures)

    diag_failures = test_diagnosis()
    print("Ran 2 tests on Diagnostic class, failed", diag_failures)
    cookie_failures = test_cookie()
    print("Ran 10 tests on Cookie class, failed", cookie_failures)
    train_failures = test_train()
    print("Ran 5 tests on Locomotive class, failed", train_failures)
    
if __name__ == "__main__":
    main()
