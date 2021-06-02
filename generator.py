
class generator:

    def __init__(self,seed):
        self.value = seed
        self.a = 747796405
        self.m = 4294967296
  
    def generateRandom(self):
        self.value = (self.a*self.value)%self.m
        return self.value

object = generator(2)
for i in range (1000):
    print(object.generateRandom())
