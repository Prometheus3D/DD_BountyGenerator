import bountyUtils.bountyTargetDetails as tD
import bountyCalculator as bC

def playerVar():
    GM = input('How many Players: ')
    aml = input('Average Player Level: ')
    dif = input('Difficulty Level: ')
    bC.xpCal.globVar(GM,aml,dif)
    bC.xpCal.gmXP()
    bC.rewardData.tarlevelData()
    bC.rewardData.proofGold()
    bC.rewardData.guardGold()
    bC.rewardData.tarArmorData()
    bC.rewardData.weaponUsedXP()
    bC.rewardData.killTypeData()
    bC.xpCal.acCalc()
# t = tD.targetPicker()
# for key in t.keys():
#     value = t[key]
#     print(key, ':', value)


playerVar()