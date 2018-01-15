import scipy as sc

import matplotlib as mp

import matplotlib.pyplot as plt

import numpy as np

import math

#Interest Match Algorithm:


#We want to create 3-D space to quantify qualitative traits. Then calculate the
#distance, we don't want any of that to be too far apart


#Political Spectrum
#Right to left scale, libertarian to authoritarian

#Music
#Old to New, Hipster to Mainstream, non western to western

#Sports
#Old to New #Individual to Group, hipster to mainstream,

#Personality profiles

#Stuart is a left - libertarian, into the blues, and playing soccer
Stuart = np.matrix([[-2, -2, 0],[3, -4, 4],[0, 4, 5]])

#Jeb is ultracapitalistic, into classical music , and plays golf
Jeb = np.matrix([[4, 1, 0],[-4, -3, 3],[-3, -3, -3]])

#Stephanie is a totalitarian, into dubstep, and plays basketball
Stephanie = np.matrix([[-1, 4, 0], [5, -4, -2], [2, 3, 4]])

print("Stuart")
print(Stuart)
print("Jeb")
print(Jeb)
print("Stephanie")
print(Stephanie)

print("Stuart and Jeb political spectrum difference")


def twodif(x1, y1, x2, y2):
    xdif = x2 - x1
    ydif = y2 - y1
    distance = math.sqrt((xdif**2 + ydif**2))
    return distance

def threedif(x1, y1, z1, x2, y2, z2):
    xdif = x2 - x1
    ydif = y2 - y1
    zdif = z2 - z1
    distance = math.sqrt((xdif**2 + ydif**2 + zdif**2))
    return distance

poldi = twodif(Stuart[0, 0], Stuart[0, 1], Jeb[0, 0], Jeb[0, 1])

print(poldi)

print("Jeb and Stephanie musical difference")
musdi = threedif(Jeb[1, 0],Jeb[1, 1],Jeb[1, 2], Stephanie[1,0], Stephanie[1, 1], Stephanie[1, 2])
print(musdi)
print("Stuart and Stephanie sport difference")
spodi = threedif(Stuart[2, 0], Stuart[2, 1], Stuart[2,2], Stephanie[2,0], Stephanie[2, 1], Stephanie[2, 2])
print(spodi)

a = (Stuart[0, 0], Jeb[0, 0])
b = (Stuart[0, 1], Jeb[0, 1])
sjp = plt.scatter(a, b)
plt.plot(a, b)
plt.axis([-5, 5, -5, 5])
plt.show()


         
#First dot is Stuart and the second dot is Jeb, the line represents their
#difference in opinions

###If I wanted to do 3D plot
##fig1 = plt.figure()
##ax = fig.gca(projection='3d')
##X = np.arange(-5, 5, 1)
##Y = np.arange(-5, 5, 1)
##X, Y = np.meshgrid(X, Y)
##to be continued

