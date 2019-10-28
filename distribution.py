'''
Template for computational homework 1.
'''

class Distribution(object):
    '''A class that defines a probability distribution.'''

    def __init__(self, dist):
        '''Initializes the distribution.
        The dictionary is constructed:
        1. if dist is a dict, it becomes the dictionary
        2. if dist is a tuple, we assume the first element of the tuple is a list or other ordered iterable object containing the outcomes and the second is an ordered iterable containing probabilities.
        2. if dist is any other object, we attempt to iterate through, assuming equal probabilities. This allows passing a single list, range, etc.
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
