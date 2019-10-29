'''
Tests for ISTA 311 Programming HW 1.
Requires scipy, matplotlib.

Runs 3 tests on each of sample() and prob(), 2 tests on normalize(), 1 test on condition().
Produces 3 graphs for the results of sample().

Author: Dylan Murphy
'''

import random
import math
import scipy as sp
from scipy import stats             # We use chi-square goodness-of-fit tests to check that 
import matplotlib.pyplot as plt

from distribution import Distribution

plot_tests = True                   # Comment this out to skip plotting

###############################
# Test Suite
###############################

##  Test Distributions

# Uniform distribution test: Rolling a 10-sided die

unif_dist = {1: 1/10,
             2: 1/10,
             3: 1/10,
             4: 1/10,
             5: 1/10,
             6: 1/10,
             7: 1/10,
             8: 1/10,
             9: 1/10,
             10: 1/10}

# Non-uniform, three options: drawing a colored ball from an urn

rgb =  {"red": 3/18,
        "green": 7/18,
        "blue": 8/18}

# Benford's law distribution for digits 1-9

benford = {1: 0.301,
           2: 0.176,
           3: 0.125,
           4: 0.097,
           5: 0.079,
           6: 0.067,
           7: 0.058,
           8: 0.051,
           9: 0.046}

benford_set_a = {2, 8, 9}
benford_set_b = {1, 3, 7, 8, 9}

# RGB urn problem, but given in terms of natural frequencies

rgb_unscaled = {"red": 3,
                "green": 7,
                "blue": 8}

letters = {"a": 0.0575,
           "b": 0.0128,
           "c": 0.0263,
           "d": 0.0285,
           "e": 0.0913,
           "f": 0.0173,
           "g": 0.0133,
           "h": 0.0313,
           "i": 0.0599,
           "j": 0.0006,
           "k": 0.0084,
           "l": 0.0335,
           "m": 0.0235,
           "n": 0.0596,
           "o": 0.0689,
           "p": 0.0192,
           "q": 0.0008,
           "r": 0.0508,
           "s": 0.0567,
           "t": 0.0706,
           "u": 0.0334,
           "v": 0.0069,
           "w": 0.0119,
           "x": 0.0073,
           "y": 0.0164,
           "z": 0.0006,
           " ": 0.1927}

vowels = {'a': 0.18488745980707397,
          'e': 0.2935691318327974,
          'i': 0.19260450160771705,
          'o': 0.22154340836012862,
          'u': 0.10739549839228296}



letters_unscaled = {"a": 575,
                    "b": 128,
                    "c": 263,
                    "d": 285,
                    "e": 913,
                    "f": 173,
                    "g": 133,
                    "h": 313,
                    "i": 599,
                    "j": 6,
                    "k": 84,
                    "l": 335,
                    "m": 235,
                    "n": 596,
                    "o": 689,
                    "p": 192,
                    "q": 8,
                    "r": 508,
                    "s": 567,
                    "t": 706,
                    "u": 334,
                    "v": 69,
                    "w": 119,
                    "x": 73,
                    "y": 164,
                    "z": 6,
                    " ": 1927}

vowel_set = {'a', 'e', 'i', 'o', 'u'}

## Testing the set probability

def test_prob():
    unif_set = {1, 5, 7, 8}
    rgb_set = {"red", "green"}
    passed_count = 0

    print("Test 1: Uniform distribution on integers 1-10.\nTest set: {1, 5, 7, 8}\nExpected result: 0.4")
    d = Distribution(unif_dist)
    result = d.prob(unif_set)
    print("Result:", result)
    if math.isclose(0.4, result):
        print("Test PASSED")
        passed_count += 1
    else:
        print("Test FAILED")

    print("Test 2: Drawing from an urn with 3 red, 7 green, 8 blue balls.\nTest set: {\"red\", \"green\"}\nExpected result: 10/18")
    d = Distribution(rgb)
    result = d.prob(rgb_set)
    print("Result:", result)
    if math.isclose(10/18, result):
        print("Test PASSED")
        passed_count += 1
    else:
        print("Test FAILED")

    print("Test 3: Benford's law on digits 1-9.\nTest set: {2, 8, 9}\nExpected result: 0.273")
    d = Distribution(benford)
    result = d.prob(benford_set_a)
    print("Result:", result)
    if math.isclose(0.273, result):
        print("Test PASSED")
        passed_count += 1
    else:
        print("Test FAILED")

    '''
    if setbonus:
        print("Test 4: Union of two sets using Benford's law.\nTest sets: {2, 8, 9}, {1, 2, 7, 8}\nExpected result: .632")
        result = probfunc(benford, benford_set_a, benford_set_b)
        print("Result:", result)
        if math.isclose(0.632, result):
            print("Test PASSED")
        else:
            print("Test FAILED")
    '''
    return passed_count

