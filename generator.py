import numpy as np
from matplotlib import pyplot as plt
import array as arr
import math


class generator:
    whichOne = 0
    prevValue = 0

    def __init__(self, seed):
        self.value = seed
        self.a = 747796405
        self.m = 4294967296

    def generateRandom(self):
        self.value = (self.a*self.value) % self.m
        return self.value

    def uniformDistribution(self):
        return self.generateRandom()/self.m

    def bernoulliDistribution(self, probability):
        rand = self.uniformDistribution()
        if (rand <= probability):
            return 0
        else:
            return 1

    def poissonDistribution(self, lambdapoiss):
        limit = math.exp(-lambdapoiss)
        n = 0
        p = self.uniformDistribution()
        while(p >= limit):
            n += 1
            p *= self.uniformDistribution()
        return n

    def exponentialDistribution(self):
        return -math.log(1-self.uniformDistribution())

    def normalDistribution(self):
        if(self.whichOne == 1):
            self.whichOne = 0
            return self.prevValue
        else:
            x = self.uniformDistribution()*2-1
            y=self.uniformDistribution()*2-1
            s=x*x+y*y
            while (s>=1 or s==0):
                x = self.uniformDistribution()*2-1
                y=self.uniformDistribution()*2-1
                s=x*x+y*y
            s=math.sqrt((math.log(s)*(-2))/s)
            self.prevValue=y*s
            self.whichOne=1
        return x*s


#!!!!Dla dużych liczb należy wykomentować wypisanie wartości!!!!

#przedstawienie działania podstawowej wersji generatora
# a = arr.array('d')
# object = generator(2)
# HowManyResults=1000
# for i in range(HowManyResults):
#     a.append(object.generateRandom())

# for i in range(HowManyResults):
#     print(a[i])

# plt.hist(a, bins=100)
# plt.show()

#przedstawienie działania zmodyfikowanej wersji dla rozkładu jednostajnego
# b = arr.array('d')
# object = generator(2)
# HowManyResults=100000
# for i in range(HowManyResults):
#     b.append(object.uniformDistribution())

# for i in range(HowManyResults):
#     print(b[i])

# plt.hist(b, bins=10)
# plt.show()

#przedstawienie działania zmodyfikowanej wersji dla rozkładu Bernoulliego
# c = arr.array('d')
# object = generator(2)
# HowManyResults=100
# probablity = 0.4
# for i in range(HowManyResults):
#     c.append(object.bernoulliDistribution(probablity))

# for i in range(HowManyResults):
#     print(c[i])

# plt.hist(c, bins=2)
# plt.show()

#przedstawienie działania zmodyfikowanej wersji dla rozkładu dwumianowego
# d = arr.array('d')
# object = generator(2)
# HowManyResults=10000
# probablity = 0.5
# samples=10
# for i in range(HowManyResults):
#     d.append(object.binomialDistribution(probablity,samples))

# for i in range(HowManyResults):
#     print(d[i])

# plt.hist(d, bins=10)
# plt.show()

#przedstawienie działania zmodyfikowanej wersji dla rozkładu poissona
# e = arr.array('d')
# object = generator(2)
# HowManyResults=100000
# lambdapoiss=5
# for i in range(HowManyResults):
#     e.append(object.poissonDistribution(lambdapoiss))

# for i in range(HowManyResults):
#     print(e[i])

# plt.hist(e, bins=20)
# plt.show()

#przedstawienie zmodyfikowanej wersji dla rozkładu wykładniczego
# f = arr.array('d')
# object = generator(2)
# HowManyResults=1000
# for i in range(HowManyResults):
#     f.append(object.exponentialDistribution())

# for i in range(HowManyResults):
#     print(f[i])

# plt.hist(f, bins=50)
# plt.show()

#przedstawienie zmodyfikowanej wersji dla rozkładu normalnego
# g = arr.array('d')
# object = generator(2)
# HowManyResults=100
# for i in range(HowManyResults):
#     g.append(object.normalDistribution())

# for i in range(HowManyResults):
#     print(g[i])

# plt.hist(g, bins=20)
# plt.show()
