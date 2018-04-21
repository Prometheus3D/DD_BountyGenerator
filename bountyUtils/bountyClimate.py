import random
def seasonPicker():
    season = ['summer', 'winter', 'fall', 'spring']
    season = random.choice(season)
    if season == 'summer':
        baseTemp = random.randint(60,81)
        odfDie = random.randint(1,5)*10
        totalTemp = (baseTemp + odfDie)
        weather = ['clear', 'light rain', 'heavy rain', 'strong wind', 'light wind']
        weather = random.choice(weather)
    elif season == 'spring':
        baseTemp = random.randint(45,61)
        odfDie = random.randint(1,5)*10
        totalTemp = (baseTemp + odfDie)
        weather = ['clear', 'light rain', 'heavy rain', 'strong wind', 'light wind']
        weather = random.choice(weather)
    else:
        baseTemp = random.randint(0,41)
        odfDie = random.randint(1,5)*10
        totalTemp = (baseTemp + odfDie)
        weather = ['clear', 'light snowfall', 'heavy snowfall', 'strong wind', 'light wind', 'foggy']
        weather = random.choice(weather)

    disadvantage = statImpact(weather)
    weather = weather.title()
    season = season.title()
    conditions = dict(Season=season, Temperature=totalTemp,Weather=weather, Disadvantage=disadvantage)
    return conditions

def timeDay():
    d = ['dawn', 'morning', 'afternoon', 'evening', 'dusk']
    d = random.choice(d)
    d = d.title()
    return d
def statImpact(x):
    if x == 'heavy rain':
        r = 'on wisdom(perception) checks that reply on sight. Rain extinguishes open flames and imposes disadvantage on wisdom(perception) checks that rely on hearing.'
        r = r.title()
        return r
    elif x == 'heavy snowfall':
        r = 'on wisdom(perception) checks that reply on sight.'
        r = r.title()
        return r
    elif x == 'foggy':
        r = 'on wisdom(perception) checks that reply on sight.'
        r = r.title()
        return r
    elif x == 'strong wind':
        r = 'on ranged weapon attack rolls and wisdom (perception) checks that reply on hearing.'
        r = r.title()
        return r
    else:
        r = 'No distadvantages'
        r = r.title()
        return r
def terrainPicker():
    t = ['arctic', 'coast', 'desert', 'forest', 'grassland', 'mountain', 'swamp', 'city']
    t = random.choice(t)
    t = t.title()
    return t

def climatePicker():
    sP = seasonPicker()
    s = sP['Season']
    t = sP['Temperature']
    w = sP['Weather']
    d = sP['Disadvantage']
    target = dict(Terrain=terrainPicker(),TimeofDay=timeDay(),Season=s,Temperature=t,
                  Weather=w, Disadvantage=d)
    t = target
    return t
    # for key in t.keys():
    #     value = t[key]
    #     print(key, ':', value)
