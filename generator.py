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
        if (rand >= probability):
            return 0
        else:
            return 1
    
    def binomialDistribution(self,probablity, n):
        counter = 0
        for i in range(n):
            counter+=self.bernoulliDistribution(probablity)
        return counter

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

#======================================przedstawienie działania podstawowej wersji generatora===========================
# a = arr.array('d')
# object = generator(2)
# HowManyResults=100000
# for i in range(HowManyResults):
#     a.append(object.generateRandom())

# for i in range(HowManyResults):
#     print(a[i])

# plt.hist(a, bins=100)
# plt.show()

#========================przedstawienie działania generatora dla rozkładu jednostajnego==================================
# b = arr.array('d')
# object = generator(2)
# HowManyResults= 100

# for i in range(HowManyResults):
#     b.append(object.uniformDistribution()) 
#     print(b[i])
    
# plt.hist(b, bins=10)
# plt.show()

#========================================================chiKwadrat rozkład jednostajny==================================
# b = arr.array('d')
# object = generator(2)
# HowManyResults= 1000
# #tablice do testu chi kwadrat
# bins = 7
# quantity = [0] * bins
# expected = [0] * bins
# for i in range(len(expected)):
#     expected[i]=math.floor( HowManyResults/bins)

# for i in range(HowManyResults):
#     b.append(object.uniformDistribution())
#     j=0
#     for counter in range (bins):
#         jnext= j + 1/bins
#         if(b[i]>=j and b[i]<jnext):
#             quantity[counter]+=1
#         j+= 1/bins     

# for i in range(HowManyResults):
#     print(b[i])

# print("expected      quantity             chi kwadarat")
# for i in range(len(quantity)):
#     print(expected[i],quantity[i],(math.pow(quantity[i]-expected[i],2)/expected[i]),sep='              ')

# chiSum=0.0
# for i in range(len(expected)):
#     chiSum+=math.pow((quantity[i]-expected[i]),2)/expected[i]
# print("suma testu chi kwadrat = ",chiSum)
# plt.hist(b, bins=10)
# plt.show()

#==========================================przedstawienie działania generatora rozkładu Bernuliego=======================
# c = arr.array('d')
# object = generator(2)
# HowManyResults=100
# probablity = 0.4

# for i in range(HowManyResults):
#     c.append(object.bernoulliDistribution(probablity))
#     print(c[i])

# plt.hist(c, bins=2)
# plt.show()

#==========================================Test chi kwadrat Rozkład Bernuliego===========================================
# c = arr.array('d')
# object = generator(2)
# HowManyResults=1000
# probablity = 0.4
# bins =2
# quantity = [0] * bins
# expected = [0] * bins

# expected[1]=math.floor( HowManyResults*probablity)
# expected[0]=HowManyResults-expected[1]

# for i in range(HowManyResults):
#     c.append(object.bernoulliDistribution(probablity))
#     if(c[i]==0):
#         quantity[0]+=1
#     else:
#         quantity[1]+=1
# print("expected    quantity")
# chiKwardrat = math.pow((quantity[0]-expected[0]),2)/expected[0] + math.pow((quantity[1]-expected[1]),2)/expected[1]
# print(expected[0],quantity[0],sep='            ')
# print(expected[1],quantity[1],sep='            ')
# print("suma testu chi kwadrat=", chiKwardrat,sep=' ')
# # for i in range(HowManyResults):
# #     print(c[i])

# plt.hist(c, bins=2)
# plt.show()

#==========================================przedstawienie działania generatora rozkładu dwumianowego=====================
# d = arr.array('d')
# object = generator(2)
# HowManyResults=100
# probablity = 0.5
# samples=10

# for i in range(HowManyResults):
#     d.append(object.binomialDistribution(probablity,samples))
#     print(d[i])

# plt.hist(d, bins=10)
# plt.show()

#==========================================Test chi kwadrat Rozkład Dwumianowy===========================================
# def distrbBinom(n, p, k):
#     return (math.factorial(n)/(math.factorial(k)*math.factorial(n-k)))*math.pow(p,k)*math.pow((1-p),(n-k))
# d = arr.array('d')
# object = generator(2)
# HowManyResults=10000000
# probablity = 0.5
# samples=10
# bins = 11
# quantity = [0] * bins
# expected = [0] * bins
# for i in range (len(expected)):
#     expected[i]=math.floor(HowManyResults*distrbBinom(samples,probablity,i))
# for i in range(HowManyResults):
#     d.append(object.binomialDistribution(probablity,samples))
#     for counter in range(bins):
#         if(d[i]>=counter and d[i]<counter+1):
#             quantity[counter]+=1
# chiKwadrat = 0.0
# print("expected      quantity")
# for i in range (len(quantity)):
#     print(expected[i],quantity[i],sep='          ')
#     chiKwadrat+=math.pow((quantity[i]-expected[i]),2)/expected[i]
# # for i in range(HowManyResults):
# #     print(d[i])
# print("suma testu Chi kwadrat= ",chiKwadrat)
# plt.hist(d, bins=10)
# plt.show()