## Testing union and intersection
'''
def test_op(andfunc, orfunc):
    passed_count = 0

    print("Test 1: Benford's law on digits 1-9.\nTest sets: {2, 8, 9}, {1, 3, 7, 8, 9}")
    andresult = andfunc(benford, benford_set_a, benford_set_b)
    orresult = orfunc(benford, benford_set_a, benford_set_b)
    print("Expected result (and/intersection): 0.097\nResult:", andresult)
    print("Expected result (or/union): 0.757\nResult:", orresult)
    if math.isclose(andresult, 0.097) and math.isclose(orresult, 0.757):
        print("Test PASSED")
        passed_count += 1
    else:
        print("Test FAILED")
    
    print("Test 2: Letters in English text.\nTest sets: {a, b, c, d, e}, {b, d, n, t, x}")
    andresult = andfunc(letters, letter_set_a, letter_set_b)
    orresult = orfunc(letters, letter_set_a, letter_set_b)
    print("Expected result (and/intersection): 0.0413\nResult:", andresult)
    print("Expected result (or/union): 0.3539\nResult:", orresult)
    if math.isclose(andresult, .0413) and math.isclose(orresult, .3539):
        print("Test PASSED")
        passed_count += 1
    else:
        print("Test FAILED")
    return passed_count
'''
## Testing normalization

def test_norm():
    passed_count = 0

    print("Test 1: letter frequencies in English text")
    temp_dict = letters_unscaled.copy()
    d = Distribution(temp_dict)
    d.normalize()
    passed = True
    for key in d.d:
        if not math.isclose(letters[key], d.d[key]):
            passed = False
            print("Probability of", key, d.d[key], "does not match expected probability", letters[key])
    if passed:
        print("Test PASSED")
        passed_count += 1
    else:
        print("Test FAILED")
    print("Test 2: drawing from an urn")
    temp_dict = rgb_unscaled.copy()
    d = Distribution(temp_dict)
    d.normalize()
    passed = True
    for key in rgb:
        if not math.isclose(rgb[key], d.d[key]):
            passed = False
            print("Probability of", key, d.d[key], "does not match expected probability", letters[key])
    if passed:
        print("Test PASSED")
        passed_count += 1
    else:
        print("Test FAILED")
    return passed_count

## Testing the simulation
# Uses a chi-square goodness-of-fit test.

def test_condition():
    passed_count = 0
    print("Testing conditioning.\nComputing conditional distribution of letters, conditional on vowels.")

    d = Distribution(letters)
    d.condition(vowel_set)
    print("Expected distribution:\n", vowels)
    print("Result:\n", d.d)
    passed = True
    for key in vowels:
        if not math.isclose(vowels[key], d.d[key]):
            passed = False
            print("Probability of", key, d.d[key], "does not match expected probability", vowels[key])
    if passed:
        print("Test PASSED")
        passed_count += 1
    else:
        print("Test FAILED")
    return passed_count

