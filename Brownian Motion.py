#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

# Number of steps and step size
n_steps = 1000
delta_t = 1
sigma = np.sqrt(delta_t)  # The standard deviation is usually taken as √(delta_t)

# Starting point
x = np.zeros(n_steps)
y = np.zeros(n_steps)

# Brownian motion
for i in range(1, n_steps):
    x[i] = x[i-1] + np.random.normal(0, sigma)
    y[i] = y[i-1] + np.random.normal(0, sigma)

# Graphic drawing
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Brownian Motion')
plt.title('Brownian Motion Simulation')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.legend()
plt.show()


# In[ ]:




