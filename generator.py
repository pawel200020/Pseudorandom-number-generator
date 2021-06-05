import numpy as np
from matplotlib import pyplot as plt
import array as arr


class generator:

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
        if ( rand<= probability):
            return 0
        else:
            return 1

    def binomialDistribution(self,probablity, n):
        counter = 0
        for i in range(n):
            counter+=self.bernoulliDistribution(probablity)
        return counter

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
# HowManyResults=1000
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
d = arr.array('d')
object = generator(2)
HowManyResults=10000
probablity = 0.5
samples=10
for i in range(HowManyResults):
    d.append(object.binomialDistribution(probablity,samples))

for i in range(HowManyResults):
    print(d[i])

plt.hist(d, bins=10)
plt.show()

