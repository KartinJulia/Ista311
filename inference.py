'''
Name: Jiatian Wang
Date: 10/24/2019
Class: ISTA 311
Collaborators:
'''

# Imports
from distribution import Distribution
import numpy as np

# Main inference class
class InferenceSuite(Distribution):

    def update(self, data):
        pass

    def map(self):
        pass

    def mean(self):
        pass

    def quantile(self, p):
        pass

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




# Don't forget to define main()!
if __name__ == '__main__':
    main()
