import numpy as np
import random
import matplotlib.pyplot as plt

a=[]

mu=2
sigma=3

for i in range(100):
    a.append(random.normalvariate(mu,sigma))

plt.subplot(1,2,1)
plt.boxplot(a)
plt.subplot(1,2,2)
plt.plot(a)
plt.show()

