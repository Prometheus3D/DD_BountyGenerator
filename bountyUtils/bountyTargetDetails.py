import random
import bountyClimate as cC
import bountyObjectives as bO

def racePicker():
        race = ['Dwarf','High Elf','Wood Elf','Dark Elf','Halfling','Human','Dragonborn','Forest Gnome','Rock Gnome',
                'Half-Elf','Half-Orc','Tiefling']
        race = random.choice(race)
        return race
def classPicker():
        classes = ['barbarian','bard','cleric','druid','fighter','monk','paladin','ranger','rogue','sorcerer',
                   'warlock','wizard']
        classes = random.choice(classes)
        classes = classes.title()
        return classes
def sex():
        s = ['Male', 'Female']
        s = random.choice(s)
        return s
def alignmentPicker():
        align = ['LG','NG','CG','LN','N','CN','LE','NE','CE']
        align = random.choice(align)
        return align
def backgroundPicker():
        background = ['acolyte','charlatan','criminal','entertainer','folk hero','guild artisan','hermit','noble',
                      'outlander','sage','sailor','soldier','urchin']
        background = random.choice(background)
        background = background.title()
        return background
def armorPicker():
        x = ['No Armor', 'Light Armor', 'Heavy Armor']
        x = random.choice(x)
        return x
def bountyReason():
    c = ['Rescue a Captive', 'Clear a ruin']

def weaponRestrictions():
        wRes = ['None','No Spells','No Simple Melee Weapons','No Simple Ranged Weapons','No Martial Melee Weapons',
                'No Martial Ranged Weapons','No Healing Spells','No Cantrips','No Melee Weapons','No Ranged Weapons']
        wRes = random.choice(wRes)
        return wRes
def targetPicker():
        c = cC.climatePicker()
        t = c['Terrain']
        tod = c['TimeofDay']
        s = c['Season']
        temp = c['Temperature']
        temp = str(temp)
        temp = (temp+' Degrees')
        w = c['Weather']
        d = c['Disadvantage']
        Obj = bO.Objectives()
        pT, tK, wU, g = Obj
        target = dict(Race=racePicker(),Sex=sex(),Class=classPicker(),Background=backgroundPicker(),
                      Armor=armorPicker(),Weapon=weaponRestrictions(),Terrain=t, Season=s, Temperature=temp,
                      Weather=w, TimeofDay=tod, WeatherDisadvantage=d, Proof=pT, TypeofKill=tK, WeaponUsed=wU, GuardKill=g)
        target
        return target