def test_sim():
    passed_count = 0

    print("Test 1: Uniform distribution")
    d = Distribution(unif_dist)
    result = sp.zeros(10)
    for i in range(10000):
        out = d.sample()
        result[out-1] += 1
    csr = sp.stats.chisquare(result, 1000 * sp.ones(10))
    print("Observed frequencies:", result)
    print("Expected frequencies:", 1000 * sp.ones(10))
    print("Chi-square statistic:", csr.statistic)
    print("p-value: ", csr.pvalue)
    if csr.pvalue < 0.01:
        print("Test FAILED")
    else:
        print("Test PASSED")
        passed_count += 1

    if plot_tests:
        plt.figure()
        plt.subplot(2, 1, 1)
        plt.bar(x = 1 + sp.arange(10), height=result, tick_label = 1 + sp.arange(10))
        plt.title("Uniform distribution: observed (top) vs. expected (bottom)")
        plt.subplot(2, 1, 2)
        plt.bar(x = 1 + sp.arange(10), height=0.1*sp.ones(10), tick_label = 1 + sp.arange(10))
        plt.savefig("uniform.png")

    print("Test 2: Drawing from an urn")
    result = sp.zeros(3)
    picks = []
    d = Distribution(rgb)
    for i in range(10000):
        picks.append(d.sample())
    result[0] = sum([pick == "red" for pick in picks])
    result[1] = sum([pick == "green" for pick in picks])
    result[2] = sum([pick == "blue" for pick in picks])
    csr = sp.stats.chisquare(result, (10000/18) * sp.array([3,7,8]))
    print("Observed frequencies:", result)
    print("Expected frequencies:", (10000/18) * sp.array([3,7,8]))
    print("Chi-square statistic:", csr.statistic)
    print("p-value: ", csr.pvalue)
    if csr.pvalue < 0.01:
        print("Test FAILED")
    else:
        print("Test PASSED")
        passed_count += 1

    if plot_tests:
        plt.figure()
        plt.subplot(2, 1, 1)
        plt.bar(x = sp.arange(3), height=result, tick_label = ["red", "green", "blue"])
        plt.title("Uniform distribution: observed (top) vs. expected (bottom)")
        plt.subplot(2, 1, 2)
        plt.bar(x = sp.arange(3), height=(1/18)*sp.array([3,7,8]), tick_label = ["red", "green", "blue"])
        plt.savefig("urn.png")

    print("Test 3: Benford's law")
    result = sp.zeros(9)
    d = Distribution(benford)
    for i in range(10000):
        out = d.sample()
        result[out-1] += 1
    csr = sp.stats.chisquare(result, 10000 * sp.array([0.301, 0.176, 0.125, 0.097, 0.079, 0.067, 0.058, 0.051, 0.046]))
    print("Observed frequencies:", result)
    print("Expected frequencies:", 10000 * sp.array([0.301, 0.176, 0.125, 0.097, 0.079, 0.067, 0.058, 0.051, 0.046]))
    print("Chi-square statistic:", csr.statistic)
    print("p-value: ", csr.pvalue)
    if csr.pvalue < 0.01:
        print("Test FAILED")
    else:
        print("Test PASSED")
        passed_count += 1

    if plot_tests:
        plt.figure()
        plt.subplot(2, 1, 1)
        plt.bar(x = 1 + sp.arange(9), height=result / 10000, tick_label = 1 + sp.arange(9))
        plt.title("Uniform distribution: observed (top) vs. expected (bottom)")
        plt.subplot(2, 1, 2)
        plt.bar(x = 1 + sp.arange(9), height=sp.array([0.301, 0.176, 0.125, 0.097, 0.079, 0.067, 0.058, 0.051, 0.046]), tick_label = 1 + sp.arange(9))
        plt.savefig("benford.png")

    '''
    if simbonus:
        print("Test 4: Drawing from an urn, with a non-normalized distribution")
        result = sp.zeros(3)
        picks = []
        for i in range(10000):
            picks.append(simfunc(rgb_unscaled))
        result[0] = sum([pick == "red" for pick in picks])
        result[1] = sum([pick == "green" for pick in picks])
        result[2] = sum([pick == "blue" for pick in picks])
        csr = sp.stats.chisquare(result, (10000/18) * sp.array([3,7,8]))
        print("Observed frequencies:", result)
        print("Expected frequencies:", (10000/18) * sp.array([3,7,8]))
        print("Chi-square statistic:", csr.statistic)
        print("p-value: ", csr.pvalue)
        if csr.pvalue < 0.01:
            print("Test FAILED")
        else:
            print("Test PASSED")

        plt.figure()
        plt.subplot(2, 1, 1)
        plt.bar(x=sp.arange(3), height=result, tick_label = ["red", "green", "blue"])
        plt.title("Uniform distribution: observed (top) vs. expected (bottom)")
        plt.subplot(2, 1, 2)
        plt.bar(x=sp.arange(3), height=(1/18)*sp.array([3,7,8]), tick_label = ["red", "green", "blue"])
        plt.savefig("urnbonus.png")
    '''

    return passed_count

def main():

    '''
    setbonus_choice = input("Test bonus functionality for set probability? (y/N) ")

    if setbonus_choice == "y":
        setbonus = True
    else:
        setbonus = False
    
    simbonus_choice = input("Test bonus functionality for simulation? (y/N) ")
    
    if simbonus_choice == "y":
        simbonus = True
    else:
        simbonus = False
    '''

    ran_count = 0
    passed_count = 0
    ans = input("Test prob() method? (Y/n) ")
    if ans != 'n' and ans != 'N':
        ran_count += 3
        passed_count += test_prob()
    #input("Press Enter to test and/or calculation.")
    #passed_count += test_op(comp1.and_prob, comp1.or_prob)
    
    ans = input("Test normalize() method? (Y/n) ")
    if ans != 'n' and ans != 'N':
        ran_count += 2
        passed_count += test_norm()

    ans = input("Test condition() method? (Y/n) ")
    if ans != 'n' and ans != 'N':
        ran_count += 1
        passed_count += test_condition()

    ans = input("Test sample() method? (Y/n) ")        
    if ans != 'n' and ans != 'N':
        ran_count += 3
        passed_count += test_sim()
        if plot_tests:
            print("Plots saved to this directory. Check plots for diagnostics.")

    print("Overall result: ran", ran_count, "tests, skipped", 9 - ran_count, "tests, passed", passed_count, "tests.")
    return None

if __name__ == "__main__":
    main()