#==========================================przedstawienie działania Rozkład Poissona===========================================

# e = arr.array('d')
# object = generator(2)
# HowManyResults=100
# lambdapoiss=5

# for i in range(HowManyResults):
#     e.append(object.poissonDistribution(lambdapoiss))
#     print(e[i])

# plt.hist(e, bins=20)
# plt.show()

#==========================================Test chi kwadrat Rozkład Poissona===========================================
# def poisdistrb(lambda1, k):
#     return (math.exp(-lambda1)*math.pow(lambda1,k))/math.factorial(k)
# e = arr.array('d')
# object = generator(2)
# HowManyResults=10000
# lambdapoiss=5
# bins =16
# quantity = [0] * bins
# expected = [0] * bins
# for i in range(bins):
#     expected[i]=HowManyResults*poisdistrb(lambdapoiss,i)
# for i in range(HowManyResults):
#     e.append(object.poissonDistribution(lambdapoiss))
#     for counter in range(bins):
#         if(e[i]>=counter and e[i]<counter+1):
#             quantity[counter]+=1

# # for i in range(HowManyResults):
# #     print(e[i])
# chiKwadrat = 0.0
# print("expected              quantity")
# for i in range (len(quantity)-1):
#     print(expected[i],quantity[i],sep='          ')
#     chiKwadrat+=math.pow((quantity[i]-expected[i]),2)/expected[i]
# # for i in range(HowManyResults):
# #     print(d[i])
# print("suma testu Chi kwadrat= ",chiKwadrat)
# plt.hist(e, bins=20)
# plt.show()

#=========================================================================przedstawienie działania Rozkład Wykładniczy===================================
# f = arr.array('d')
# object = generator(2)
# HowManyResults=100

# for i in range(HowManyResults):
#     f.append(object.exponentialDistribution())
#     print(f[i])

# plt.hist(f, bins=50)
# plt.show()

#=========================================================================Test chi kwadrat Rozkład Wykładniczy===========================================
# f = arr.array('d')
# object = generator(2)
# bins =30
# prev=0
# HowManyResults=1000
# quantity = [0] * bins
# expected = [0] * bins
# c=bins/10
# for i in range(bins-1,-1,-1):
#     expected[i]=(math.exp(-c)-prev)
#     c-=0.1
#     prev += expected[i]
# for i in range (bins):
#     expected[i]*=HowManyResults
# for i in range(HowManyResults):
#     f.append(object.exponentialDistribution())
#     c=0
#     for j in range (bins):
#         if(f[i]>=c and f[i]<c+ 0.1):
#             quantity[j]+=1
#         c+=0.1
# chiKwadrat=0.0
# print("expected            quantity")
# for i in range (bins-1):
#     print(expected[i],quantity[i],sep='     ')
#     chiKwadrat+=math.pow((quantity[i]-expected[i]),2)/expected[i]

# print("suma testu chi kwadrat ",chiKwadrat)
# for i in range(HowManyResults):
#     print(f[i])

# plt.hist(f, bins=50)
# plt.show()
#=========================================================================prezentacja działania Rozkład Normalny===========================================
# g = arr.array('d')
# object = generator(2)
# HowManyResults=100
# for i in range(HowManyResults):
#     g.append(object.normalDistribution())
#     print(g[i])

# plt.hist(g, bins=20)
# plt.show()
#=========================================================================Test chi kwadrat Rozkład Normalny===========================================
# g = arr.array('d')
# object = generator(2)
# HowManyResults=100000
# bins=30
# quantity = [0] * bins
# expected = [0] * bins
# fi = [0] * 31
# fi[30]=0.9987
# fi[29]=0.9974
# fi[28]=0.9953
# fi[27]=0.9918
# fi[26]=0.9861
# fi[25]=0.9772
# fi[24]=0.9641
# fi[23]=0.9452
# fi[22]=0.9192
# fi[21]=0.8849
# fi[20]=0.8413
# fi[19]=0.7881
# fi[18]=0.7257
# fi[17]=0.6554
# fi[16]=0.5793
# fi[15]=0.5000
# j=30
# for i in range(15):
#     fi[i]=fi[j]
#     j-=1
# j=0
# for i in range(len(expected)):
#     if(i<14):
#         expected[i]=(fi[i]-fi[i+1])*HowManyResults
#         j+=1
#     if(i==14):
#         expected[i]=(fi[i]-fi[i+1])*HowManyResults
#     if(i>14):
#         expected[i]=((fi[i]-fi[i+1])*(-1))*HowManyResults
#         j+=1


# for i in range(HowManyResults):
#     g.append(object.normalDistribution())
#     c=-3
#     for j in range(len(quantity)):
#         if(g[i]>=c and g[i]<c+ 0.2):
#             quantity[j]+=1
#         c+=0.2
# chiKwadrat=0.0 
# for i in range (bins):
#     print(expected[i], quantity[i],sep='    ')
#     chiKwadrat+=math.pow((quantity[i]-expected[i]),2)/expected[i]
# print("suma testu chi kwadrat wynosi ",chiKwadrat)
# # plt.hist(g, bins=20)
# # plt.show()