import random

def proofType():
    p = ['Head', 'Arm', 'Leg', 'Tooth', 'Lock of Hair', 'Ring', 'Any', 'Armor']
    p = random.choice(p)
    return p

def killType():
    t = ['Look like an accident', 'brutal public murder', 'silent assassination', 'sabotage']
    t = random.choice(t)
    t = t.title()
    return t

def weaponUsed():
    w = ['poison', 'simple melee weapon', 'simple ranged weapon',
         'martial melee weapon', 'martial ranged weapon', 'any']
    w = random.choice(w)
    w = w.title()
    return w

def guardKill():
    g = ['Yes','No']
    g = random.choice(g)
    return g

def Objectives():
    g = guardKill()
    p = proofType()
    t = killType()
    w = weaponUsed()
    return p, t, w, g