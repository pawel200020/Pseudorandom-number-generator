
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


a = arr.array('d')
object = generator(2)
for i in range(100000):
    a.append(object.generateRandom())

for i in range(10000):
    print(a[i])

plt.hist(a, bins=10000)
plt.show()
