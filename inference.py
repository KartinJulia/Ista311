'''
Name: jiatian wang
Date: 10/25/2019
Class: ISTA 311
Collaborators: Tao Ding
'''

# Imports
from distribution import Distribution
import numpy as np

# Main inference class
class InferenceSuite(Distribution):

    def update(self, data):
        for key in self.d.keys():
            self.d[key] = self.likelihood(data,hypothesis)
        self.normalize

    def map(self):
        maxi = 0
        result = ""
        for key in self.d.keys():
            if self.d[key] > maxi:
                maxi = self.d[key]
                result = key
        return result

    def mean(self):
        sumi = 0
        count = 0
        for key in self.d.keys():
            sumi += self.d[key]
            count += 1

        return sumi/count

    def quantile(self, p):
        lst = []
        for key in self.d.keys():
            lst.append(self.d[key])
        lst.sort()
        return lst[int(len(lst)*p)]

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


    def likelihood(self,data,hypothesis):
        disease=data
        if hypothesis=='sick':
            if disease:
                return 0.9
            else:
                return 0.1
        if hypothesis=='healty':
            if disease:
                return 0.05
            else:
                return 0.95

class Cookie(InferenceSuite):
    def __inti__(self,bowl1,bowl2):
        self.d={1:0.5,2:0.5}
        self.b1=bowl1
        self.b2=bowl2


    def likelihood(self,data,hypothesis):
        type=data
        if hypothesis==1:
            return 1/len(self.b1)
        if hypothesis==2:
            return 1/len(self.b2)


class Locomotive(InferenceSuite):
    def __init__(self,dist):
        self.d = dist

    def likelihood(self, data, hypothesis):
        k = data                     # This assignment isn't needed, just for clarity
        if hypothesis >= k:
            return 1/hypothesis
        else:
            return 0
def main():

    #3

    d1 = {}
    for i in range (1,1001):
        d1[i] = 1/1000
    d2 = {}
    for j in range (1,501):
        d2[j] = 1/500
    d3 = {}
    for k in range (1,301):
        d3[k] = 1/300

    l1 = Locomotive(d1)
    l2 = Locomotive(d2)
    l3 = Locomotive(d3)

    l1.likelihood(187,1000)
    l2.likelihood(169,500)
    l3.likelihood(299,300)


    print(l1.map())


# Don't forget to define main()!
if __name__ == '__main__':
    main()
