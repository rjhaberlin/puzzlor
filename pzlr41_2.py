# -*- coding: utf-8 -*-
"""
Informs Puzzlor 41_2
Your government has lost track of a high profile foreign spy and they have 
requested your help to track him down. As part of his attempts to evade 
capture, the spy has employed a simple strategy. Each day the spy moves from 
the country that he is currently in to a neighboring country.

The spy cannot skip over a country (for example, he cannot go from Chile to 
Ecuador in one day). The movement probabilities are equally distributed 
among the neighboring countries. For example, if the spy is currently in 
Ecuador, there is a 50 percent chance he will move to Colombia and a 50 
percent chance he will move to Peru. The spy was last seen in Chile and will 
only move about countries that are in South America. He has been moving about 
the countries for several weeks.

Which country is the spy most likely hiding in and how likely is it that he is
there?

Rick Haberlin
"""
import numpy as np
import random
import pandas as pd
np.set_printoptions(precision=2)

# south america
sa = ['co','ec','pe','bo','ch','ar','ur','pa','br','ve','gu','su','fr']

# transition matrix for south america
co = np.array([0.00,0.25,0.25,0.00,0.00,0.00,0.00,0.00,0.25,0.25,0.00,0.00,0.00])
ec = np.array([0.50,0.00,0.50,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00])
pe = np.array([0.20,0.20,0.00,0.20,0.20,0.00,0.00,0.00,0.20,0.00,0.00,0.00,0.00])
bo = np.array([0.00,0.00,0.20,0.00,0.20,0.20,0.00,0.20,0.20,0.00,0.00,0.00,0.00])
ch = np.array([0.00,0.00,0.33,0.33,0.00,0.33,0.00,0.00,0.00,0.00,0.00,0.00,0.00])
ar = np.array([0.00,0.00,0.00,0.20,0.20,0.00,0.20,0.20,0.20,0.00,0.00,0.00,0.00])
ur = np.array([0.00,0.00,0.00,0.00,0.00,0.50,0.00,0.00,0.50,0.00,0.00,0.00,0.00])
pa = np.array([0.00,0.00,0.00,0.33,0.00,0.33,0.00,0.00,0.33,0.00,0.00,0.00,0.00])
br = np.array([0.10,0.00,0.10,0.10,0.00,0.10,0.10,0.10,0.00,0.10,0.10,0.10,0.10])
ve = np.array([0.33,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.33,0.00,0.33,0.00,0.00])
gu = np.array([0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.33,0.33,0.00,0.33,0.00])
su = np.array([0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.33,0.00,0.33,0.00,0.33])
fr = np.array([0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.50,0.00,0.00,0.50,0.00])

# cumulative transition matrix
cco = np.cumsum(co)
cec = np.cumsum(ec)
cpe = np.cumsum(pe)
cbo = np.cumsum(bo)
cch = np.cumsum(ch)
car = np.cumsum(ar)
cur = np.cumsum(ur)
cpa = np.cumsum(pa)
cbr = np.cumsum(br)
cve = np.cumsum(ve)
cgu = np.cumsum(gu)
csu = np.cumsum(su)
cfr = np.cumsum(fr)

# consolidated transition matrix
trans_mat = np.array([[cco],[cec],[cpe],[cbo],[cch],[car],[cur],[cpa],[cbr],[cve],[cgu],[csu],[cfr]])

# initialize
days = 100
current = 4 # start in chile
spy = pd.Series([0,0,0,0,0,0,0,0,0,0,0,0,0],index=sa)

for d in range(days):
    # increment country count
    spy[current] += 1
    # randomly select next country
    roll = random.random()
    # update current
    ind = roll <= trans_mat[current]
    i,current = np.unravel_index(ind.argmax(), ind.shape)

spy /= days
print spy.order(ascending=False) 
