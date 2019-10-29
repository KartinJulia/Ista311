'''
Name: Ding tao
Date: 10/25/2019
Class: ISTA 311
Collaborators: jiatian wang
'''

# Imports
from distribution import Distribution
import numpy as np

# Main inference class
class InferenceSuite(Distribution):

    def update(self, data):
        for key in self.d.keys():
            self.d[key]=self.d[key]*self.likelihood(data,key)
        self.normalize()

    def map(self):
        max=0
        for key in self.d:
            if self.d[key]>max:
                max=self.d[key]
                hy=key
        return hy

    def mean(self):
        total=0
        for key in self.d:
            total+=key*self.d[key]
        return total

    def quantile(self, p):
        sum=0
        for key in self.d.keys():
            sum+=self.d[key]
            if sum>=p:
                return key

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
            if disease=="+":
                return 0.9
            else:
                return 0.1
        if hypothesis=='healthy':
            if disease=="+":
                return 0.05
            else:
                return 0.95

class Cookie(InferenceSuite):
    def __init__(self,bowl1,bowl2):
        self.d={1:0.5,2:0.5}
        self.b1=bowl1
        self.b2=bowl2


    def likelihood(self,data,hypothesis):
        type=data
        if hypothesis==1:
            if type=='c':
                return self.b1[0]
            if type=='v':
                return self.b1[1]
            if type=='s':
                return self.b1[2]
        if hypothesis==2:
            if type=='c':
                return self.b2[0]
            if type=='v':
                return self.b2[1]
            if type=='s':
                return self.b2[2]

class Locomotive(InferenceSuite):

    def likelihood(self, data, hypothesis):
        k = data                     # This assignment isn't needed, just for clarity
        if hypothesis >= k:
            return 1/hypothesis
        else:
            return 0


def main():
    d1 = {}
    for i in range (1,1001):
        d1[i] = 1

    d2 = {}
    for j in range (1,301):
        d2[j] = j^(-2)

    d3 = {}
    for k in range (1,501):
        d3[k] = k^5


    l1 = Locomotive(d1)
    l2 = Locomotive(d2)
    l3 = Locomotive(d3)

    l1.normalize()
    l2.normalize()
    l3.normalize()

    l1.likelihood(187,1000)
    l2.likelihood(169,300)
    l3.likelihood(299,500)

    print("Maximum a posteriori estimate: ",l1.map(),"Mean: ",l1.mean()," 90% credible interval: ",l1.quantile(0.9))
    print("Maximum a posteriori estimate: ",l2.map(),"Mean: ",l2.mean()," 90% credible interval: ",l2.quantile(0.9))
    print("Maximum a posteriori estimate: ",l3.map(),"Mean: ",l3.mean()," 90% credible interval: ",l3.quantile(0.9))









# Don't forget to define main()!
if __name__ == '__main__':
    main()
