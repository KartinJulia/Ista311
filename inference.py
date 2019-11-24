'''
Name:
Date:
Class: ISTA 311
Collaborators:
'''

# Imports
from distribution import Distribution
import numpy as np

import scipy as sp
from scipy import stats



# Main inference class
class InferenceSuite(Distribution):

    def update(self, data):
        for hypothesis in self.d:
            self.d[hypothesis] *= self.likelihood(data, hypothesis)
        self.normalize()

    def map(self):
        max_p = 0
        max_x = 0
        for x in self.d:
            if self.d[x] > max_p:
                max_x = x
                max_p = self.d[x]
        return max_x

    def mean(self):
        return sum([x * self.d[x] for x in self.d])

    def quantile(self, p):
        totalp = 0
        for x in sorted(self.d):
            totalp += self.d[x]
            if totalp >= p:
                return x

    def likelihood(self, data, hypothesis):
        '''
        Computes the likelihood of the given data under the hypothesis.
        '''
        raise NotImplementedError

class Mayor(InferenceSuite):
    '''
    An example application of the InferenceSuite class.

    Note that not every application will require redefining __init__, but every application of
    InferenceSuite should have a working likelihood method.
    '''
    def __init__(self):
        self.d = {'A':0.25, 'B':0.35, 'C':0.40}

    def likelihood(self, data, hypothesis):
        bridge_built = data                     # This assignment isn't needed, just for clarity
        if hypothesis == 'A':
            if bridge_built:
                return 0.6
            else:
                return 0.4
        if hypothesis == 'B':
            if bridge_built:
                return 0.9
            else:
                return 0.1
        if hypothesis == 'C':
            if bridge_built:
                return 0.8
            else:
                return 0.2

class Diagnostic(InferenceSuite):
    def likelihood(self, data, hypothesis):
        if hypothesis == 'healthy':
            if data == '+':
                return 0.05
            else:
                return .95
        if hypothesis == 'sick':
            if data == '+':
                return 0.9
            else:
                return 0.1

class Cookie(InferenceSuite):
    def __init__(self, bowl1, bowl2):
        self.d = {1: 0.5, 2:0.5}
        self.bowl1probs = dict(zip(['c','v','s'], bowl1))
        self.bowl2probs = dict(zip(['c','v','s'], bowl2))

    def likelihood(self, data, hypothesis):
        if hypothesis == 1:
            return self.bowl1probs[data]
        if hypothesis == 2:
            return self.bowl2probs[data]

class Locomotive(InferenceSuite):
    def likelihood(self, data, hypothesis):
        if hypothesis < data:
            return 0.0
        else:
            return 1.0 / hypothesis





# Don't forget to define main()!
if __name__ == '__main__':
    main()
