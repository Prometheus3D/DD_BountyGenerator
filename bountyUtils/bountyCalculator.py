import bountyTargetDetails as bTD
import math
# import bountyGenerator_main as bGmain
c = bTD.targetPicker()

class xpCal():
    def globVar(GM, aml, dif):
        globals()['gm'] = GM
        globals()['aml'] = aml
        globals()['dif'] = dif
    def gmXP():
        global gm
        gm = int(gm)
        xp = gm*2
        return xp
    def tarLevelTotal():
        global dif, aml
        aml = int(aml)
        dif = int(dif)
        t = (aml+dif)/2
        tarTotal = round(t)
        return tarTotal
    def acCalc():
        global acR
        acR = int(acR)
        r = acR*25
        return r

class rewardData():
    def diflevelData():
        global dif
        dif = int(dif)
        lvlData = {1:{'xp': 50, 'Gold':10}, 2:{'xp': 50,'Gold': 25}, 3:{'xp':150, 'Gold':50},
                 4:{'xp':300, 'Gold':75}, 5:{'xp':500, 'Gold': 100}, 6:{'xp': 750, 'Gold': 125},
                 7:{'xp': 1050, 'Gold': 150}, 8:{'xp':1400, 'Gold':175}, 9:{'xp': 1800,'Gold':200},
                 10:{'xp':2250, 'Gold':225}, 11:{'xp':2750,'Gold':250},12:{'xp':3300,'Gold':275},
                 13:{'xp':3900,'Gold':300},14:{'xp':4550,'Gold':325},15:{'xp':5250,'Gold':350},
                 16:{'xp':6000,'Gold':375},17:{'xp':6800, 'Gold':400},18:{'xp':7650,'Gold':425},
                 19:{'xp':8550,'Gold':450},20:{'xp':9500,'Gold':475},21:{'xp':10500,'Gold':500}}
        x = lvlData[dif]['xp']
        return x
    def tarlevelData():
        tarTotal = xpCal.tarLevelTotal()
        tarTot = int(tarTotal)
        if tarTot > 20:
            tarTot = 20
        tarData = {1:{'xp': 25, 'Gold':100}, 2:{'xp': 100,'Gold': 200}, 3:{'xp':225, 'Gold':300},
                 4:{'xp':400, 'Gold':400}, 5:{'xp':625, 'Gold': 500}, 6:{'xp': 900, 'Gold': 600},
                 7:{'xp': 1225, 'Gold': 700}, 8:{'xp':1600, 'Gold':800}, 9:{'xp': 2025,'Gold':900},
                 10:{'xp':2500, 'Gold':1000}, 11:{'xp':3025,'Gold':1100},12:{'xp':3600,'Gold':1200},
                 13:{'xp':4225,'Gold':1300},14:{'xp':4900,'Gold':1400},15:{'xp':5625,'Gold':1500},
                 16:{'xp':6400,'Gold':1600},17:{'xp':7225, 'Gold':1700},18:{'xp':8100,'Gold':1800},
                 19:{'xp':9025,'Gold':1900},20:{'xp':10000,'Gold':2000}}
        x = tarData[tarTot]['xp']
        return x
    def tarArmorData():
        tarm = c['Armor']
        arm = {'No Armor':{'xp':0, 'AC':2}, 'Light Armor':{'xp':11, 'AC':12}, 'Heavy Armor':{'xp':16, 'AC': 16}}
        xR = arm[tarm]['xp']
        acR = arm[tarm]['AC']
        globals()['acR'] = acR
        globals()['xR'] = xR
        return xR, acR
    def proofGold():
        pT = c['Proof']
        p = {'Head':{'Gold':100}, 'Arm':{'Gold':50}, 'Leg':{'Gold':50}, 'Tooth':{'Gold':10}, 'Lock of Hair':{'Gold':10},
             'Ring':{'Gold':5},'Any':{'Gold':0}, 'Armor':{'Gold':75}}
        r = p[pT]['Gold']
        return r
    def guardGold():
        gK = c['GuardKill']
        g = {'Yes':{'xp':0},'No':{'xp':500}}
        r = g[gK]['xp']
        return r
    def weaponUsedXP():
        wU = c['WeaponUsed']
        if wU == 'Any':
            xp = 0
        else:
            xp = 100
        return xp
    def killTypeData():
        tK = c['TypeofKill']
        tK = tK.lower()
        t = {'look like an accident':{'Gold':25,'xp':25}, 'brutal public murder':{'Gold':50,'xp':50},
             'silent assassination':{'Gold':150,'xp':150}, 'sabotage':{'Gold':100,'xp':100}}
        rG = t[tK]['Gold']
        rX = t[tK]['xp']
        return rG,rX
