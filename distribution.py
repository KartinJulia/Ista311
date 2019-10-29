'''
Solution for HW 1
'''

import numpy as np

class Distribution(object):
    '''A class that defines a probability distribution.'''

    def __init__(self, dist):
        '''Initializes the distribution.
        After initialization, the instance has a single instance variable d (a dictionary), which represents a probability distribution.
        The keys of the dictionary are the outcomes; the values are the probabilities. Keys may have any (immutable) type, but values should always be floats.

        The dictionary is constructed:
        1. if dist is a dict, it becomes the dictionary
        2. if dist is a tuple, we assume the first element of the tuple is a list or other ordered iterable object containing the outcomes and the second is an ordered iterable containing probabilities.
        3. if dist is any other object, we attempt to iterate through, assuming equal probabilities. This allows passing a single list, range, etc.
        '''

        if isinstance(dist, dict):
            self.d = dist
        elif isinstance(dist, tuple):
            self.d = {}
            n = len(dist[0])
            for i in range(n):
                self.d.setdefault(dist[0][i], dist[1][i])
        else:
            self.d = {}
            n = len(dist)
            for elem in dist:
                self.d.setdefault(elem, 1/n)
        return None

    def prob(self, event):
        '''
        Returns the total probability of the given event.
        Parameters:
            event: a set, containing a subset of the keys of the distribution
        Returns: float
        '''
        p = 0
        for outcome in event:
            p += self.d[outcome]
        return p

    def normalize(self):
        '''
        Normalizes the probability distribution, ensuring that the values sum to 1.
        Parameters: none
        Returns: none
        '''
        totalprob = sum(self.d.values())
        for outcome in self.d:
            self.d[outcome] /= totalprob
        return None

    def condition(self, event):
        '''
        Replaces the distribution with the conditional distribution given an event.
        Parameters:
            event: a subset of the outcomes of the distribution
        Returns: none
        '''
        removals = set()
        # self.d = {k:self.d[k] for k in self.d if k in event}  ### the fancy way for Pythonistas
        for outcome in self.d:
            if not (outcome in event):
                removals.add(outcome)
        for outcome in removals:
            self.d.pop(outcome)
        self.normalize()
        return None

    def sample(self):
        '''
        Generates an outcome from the probability distribution.
        Parameters: none
        Returns: one of the keys of the dictionary (variable type)
        '''
        test = np.random.uniform()
        total = 0
        for outcome in self.d:
            if test < self.d[outcome] + total:
                return outcome
            total += self.d[outcome]
        return None
