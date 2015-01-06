# -*- coding: utf-8 -*-
"""
Created on Mon Dec 29 10:49:04 2014

@author: rhaberlin
"""

import random
import string
import pandas as pd

field = ['allen','barry','charles','dan']
score = pd.Series([0,0,0,0],index=field)

for r in range(1000):
    field = ['allen','barry','charles','dan']
    health = pd.Series([10, 12, 16, 18],index=field)
    attack = pd.Series([4, 3, 2, 1],index=field)

        
    while len(field) > 1:
        draw = field
        attacker = random.choice(draw)
        defender = random.choice(draw)
        if attacker != defender:
            health[defender] -= attack[attacker]
        if health[defender] <= 0:
            field.remove(defender)
            
    winner = string.join(draw)    
    if winner == 'allen':
        score['allen'] += 1
    elif winner == 'barry':
        score['barry'] += 1
    elif winner == 'charles':
        score['charles'] += 1
    else:
        score['dan'] += 1
        
print score.order(ascending=False)    

