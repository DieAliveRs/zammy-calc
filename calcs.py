import math

import constants as c
from settings import variables

### Armor stuff ###
def getTier(gear):
    if gear == "Cryptbloom" or gear == "Achto (mage)" or gear == "Achto (non mage)" or gear == "Deathwarden" or gear == "T90":
        tier = 90
    elif gear == "Sub. Ports":
        tier = 85
    elif gear == "Ganodermic":
        tier = 70
    
    elif gear == "Spirit":
        tier = 75
    elif gear == "T90 defender":
        tier = 45
    elif gear == "None" or gear == "Other/Dps" or gear == "Deathtouch bracelet":
        tier = 0
    
    return tier

def getBaseArmor(tier):
    return tier**3/500 + (10 * tier) + 100 if tier > 0 else 0

#armorDR
def armorReduction(helm, top, bottom, gloves, boots, shield, fortCheck, defLvl):
    gear = [helm, top, bottom, gloves, boots]
    
    reduction = 0
    for piece in gear:
        reduction += getTier(piece) * 0.0002    
    reduction += getTier(shield) * 0.001
    
    #Def lvl = 99
    reduction += defLvl/1000
    
    if fortCheck:
        reduction += 0.03
    
    return 1 - reduction

#adCalc
def animateDead(helm, top, bottom, gloves, boots, shield, ovl, aura, defLvl=99):
    helmArmor = getBaseArmor(getTier(helm)) * 0.2
    topArmor = getBaseArmor(getTier(top)) * 0.23
    bottomArmor = getBaseArmor(getTier(bottom)) * 0.22
    glovesArmor = getBaseArmor(getTier(gloves)) * 0.05
    bootsArmor = getBaseArmor(getTier(boots)) * 0.05
    shieldArmor = getBaseArmor(getTier(shield)) * 0.2
    
    gearArmor = [helmArmor, topArmor, bottomArmor, glovesArmor, bootsArmor, shieldArmor]
    
    
    if aura == "Zerk aura":
        defLvl = math.floor(defLvl * 0.85)
    if ovl == "Elder overload":
        defLvl += 21
    
    sumRed = 0
    sumDefRed = 0
    for pieceArmor in gearArmor:
        pieceRed = pieceArmor * 0.1
        sumRed += pieceRed
        
        defReduction = math.floor(defLvl / 4 if pieceRed > 0 else 0)
        sumDefRed += defReduction
    
    return math.floor(sumRed) + sumDefRed

#crypt
def cryptMod(helm, top, bottom, gloves, boots):
    gear = [helm, top, bottom, gloves, boots]
    
    pieceCont = 0
    for piece in gear:
        if piece == "Cryptbloom":
            pieceCont += 1
    
    if pieceCont == 2:
        meleeMod = 0.08
        magicMod = 0.12
    elif pieceCont > 2:
        meleeMod = 0.12
        magicMod = 0.18
    else:
        meleeMod = 0
        magicMod = 0
    
    return 1 - meleeMod, 1 - magicMod


### Disintegrate ###
def disintegrateMod(defValue, disintegrate=0, flames=0, base=0):
    return (math.floor(defValue * (disintegrate * 0.07 + flames * 0.01 + base/100)) + (100 - defValue))/100

### Aura ###
def auraCheck(aura):
    if aura == "Zerk aura":
        return True, False
    elif aura == "Aegis":
        return False, True
    else:
        return False, False

### Spirit ###
def spiritShieldCheck(shield):
    if shield == "Spirit":
        return True
    else:
        return False

### Prayers ###
#protects
def protects(check, eofCheck, enrage):
    if eofCheck:
        eof = 0.1
    else:
        eof = 0
    
    if check == "autos":
        return 1 - (0.6 + eof)
    elif check == "twinshot":
        return 1 - (0.5 + eof)
    elif check == "slam":
        return 1 - (0.5 + eof)
    elif check == "cage":
        if enrage < 500:
            return 1 - (0.5 + eof)
        elif enrage < 800:
            return 1 - (0.4 + eof)
        elif enrage < 1100:
            return 1 - (0.35 + eof)
        else:
            return 1 - (0.3 + eof)

#curses
def curse(drain):
    return 1 - drain/100
        

### Damage modifiers ###
def dmgMod(check, base, mod, stacks=0):
    if check:
        return math.floor(base * mod)
    else:
        return math.floor(base * (1 - stacks * mod))

def dmgMod2(check, base, mod):
    if check:
        return base - math.floor(base * mod)
    else:
        return base

def spiritMod(check, base, mod, pp, powderCheck):
    if check:
        if powderCheck:
            ppRestoration = math.ceil(min(0.025 * base, 990-pp, 100))
        else:
            ppRestoration = 0
        reductionCap = (pp + ppRestoration) * 10
        return base - min(math.floor(base * mod), reductionCap)
    else:
        return base

def deathwardMod(check, base, currentHp, maxHp):
    if check:
        Current = currentHp
        Half = math.floor(maxHp/2)
        Quarter = math.floor(maxHp/4)
        
        #Upper half portion
        if Current < Half:
            U = 0
        else:
            U = min(Current-Half, base)
        
        #Quarter-half portion
        if Current < Quarter:
            Qh = 0
        else:
            Qh = math.ceil(min(min(Current, Half)-Quarter, min(base, max(0, base-(Current-Half))))*0.95)
        
        #Lower quarter portion
        Ql = max(0, math.ceil(base-max(0, Current-Quarter))*0.9)
        
        return math.floor(U + Qh + Ql)
    else:
        return base


def adMod(check, base, mod):
    if check:
        if base*0.6 > mod:
            return base - mod
        else:
            return math.floor(base * 0.4)
    else:
        return base

def damageCalculation(base, pulvCheck, cadeCheck, debilCheck, zerkAuraCheck, severCheck, enfeebleCheck, anchorCheck, aegisCheck,
                      sdCheck, disruptCheck, pad3Check, pad5Check, prayerCheck, anticipCheck, reflectCheck, darknessCheck,
                      resCheck, immortCheck, zerkUltCheck, fulBookCheck, armorCheck, spiritCheck, cryptCheck, deathwardCheck,
                      hhCheck, adCheck,
                      curseDR, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, prayerDR, reflectDR, resDR,
                      armorDR, cryptDR, adDR,
                      pp, powderCheck, currentHp, maxHp):
    
    curse = dmgMod(True, base, curseDR)### curseDR = 1 - curseStacks/100
    pulv = dmgMod(pulvCheck, curse, 0.75)
    cade = dmgMod(cadeCheck, pulv, cadeDR)
    debil = dmgMod(debilCheck, cade, debilDR)
    zerkAura = dmgMod(zerkAuraCheck, debil, 1.15)
    sever = dmgMod(severCheck, zerkAura, 0.9)
    enfeeble = dmgMod(enfeebleCheck, sever, 0.9)
    anchor = dmgMod(anchorCheck, enfeeble, 0.9)
    absorb = dmgMod(False, anchor, 0.05, absorbStacks)
    aegis = dmgMod2(aegisCheck, absorb, 0.1)
    sd = dmgMod(sdCheck, aegis, sdDR)
    emerald = dmgMod(False, sd, 0.01, emeraldStacks)
    disrupt = dmgMod(disruptCheck, emerald, disruptDR)
    pad3 = dmgMod(pad3Check, disrupt, 1.05)
    pad5 = dmgMod(pad5Check, pad3, 0.95)
    prayer = dmgMod(prayerCheck, pad5, prayerDR)
    anticip = dmgMod(anticipCheck, prayer, 0.9)
    reflect = dmgMod(reflectCheck, anticip, reflectDR)
    darkness = dmgMod(darknessCheck, reflect, 0.75)
    res = dmgMod(resCheck, darkness, resDR)
    immort = dmgMod(immortCheck, res, 0.75)
    zerkUlt = dmgMod(zerkUltCheck, immort, 1.5)
    fulBook = dmgMod(fulBookCheck, zerkUlt, 1.1)
    armor = dmgMod(armorCheck, fulBook, armorDR)
    spirit = spiritMod(spiritCheck, armor, 0.3, pp, powderCheck)
    crypt = dmgMod(cryptCheck, spirit, cryptDR)
    deathward = deathwardMod(deathwardCheck, crypt, currentHp, maxHp)
    hh = dmgMod(hhCheck, deathward, 0.8)
    ad = adMod(adCheck, hh, adDR)
    
    Final = ad
    
    return Final


#healing/divert stuff
def healingCalculation(base, pulvCheck, cadeCheck, debilCheck, zerkAuraCheck, severCheck, enfeebleCheck, anchorCheck, aegisCheck,
                      sdCheck, disruptCheck, pad3Check, pad5Check, prayerCheck, anticipCheck, reflectCheck, darknessCheck,
                      resCheck,
                      curseDR, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, prayerDR, reflectDR, resDR):
    curse = dmgMod(True, base, curseDR)
    pulv = dmgMod(pulvCheck, curse, 0.75)
    cade = dmgMod(cadeCheck, pulv, cadeDR)
    debil = dmgMod(debilCheck, cade, debilDR)
    zerkAura = dmgMod(zerkAuraCheck, debil, 1.15)
    sever = dmgMod(severCheck, zerkAura, 0.9)
    enfeeble = dmgMod(enfeebleCheck, sever, 0.9)
    anchor = dmgMod(anchorCheck, enfeeble, 0.9)
    absorb = dmgMod(False, anchor, 0.05, absorbStacks)
    aegis = dmgMod2(aegisCheck, absorb, 0.1)
    sd = dmgMod(sdCheck, aegis, sdDR)
    emerald = dmgMod(False, sd, 0.01, emeraldStacks)
    disrupt = dmgMod(disruptCheck, emerald, disruptDR)
    pad3 = dmgMod(pad3Check, disrupt, 1.05)
    pad5 = dmgMod(pad5Check, pad3, 0.95)
    prayer = dmgMod(prayerCheck, pad5, prayerDR)
    anticip = dmgMod(anticipCheck, prayer, 0.9)
    reflect = dmgMod(reflectCheck, anticip, reflectDR)
    darkness = dmgMod(darknessCheck, reflect, 0.75)
    res = dmgMod(resCheck, darkness, resDR)

    if variables["shield"] == "None":
        shieldTier = variables["boneshield"]
    else:
        shieldTier = getTier(variables["shield"])
    blocked = darkness - res
    healingPercentage = math.floor(50 + shieldTier * 0.5)/100
    healing = blocked * healingPercentage

    return healing

def divertCalculation(base, pulvCheck, cadeCheck, debilCheck, zerkAuraCheck, severCheck, enfeebleCheck, anchorCheck, aegisCheck,
                      sdCheck, disruptCheck, pad3Check, pad5Check, prayerCheck, anticipCheck, reflectCheck, darknessCheck,
                      resCheck,
                      curseDR, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, prayerDR, reflectDR, resDR):
    curse = dmgMod(True, base, curseDR)
    pulv = dmgMod(pulvCheck, curse, 0.75)
    cade = dmgMod(cadeCheck, pulv, cadeDR)
    debil = dmgMod(debilCheck, cade, debilDR)
    zerkAura = dmgMod(zerkAuraCheck, debil, 1.15)
    sever = dmgMod(severCheck, zerkAura, 0.9)
    enfeeble = dmgMod(enfeebleCheck, sever, 0.9)
    anchor = dmgMod(anchorCheck, enfeeble, 0.9)
    absorb = dmgMod(False, anchor, 0.05, absorbStacks)
    aegis = dmgMod2(aegisCheck, absorb, 0.1)
    sd = dmgMod(sdCheck, aegis, sdDR)
    emerald = dmgMod(False, sd, 0.01, emeraldStacks)
    disrupt = dmgMod(disruptCheck, emerald, disruptDR)
    pad3 = dmgMod(pad3Check, disrupt, 1.05)
    pad5 = dmgMod(pad5Check, pad3, 0.95)
    prayer = dmgMod(prayerCheck, pad5, prayerDR)
    anticip = dmgMod(anticipCheck, prayer, 0.9)
    reflect = dmgMod(reflectCheck, anticip, reflectDR)
    darkness = dmgMod(darknessCheck, reflect, 0.75)
    res = dmgMod(resCheck, darkness, resDR)

    if variables["shield"] == "None":
        shieldTier = variables["boneshield"]
    else:
        shieldTier = getTier(variables["shield"])
    
    blocked = darkness - res
    adrenGain = 0

    if blocked > 12000:
        blocked = 12000

    if blocked > 9000:
        adrenGain += 0.1 * ((blocked - 9000) // (200 - shieldTier))
        blocked = 9000
    
    if blocked > 6000:
        adrenGain += 0.4 * ((blocked - 6000) // (200 - shieldTier))
        blocked = 6000

    if blocked > 3000:
        adrenGain += 0.6 * ((blocked - 3000) // (200 - shieldTier))
        blocked = 3000

    if blocked > 0:
        adrenGain += 0.8 * (blocked // (200 - shieldTier))

    return round(adrenGain, 1)

#refl stuff
def reflectCalculation(base, pulvCheck, cadeCheck, debilCheck, zerkAuraCheck, severCheck, enfeebleCheck, anchorCheck, aegisCheck,
                      sdCheck, disruptCheck, pad3Check, pad5Check, prayerCheck, anticipCheck, reflectCheck, darknessCheck,
                      resCheck, immortCheck, zerkUltCheck, fulBookCheck, armorCheck, spiritCheck, cryptCheck, deathwardCheck,
                      hhCheck, adCheck,
                      curseDR, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, prayerDR, reflectDR, resDR,
                      armorDR, cryptDR, adDR,
                      pp, powderCheck, currentHp, maxHp,
                      vulnCheck, croeCheck, pad6Stacks, vengCheck, dtbCheck):
    curse = dmgMod(True, base, curseDR)
    pulv = dmgMod(pulvCheck, curse, 0.75)
    cade = dmgMod(cadeCheck, pulv, cadeDR)
    debil = dmgMod(debilCheck, cade, debilDR)
    zerkAura = dmgMod(zerkAuraCheck, debil, 1.15)
    sever = dmgMod(severCheck, zerkAura, 0.9)
    enfeeble = dmgMod(enfeebleCheck, sever, 0.9)
    anchor = dmgMod(anchorCheck, enfeeble, 0.9)
    absorb = dmgMod(False, anchor, 0.05, absorbStacks)
    aegis = dmgMod2(aegisCheck, absorb, 0.1)
    sd = dmgMod(sdCheck, aegis, sdDR)
    emerald = dmgMod(False, sd, 0.01, emeraldStacks)
    disrupt = dmgMod(disruptCheck, emerald, disruptDR)
    pad3 = dmgMod(pad3Check, disrupt, 1.05)
    pad5 = dmgMod(pad5Check, pad3, 0.95)
    prayer = dmgMod(prayerCheck, pad5, prayerDR)
    anticip = dmgMod(anticipCheck, prayer, 0.9)
    reflect = dmgMod(reflectCheck, anticip, reflectDR)
    darkness = dmgMod(darknessCheck, reflect, 0.75)
    res = dmgMod(resCheck, darkness, resDR)
    immort = dmgMod(immortCheck, res, 0.75)
    zerkUlt = dmgMod(zerkUltCheck, immort, 1.5)
    fulBook = dmgMod(fulBookCheck, zerkUlt, 1.1)
    armor = dmgMod(armorCheck, fulBook, armorDR)
    spirit = spiritMod(spiritCheck, armor, 0.3, pp, powderCheck)
    crypt = dmgMod(cryptCheck, spirit, cryptDR)
    deathward = deathwardMod(deathwardCheck, crypt, currentHp, maxHp)
    hh = dmgMod(hhCheck, deathward, 0.8)
    ad = adMod(adCheck, hh, adDR)

    #Reflect
    if reflectCheck:
        reflectDmg = dmgMod2(reflectCheck, anticip, 1-reflectDR)
        vulnRefl = dmgMod(vulnCheck, reflectDmg, 1.1)
        croeRefl = dmgMod(croeCheck, vulnRefl, 1.1)
        pad3Refl = dmgMod(pad3Check, croeRefl, 1.05)
        pad5Refl = dmgMod(pad5Check, pad3Refl, 0.95)
        pad6Refl = dmgMod(True, pad5Refl, pad6Stacks)
    else:
        pad6Refl = 0

    #Deflect
    if prayerCheck and variables["defl_check"]:
        defelctDmg = dmgMod(prayerCheck, pad5, 0.1)
        vulnDefl = dmgMod(vulnCheck, defelctDmg, 1.1)
        croeDefl = dmgMod(croeCheck, vulnDefl, 1.1)
        pad3Defl = dmgMod(pad3Check, croeDefl, 1.05)
        pad5Defl = dmgMod(pad5Check, pad3Defl, 0.95)
        pad6Defl = dmgMod(True, pad5Defl, pad6Stacks)
    else:
        pad6Defl = 0

    #Darkness
    if darknessCheck:
        darknessDmg = dmgMod(darknessCheck, darkness, 0.25)
        vulnDark = dmgMod(vulnCheck, darknessDmg, 1.1)
        croeDark = dmgMod(croeCheck, vulnDark, 1.1)
        pad3Dark = dmgMod(pad3Check, croeDark, 1.05)
        pad5Dark = dmgMod(pad5Check, pad3Dark, 0.95)
        pad6Dark = dmgMod(True, pad5Dark, pad6Stacks)
    else:
        pad6Dark = 0

    #Vengeance
    if vengCheck:
        vengDmg = dmgMod(vengCheck, ad, 0.75)
        vulnVeng = dmgMod(vulnCheck, vengDmg, 1.1)
        croeVeng = dmgMod(croeCheck, vulnVeng, 1.1)
        pad3Veng = dmgMod(pad3Check, croeVeng, 1.05)
        pad5Veng = dmgMod(pad5Check, pad3Veng, 0.95)
        pad6Veng = dmgMod(True, pad5Veng, pad6Stacks)
    else:
        pad6Veng = 0

    #Dtb
    #Dtb min
    if dtbCheck and variables["dtb_check"]:
        dtbMinDmg = dmgMod(dtbCheck, immort, 0.25)
        vulnDtbMin = dmgMod(vulnCheck, dtbMinDmg, 1.1)
        croeDtbMin = dmgMod(croeCheck, vulnDtbMin, 1.1)
        pad3DtbMin = dmgMod(pad3Check, croeDtbMin, 1.05)
        pad5DtbMin = dmgMod(pad5Check, pad3DtbMin, 0.95)
        pad6DtbMin = dmgMod(True, pad5DtbMin, pad6Stacks)
        #Dtb max
        dtbMaxDmg = dmgMod(dtbCheck, immort, 0.25)
        vulnDtbMax = dmgMod(vulnCheck, dtbMaxDmg, 1.1)
        croeDtbMax = dmgMod(croeCheck, vulnDtbMax, 1.1)
        pad3DtbMax = dmgMod(pad3Check, croeDtbMax, 1.05)
        pad5DtbMax = dmgMod(pad5Check, pad3DtbMax, 0.95)
        pad6DtbMax = dmgMod(True, pad5DtbMax, pad6Stacks)
        #Dtb avg
        dtbAvg = math.floor((pad6DtbMin + pad6DtbMax)/2)
    else:
        dtbAvg = 0

    reflFinal = pad6Refl
    deflFinal = pad6Defl
    darkFinal = pad6Dark
    vengFinal = pad6Veng
    dtbFinal = dtbAvg

    return reflFinal, deflFinal, darkFinal, vengFinal, dtbFinal


### Enrage scaling stuff/mechanics ##
def autos(enrage, twinshot, greyCheck, aggroCheck, questCheck):
    #global var
    dmg = c.autos_base
    scaling = c.autos_scaling
    
    maxDmg = dmg + scaling * enrage
    minDmg = maxDmg * 0.7
    
    
    if not greyCheck:
        maxDmg = math.floor(maxDmg/1.5)
        minDmg = math.floor(minDmg/1.5)
    
    if not aggroCheck:
        maxDmg = math.floor(maxDmg * 0.75)
        minDmg = math.floor(minDmg * 0.75)
    
    if questCheck:
        maxDmg = math.floor(maxDmg * 0.9)
        minDmg = math.floor(minDmg * 0.9)
    
    TS = math.floor((maxDmg * twinshot)/10)
    
    return maxDmg, minDmg, TS


def infernus(choke, puzzleboxCheck):
    #global var
    dmg = c.infernus_base
    scaling = c.infernus_scaling
    
    base = dmg + scaling * choke
    
    if puzzleboxCheck:
        base = math.floor(base * 0.35)
    
    return base


def smoke(enrage, stacks, infernusCheck):
    dmg = c.smoke_base
    scaling = c.smoke_scaling
    
    
    base = (dmg + scaling * enrage) * stacks
    
    
    if infernusCheck:
        return base * 1.5, stacks * 3
    else:
        return base, stacks


def slam(enrage, distance):
    #global var
    dmg = c.slam_base
    enrage_scaling = c.slam_enrage_scaling
    distance_scaling = c.slam_distance_scaling
    
    base = min(dmg + enrage_scaling * enrage, 35000)
    
    final = math.floor(base * (1 - distance_scaling * distance))
    
    return final, math.floor(final/2)


def decimation(enrage, stun):
    #global var
    dmg = c.decimation_base
    enrage_scaling = c.decimation_enrage_scaling
    tick_scaling = c.decimation_tick_scaling
    
    base = dmg + enrage_scaling * enrage
    
    final = base * tick_scaling * stun
    
    return final


def cage(enrage, team_size, questCheck):
    #global var
    dmg = c.cage_base
    scaling = c.cage_scaling
    
    base = min(math.floor(dmg + scaling * enrage) * team_size, 32500)
    
    if questCheck:
        base = math.floor(base * 0.9)
    
    return base


### P7 ###
def redBar(charge_start, charge_rate, iteration):
    charge = charge_start
    red_bar = 0
    for i in range(iteration):
        charge += charge_rate
        red_bar += math.floor(charge)
    return min(red_bar, 100000)

def smallBombs(red_bar, iteration):
    return math.floor((red_bar/100)*iteration)

def iterationCalc(charge_start, charge_rate, charge):
    newCharge = charge_start
    iteration = 0
    while newCharge < charge:
        newCharge += charge_rate
        iteration += 1
    return min(iteration, 500)

def p7(mode, enrage):
    if mode == "Iteration":
        iteration = min(variables["iteration_input"], 500)
        
        charge_start = min(250 + (enrage/5 - 20), 2000)
        charge_rate = charge_start/100
        # charge_cap = charge_start + charge_rate * 500
        
        red_bar = redBar(charge_start, charge_rate, iteration)
        small_bombs = smallBombs(red_bar, iteration)
        
    if mode == "Charge value":
        charge_value = variables["charge_input"]
        
        charge_start = min(250 + (enrage/5 - 20), 2000)
        charge_rate = charge_start/100
        
        iteration = iterationCalc(charge_start, charge_rate, charge_value)
        
        red_bar = redBar(charge_start, charge_rate, iteration)
        small_bombs = smallBombs(red_bar, iteration)
        
    if mode == "Red bar":
        red_bar = variables["red_input"]
        small_bombs = 0
    
    return red_bar, small_bombs

def chargeCalcs():
    if variables["enrage"] < 100:
        return 0, 0
    charge_start = min(250 + (variables["enrage"]/5 - 20), 2000)
    charge_rate = charge_start/100
    charge_cap = charge_start + charge_rate * 500

    return int(charge_start), int(charge_cap)

### Hp scaling stuff ###
def phaseHp(enrage, teamSize):
    
    totalHp = math.floor(teamSize * (min(300000 + (7500 * enrage)/10, 1600000)))
    p1Hp = int(totalHp)
    p2Hp = int(totalHp * 0.84)
    p3Hp = int(totalHp * 0.68)
    p4Hp = int(totalHp * 0.52)
    p5Hp = int(totalHp * 0.36)
    p6Hp = int(totalHp * 0.2)

    if enrage >= 100:
        p7Hp = int(math.floor(1000 * teamSize * (100 + (max(min(enrage, 1000), 100)-100)/6)))
    
    else:
        p7Hp = 0

    grey = int(math.floor(teamSize * (75000 + min(enrage, 750) * 100)))
    witch = int(math.floor(33000 + (enrage * 13.2)))
    demon = int(min(math.floor(15000 + enrage * 37.5), 70000))
    if teamSize == 1:
        rune = int(math.floor(25000 + (max(min(enrage, 3500), 1000) * 10))/2)
    else:
        rune = int(math.floor(25000 + (max(min(enrage, 3500), 1000) * 10)))

    return p1Hp, p2Hp, p3Hp, p4Hp, p5Hp, p6Hp, p7Hp, grey, witch, demon, rune

### Pad effects ##
def pad1eff(adren, stacks):
    gain = adren + 0.2 * adren * stacks
    dmg = int(stacks*10)
    return gain, dmg

def pad2eff(stacks, maxHp, fortCheck):
    cdr = stacks * 8
    thresh = math.floor(99 * 100 * 0.05 * stacks)
    if fortCheck:
        effHp = maxHp - thresh + 1000
    else:
        effHp = maxHp - thresh
    return int(cdr), int(thresh), int(effHp)

def pad4eff(dr, disint, spec, smoke=0, infernus=False):
    if spec == "P7 Bomb":
        b = 50
        smoke = 0
    elif spec == "Decimation":
        b = 40
        smoke = 0
    elif spec == "Smoke":
        b = 0
        if infernus:
            smoke = smoke * 3
    else:
        b = 0
        smoke = 0
    effectiveness = int(100 - disintegrateMod(dr, disintegrate=disint, flames=smoke, base=b) * 100)
    return effectiveness

def pad6eff(stacks, maxHp, currentHp):
    hpNeeded = int(math.floor(maxHp * 0.6))
    if currentHp/maxHp < 0.6:
        dmgBonus = int(stacks * 6)
    else: dmgBonus = 0
    healingReduction = int(stacks * 10)
    return hpNeeded, dmgBonus, healingReduction


#Main
#mage autos: calculate dmg from autos() based on enrage
# -> define mage autos settings (curses, prayer, disintegrate, armor)
# -> give inputs to damageCalculations()
# -> return dmg calculation, show output



def calcMageAutos():
    maxDmg, minDmg, ts = autos(variables["enrage"], variables["pad1"], variables["grey"], variables["aggro"], variables["totg"])
    curseDR = curse(variables["affliction"])
    
    cadeDR = disintegrateMod(100, variables["pad4"])
    debilDR = disintegrateMod(50, variables["pad4"])
    sdDR = disintegrateMod(variables["sd"], variables["pad4"])
    disruptDR = cadeDR
    reflectDR = debilDR
    resDR = cadeDR
    
    emeraldStacks = variables["emerald"]
    absorbStacks = variables["absorb"]
    
    autosDR = protects("autos", variables["eof"], variables["enrage"])
    twinshotDR = protects("twinshot", variables["eof"], variables["enrage"])
    armorDR = armorReduction(variables["helm"], variables["top"], variables["bottoms"], variables["gloves"], variables["boots"], variables["shield"], variables["fort"], variables["def"])
    cryptMelee, cryptMagic = cryptMod(variables["helm"], variables["top"], variables["bottoms"], variables["gloves"], variables["boots"])
    adDR = animateDead(variables["helm"], variables["top"], variables["bottoms"], variables["gloves"], variables["boots"], variables["shield"], variables["ovl"], variables["aura"], variables["def"])
    zerkAuraCheck, aegisCheck = auraCheck(variables["aura"])
    spiritCheck = spiritShieldCheck(variables["shield"])
    
    maxFinal = damageCalculation(maxDmg, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], variables["deflect"],
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"], variables["immort"], variables["zerk"],
                              variables["ful"], True, spiritCheck, True, variables["dw"], variables["hh"], variables["ad"],
                              curseDR, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, autosDR, reflectDR,
                              resDR, armorDR, cryptMagic, adDR, variables["ppoints"], variables["powder"], variables["currenthp"], variables["maxhp"])
    
    minFinal = damageCalculation(minDmg, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], variables["deflect"],
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"], variables["immort"], variables["zerk"],
                              variables["ful"], True, spiritCheck, True, variables["dw"], variables["hh"], variables["ad"],
                              curseDR, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, autosDR, reflectDR,
                              resDR, armorDR, cryptMagic, adDR, variables["ppoints"], variables["powder"], variables["currenthp"], variables["maxhp"])
    
    avgFinal = damageCalculation((maxDmg + minDmg)/2, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], variables["deflect"],
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"], variables["immort"], variables["zerk"],
                              variables["ful"], True, spiritCheck, True, variables["dw"], variables["hh"], variables["ad"],
                              curseDR, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, autosDR, reflectDR,
                              resDR, armorDR, cryptMagic, adDR, variables["ppoints"], variables["powder"], variables["currenthp"], variables["maxhp"])
    
    tsFinal = damageCalculation(ts, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], variables["deflect"],
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"], variables["immort"], variables["zerk"],
                              variables["ful"], True, spiritCheck, True, variables["dw"], variables["hh"], variables["ad"],
                              curseDR, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, twinshotDR, reflectDR,
                              resDR, armorDR, cryptMagic, adDR, variables["ppoints"], variables["powder"], variables["currenthp"], variables["maxhp"])
    
    return int(maxFinal), int(minFinal), int(avgFinal), int(tsFinal)

def calcRangeAutos():
    maxDmg, minDmg, ts = autos(variables["enrage"], variables["pad1"], variables["grey"], variables["aggro"], variables["totg"])
    curseDR = curse(variables["desolation"])
    
    cadeDR = disintegrateMod(100, variables["pad4"])
    debilDR = disintegrateMod(50, variables["pad4"])
    sdDR = disintegrateMod(variables["sd"], variables["pad4"])
    disruptDR = cadeDR
    reflectDR = debilDR
    resDR = cadeDR
    
    emeraldStacks = variables["emerald"]
    absorbStacks = variables["absorb"]
    
    autosDR = protects("autos", variables["eof"], variables["enrage"])
    twinshotDR = protects("twinshot", variables["eof"], variables["enrage"])
    armorDR = armorReduction(variables["helm"], variables["top"], variables["bottoms"], variables["gloves"], variables["boots"], variables["shield"], variables["fort"], variables["def"])

    adDR = animateDead(variables["helm"], variables["top"], variables["bottoms"], variables["gloves"], variables["boots"], variables["shield"], variables["ovl"], variables["aura"], variables["def"])
    zerkAuraCheck, aegisCheck = auraCheck(variables["aura"])
    spiritCheck = spiritShieldCheck(variables["shield"])
    
    maxFinal = damageCalculation(maxDmg, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], variables["deflect"],
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"], variables["immort"], variables["zerk"],
                              variables["ful"], True, spiritCheck, False, variables["dw"], variables["hh"], variables["ad"],
                              curseDR, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, autosDR, reflectDR,
                              resDR, armorDR, 1, adDR, variables["ppoints"], variables["powder"], variables["currenthp"], variables["maxhp"])
    
    minFinal = damageCalculation(minDmg, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], variables["deflect"],
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"], variables["immort"], variables["zerk"],
                              variables["ful"], True, spiritCheck, False, variables["dw"], variables["hh"], variables["ad"],
                              curseDR, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, autosDR, reflectDR,
                              resDR, armorDR, 1, adDR, variables["ppoints"], variables["powder"], variables["currenthp"], variables["maxhp"])
    
    avgFinal = damageCalculation((maxDmg + minDmg)/2, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], variables["deflect"],
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"], variables["immort"], variables["zerk"],
                              variables["ful"], True, spiritCheck, False, variables["dw"], variables["hh"], variables["ad"],
                              curseDR, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, autosDR, reflectDR,
                              resDR, armorDR, 1, adDR, variables["ppoints"], variables["powder"], variables["currenthp"], variables["maxhp"])
    
    tsFinal = damageCalculation(ts, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], variables["deflect"],
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"], variables["immort"], variables["zerk"],
                              variables["ful"], True, spiritCheck, True, variables["dw"], variables["hh"], variables["ad"],
                              curseDR, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, twinshotDR, reflectDR,
                              resDR, armorDR, 1, adDR, variables["ppoints"], variables["powder"], variables["currenthp"], variables["maxhp"])
    
    return int(maxFinal), int(minFinal), int(avgFinal), int(tsFinal)
    
def calcSlam():
    base1, base2 = slam(variables["enrage"], variables["slam"])
    
    cadeDR = disintegrateMod(100, variables["pad4"])
    debilDR = disintegrateMod(50, variables["pad4"])
    sdDR = disintegrateMod(variables["sd"], variables["pad4"])
    disruptDR = cadeDR
    reflectDR = debilDR
    resDR = cadeDR
    
    emeraldStacks = variables["emerald"]
    absorbStacks = variables["absorb"]
    
    slamDR = protects("slam", variables["eof"], variables["enrage"])
    # twinshotDR = protects("twinshot", variables["eof"], variables["enrage"])
    armorDR = armorReduction(variables["helm"], variables["top"], variables["bottoms"], variables["gloves"], variables["boots"], variables["shield"], variables["fort"], variables["def"])
    cryptMelee, cryptMagic = cryptMod(variables["helm"], variables["top"], variables["bottoms"], variables["gloves"], variables["boots"])
    adDR = animateDead(variables["helm"], variables["top"], variables["bottoms"], variables["gloves"], variables["boots"], variables["shield"], variables["ovl"], variables["aura"], variables["def"])
    zerkAuraCheck, aegisCheck = auraCheck(variables["aura"])
    spiritCheck = spiritShieldCheck(variables["shield"])
    
    Final1 = damageCalculation(base1, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], variables["deflect"],
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"], variables["immort"], variables["zerk"],
                              variables["ful"], True, spiritCheck, True, variables["dw"], variables["hh"], variables["ad"],
                              1, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, slamDR, reflectDR,
                              resDR, armorDR, cryptMelee, adDR, variables["ppoints"], variables["powder"], variables["currenthp"], variables["maxhp"])
    
    Final2 = damageCalculation(base2, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], variables["deflect"],
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"], variables["immort"], variables["zerk"],
                              variables["ful"], True, spiritCheck, True, variables["dw"], variables["hh"], variables["ad"],
                              1, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, slamDR, reflectDR,
                              resDR, armorDR, cryptMelee, adDR, variables["ppoints"], variables["powder"], variables["currenthp"], variables["maxhp"])

    return Final1, Final2
    
def calcInfernus():
    minInfernus = infernus(variables["choke"], variables["puzzlebox"])

    maxInfernus = math.floor(minInfernus * 1.1)
    avgInfernus = math.floor((minInfernus + maxInfernus)/2)
    
    minHh = dmgMod(variables["hh"], minInfernus, 0.8)
    maxHh = dmgMod(variables["hh"], maxInfernus, 0.8)
    avgHh = dmgMod(variables["hh"], avgInfernus, 0.8)
    
    return minHh, maxHh, avgHh

def calcSmoke():
    smokeBase, flamesStacks = smoke(variables["enrage"], variables["smoke"], variables["infernus"])
    
    cadeDR = disintegrateMod(100, variables["pad4"], flamesStacks)
    debilDR = disintegrateMod(50, variables["pad4"], flamesStacks)
    sdDR = disintegrateMod(variables["sd"], variables["pad4"], flamesStacks)
    disruptDR = cadeDR
    reflectDR = debilDR
    resDR = cadeDR
    
    emeraldStacks = variables["emerald"]
    absorbStacks = variables["absorb"]
    
    armorDR = armorReduction(variables["helm"], variables["top"], variables["bottoms"], variables["gloves"], variables["boots"], variables["shield"], variables["fort"], variables["def"])
    zerkAuraCheck, aegisCheck = auraCheck(variables["aura"])
    spiritCheck = spiritShieldCheck(variables["shield"])
    
    Final = damageCalculation(smokeBase, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], False,
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"], variables["immort"], variables["zerk"],
                              variables["ful"], True, spiritCheck, False, variables["dw"], variables["hh"], False,
                              1, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, 0, reflectDR,
                              resDR, armorDR, 1, 0, variables["ppoints"], variables["powder"], variables["currenthp"], variables["maxhp"])
    
    return Final


def calcDecimation(releaseTick):
    decimationBase = decimation(variables["enrage"], releaseTick)
    
    cadeDR = disintegrateMod(100, variables["pad4"], 0, 40)
    debilDR = disintegrateMod(50, variables["pad4"], 0, 40)
    sdDR = disintegrateMod(variables["sd"], variables["pad4"], 0, 40)
    disruptDR = cadeDR
    reflectDR = debilDR
    resDR = cadeDR
    
    emeraldStacks = variables["emerald"]
    absorbStacks = variables["absorb"]
    
    armorDR = armorReduction(variables["helm"], variables["top"], variables["bottoms"], variables["gloves"], variables["boots"], variables["shield"], variables["fort"], variables["def"])
    zerkAuraCheck, aegisCheck = auraCheck(variables["aura"])
    spiritCheck = spiritShieldCheck(variables["shield"])
    
    Final = damageCalculation(decimationBase, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], False,
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"], variables["immort"], variables["zerk"],
                              variables["ful"], True, spiritCheck, False, variables["dw"], variables["hh"], False,
                              1, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, 0, reflectDR,
                              resDR, armorDR, 1, 0, variables["ppoints"], variables["powder"], variables["currenthp"], variables["maxhp"])
    
    return Final

def calcCage():
    base = cage(variables["enrage"], variables["teamsize"], variables["totg"])
    
    cadeDR = disintegrateMod(100, variables["pad4"])
    debilDR = disintegrateMod(50, variables["pad4"])
    sdDR = disintegrateMod(variables["sd"], variables["pad4"])
    disruptDR = cadeDR
    reflectDR = debilDR
    resDR = cadeDR
    
    emeraldStacks = variables["emerald"]
    absorbStacks = variables["absorb"]
    
    cageDR = protects("cage", variables["eof"], variables["enrage"])
    armorDR = armorReduction(variables["helm"], variables["top"], variables["bottoms"], variables["gloves"], variables["boots"], variables["shield"], variables["fort"], variables["def"])
    cryptMelee, cryptMagic = cryptMod(variables["helm"], variables["top"], variables["bottoms"], variables["gloves"], variables["boots"])
    adDR = animateDead(variables["helm"], variables["top"], variables["bottoms"], variables["gloves"], variables["boots"], variables["shield"], variables["ovl"], variables["aura"], variables["def"])
    zerkAuraCheck, aegisCheck = auraCheck(variables["aura"])
    spiritCheck = spiritShieldCheck(variables["shield"])
    
    Final = damageCalculation(base, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], variables["deflect"],
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"], variables["immort"], variables["zerk"],
                              variables["ful"], True, spiritCheck, True, variables["dw"], variables["hh"], variables["ad"],
                              1, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, cageDR, reflectDR,
                              resDR, armorDR, cryptMagic, adDR, variables["ppoints"], variables["powder"], variables["currenthp"], variables["maxhp"])
    
    return Final

def calcBigBomb():
    bigBomb, smallBomb = p7(variables["mode"], variables["enrage"])
    bigBombMax = bigBomb * 1.1
    bigBombAvg = bigBomb * 1.05

    cadeDR = disintegrateMod(100, variables["pad4"], 0, 50)
    debilDR = disintegrateMod(50, variables["pad4"], 0, 50)
    sdDR = disintegrateMod(variables["sd"], variables["pad4"], 0, 50)
    disruptDR = cadeDR
    reflectDR = debilDR
    resDR = cadeDR
    
    emeraldStacks = variables["emerald"]
    absorbStacks = variables["absorb"]
    
    zerkAuraCheck, aegisCheck = auraCheck(variables["aura"])
    spiritCheck = spiritShieldCheck(variables["shield"])
    
    bigMaxFinal = damageCalculation(bigBombMax, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], False,
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"], variables["immort"], variables["zerk"],
                              variables["ful"], True, spiritCheck, False, variables["dw"], variables["hh"], False,
                              1, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, 0, reflectDR,
                              resDR, 1, 1, 0, variables["ppoints"], variables["powder"], variables["currenthp"], variables["maxhp"])

    bigMinFinal = damageCalculation(bigBomb, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], False,
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"], variables["immort"], variables["zerk"],
                              variables["ful"], True, spiritCheck, False, variables["dw"], variables["hh"], False,
                              1, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, 0, reflectDR,
                              resDR, 1, 1, 0, variables["ppoints"], variables["powder"], variables["currenthp"], variables["maxhp"])
    
    bigAvgFinal = damageCalculation(bigBombAvg, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], False,
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"], variables["immort"], variables["zerk"],
                              variables["ful"], True, spiritCheck, False, variables["dw"], variables["hh"], False,
                              1, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, 0, reflectDR,
                              resDR, 1, 1, 0, variables["ppoints"], variables["powder"], variables["currenthp"], variables["maxhp"])

    return int(bigMaxFinal), int(bigMinFinal), int(bigAvgFinal)

def calcSmallBomb():
    bigBomb, smallBomb = p7(variables["mode"], variables["enrage"])
    smallTsBomb = math.floor((smallBomb * variables["pad1"])/10)

    cadeDR = disintegrateMod(100, variables["pad4"])
    debilDR = disintegrateMod(50, variables["pad4"])
    sdDR = disintegrateMod(variables["sd"], variables["pad4"])
    disruptDR = cadeDR
    reflectDR = debilDR
    resDR = cadeDR
    
    emeraldStacks = variables["emerald"]
    absorbStacks = variables["absorb"]
    
    armorDR = armorReduction(variables["helm"], variables["top"], variables["bottoms"], variables["gloves"], variables["boots"], variables["shield"], variables["fort"], variables["def"])
    zerkAuraCheck, aegisCheck = auraCheck(variables["aura"])
    spiritCheck = spiritShieldCheck(variables["shield"])

    smallFinal = damageCalculation(smallBomb, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], False,
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"], variables["immort"], variables["zerk"],
                              variables["ful"], True, spiritCheck, False, variables["dw"], variables["hh"], False,
                              1, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, 0, reflectDR,
                              resDR, armorDR, 1, 0, variables["ppoints"], variables["powder"], variables["currenthp"], variables["maxhp"])

    smallTsFinal = damageCalculation(smallTsBomb, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], False,
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"], variables["immort"], variables["zerk"],
                              variables["ful"], True, spiritCheck, False, variables["dw"], variables["hh"], False,
                              1, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, 0, reflectDR,
                              resDR, armorDR, 1, 0, variables["ppoints"], variables["powder"], variables["currenthp"], variables["maxhp"])
    
    return int(smallFinal), int(smallTsFinal)


#Healing calcs
def calcMageAutosHealing():
    maxDmg, minDmg, ts = autos(variables["enrage"], variables["pad1"], variables["grey"], variables["aggro"], variables["totg"])
    curseDR = curse(variables["affliction"])
    
    cadeDR = disintegrateMod(100, variables["pad4"])
    debilDR = disintegrateMod(50, variables["pad4"])
    sdDR = disintegrateMod(variables["sd"], variables["pad4"])
    disruptDR = cadeDR
    reflectDR = debilDR
    resDR = cadeDR
    
    emeraldStacks = variables["emerald"]
    absorbStacks = variables["absorb"]
    
    autosDR = protects("autos", variables["eof"], variables["enrage"])
    twinshotDR = protects("twinshot", variables["eof"], variables["enrage"])
    
    zerkAuraCheck, aegisCheck = auraCheck(variables["aura"])



    maxHealing = healingCalculation(maxDmg, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], variables["deflect"],
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"],
                              curseDR, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, autosDR, reflectDR, resDR)
    
    minHealing = healingCalculation(minDmg, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], variables["deflect"],
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"],
                              curseDR, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, autosDR, reflectDR, resDR)
    
    avgHealing = healingCalculation((maxDmg + minDmg)/2, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], variables["deflect"],
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"],
                              curseDR, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, autosDR, reflectDR, resDR)
    
    tsHealing = healingCalculation(ts, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], variables["deflect"],
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"],
                              curseDR, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, twinshotDR, reflectDR, resDR)
    
    return int(maxHealing), int(minHealing), int(avgHealing), int(tsHealing)

def calcRangeAutosHealing():
    maxDmg, minDmg, ts = autos(variables["enrage"], variables["pad1"], variables["grey"], variables["aggro"], variables["totg"])
    curseDR = curse(variables["desolation"])
    
    cadeDR = disintegrateMod(100, variables["pad4"])
    debilDR = disintegrateMod(50, variables["pad4"])
    sdDR = disintegrateMod(variables["sd"], variables["pad4"])
    disruptDR = cadeDR
    reflectDR = debilDR
    resDR = cadeDR
    
    emeraldStacks = variables["emerald"]
    absorbStacks = variables["absorb"]
    
    autosDR = protects("autos", variables["eof"], variables["enrage"])
    twinshotDR = protects("twinshot", variables["eof"], variables["enrage"])
    zerkAuraCheck, aegisCheck = auraCheck(variables["aura"])

    maxHealing = healingCalculation(maxDmg, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], variables["deflect"],
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"],
                              curseDR, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, autosDR, reflectDR, resDR)
    
    minHealing = healingCalculation(minDmg, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], variables["deflect"],
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"],
                              curseDR, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, autosDR, reflectDR, resDR)
    
    avgHealing = healingCalculation((maxDmg + minDmg)/2, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], variables["deflect"],
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"],
                              curseDR, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, autosDR, reflectDR, resDR)
    
    tsHealing = healingCalculation(ts, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], variables["deflect"],
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"],
                              curseDR, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, twinshotDR, reflectDR, resDR)
    
    return int(maxHealing), int(minHealing), int(avgHealing), int(tsHealing)

def calcSlamHealing():
    base1, base2 = slam(variables["enrage"], variables["slam"])
    
    cadeDR = disintegrateMod(100, variables["pad4"])
    debilDR = disintegrateMod(50, variables["pad4"])
    sdDR = disintegrateMod(variables["sd"], variables["pad4"])
    disruptDR = cadeDR
    reflectDR = debilDR
    resDR = cadeDR
    
    emeraldStacks = variables["emerald"]
    absorbStacks = variables["absorb"]
    
    slamDR = protects("slam", variables["eof"], variables["enrage"])
    zerkAuraCheck, aegisCheck = auraCheck(variables["aura"])

    slam1Healing = healingCalculation(base1, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], variables["deflect"],
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"],
                              1, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, slamDR, reflectDR, resDR)
    
    slam2Healing = healingCalculation(base2, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], variables["deflect"],
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"],
                              1, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, slamDR, reflectDR, resDR)
    
    return int(slam1Healing), int(slam2Healing)

def calcSmokeHealing():
    smokeBase, flamesStacks = smoke(variables["enrage"], variables["smoke"], variables["infernus"])

    cadeDR = disintegrateMod(100, variables["pad4"], flamesStacks)
    debilDR = disintegrateMod(50, variables["pad4"], flamesStacks)
    sdDR = disintegrateMod(variables["sd"], variables["pad4"], flamesStacks)
    disruptDR = cadeDR
    reflectDR = debilDR
    resDR = cadeDR
    
    emeraldStacks = variables["emerald"]
    absorbStacks = variables["absorb"]
    
    zerkAuraCheck, aegisCheck = auraCheck(variables["aura"])

    smokeHealing = healingCalculation(smokeBase, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], False,
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"],
                              1, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, 0, reflectDR, resDR)
    
    return int(smokeHealing)

def calcDecimationHealing(releaseTick):
    decimationBase = decimation(variables["enrage"], releaseTick)
    
    cadeDR = disintegrateMod(100, variables["pad4"], 0, 40)
    debilDR = disintegrateMod(50, variables["pad4"], 0, 40)
    sdDR = disintegrateMod(variables["sd"], variables["pad4"], 0, 40)
    disruptDR = cadeDR
    reflectDR = debilDR
    resDR = cadeDR
    
    emeraldStacks = variables["emerald"]
    absorbStacks = variables["absorb"]
    
    zerkAuraCheck, aegisCheck = auraCheck(variables["aura"])

    decimationHealing = healingCalculation(decimationBase, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], False,
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"],
                              1, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, 0, reflectDR, resDR)
    
    return int(decimationHealing)

def calcCageHealing():
    base = cage(variables["enrage"], variables["teamsize"], variables["totg"])
    
    cadeDR = disintegrateMod(100, variables["pad4"])
    debilDR = disintegrateMod(50, variables["pad4"])
    sdDR = disintegrateMod(variables["sd"], variables["pad4"])
    disruptDR = cadeDR
    reflectDR = debilDR
    resDR = cadeDR
    
    emeraldStacks = variables["emerald"]
    absorbStacks = variables["absorb"]
    
    cageDR = protects("cage", variables["eof"], variables["enrage"])
    zerkAuraCheck, aegisCheck = auraCheck(variables["aura"])

    cageHealing = healingCalculation(base, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], variables["deflect"],
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"],
                              1, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, cageDR, reflectDR, resDR)
    
    return int(cageHealing)

def calcBigBombHealing():
    bigBomb, smallBomb = p7(variables["mode"], variables["enrage"])

    bigBombMax = bigBomb * 1.1
    bigBombAvg = bigBomb * 1.05
    
    cadeDR = disintegrateMod(100, variables["pad4"], 0, 50)
    debilDR = disintegrateMod(50, variables["pad4"], 0, 50)
    sdDR = disintegrateMod(variables["sd"], variables["pad4"], 0, 50)
    disruptDR = cadeDR
    reflectDR = debilDR
    resDR = cadeDR
    
    emeraldStacks = variables["emerald"]
    absorbStacks = variables["absorb"]
    
    zerkAuraCheck, aegisCheck = auraCheck(variables["aura"])

    bigMaxHealFinal = healingCalculation(bigBombMax, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], False,
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"],
                              1, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, 0, reflectDR, resDR)
    
    bigMinHealFinal = healingCalculation(bigBomb, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], False,
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"],
                              1, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, 0, reflectDR, resDR)
    
    bigAvgHealFinal = healingCalculation(bigBombAvg, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], False,
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"],
                              1, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, 0, reflectDR, resDR)
    
    return int(bigMaxHealFinal), int(bigMinHealFinal), int(bigAvgHealFinal)

def calcSmallBombHealing():
    bigBomb, smallBomb = p7(variables["mode"], variables["enrage"])
    smallTsBomb = math.floor((smallBomb * variables["pad1"])/10)
    
    cadeDR = disintegrateMod(100, variables["pad4"])
    debilDR = disintegrateMod(50, variables["pad4"])
    sdDR = disintegrateMod(variables["sd"], variables["pad4"])
    disruptDR = cadeDR
    reflectDR = debilDR
    resDR = cadeDR
    
    emeraldStacks = variables["emerald"]
    absorbStacks = variables["absorb"]
    
    zerkAuraCheck, aegisCheck = auraCheck(variables["aura"])

    smallFinalHealing = healingCalculation(smallBomb, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], False,
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"],
                              1, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, 0, reflectDR, resDR)
    
    smallTsFinalHealing = healingCalculation(smallTsBomb, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], False,
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"],
                              1, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, 0, reflectDR, resDR)
    
    return int(smallFinalHealing), int(smallTsFinalHealing)

#Divert calcs
def calcMageAutosDivert():
    maxDmg, minDmg, ts = autos(variables["enrage"], variables["pad1"], variables["grey"], variables["aggro"], variables["totg"])
    curseDR = curse(variables["affliction"])
    
    cadeDR = disintegrateMod(100, variables["pad4"])
    debilDR = disintegrateMod(50, variables["pad4"])
    sdDR = disintegrateMod(variables["sd"], variables["pad4"])
    disruptDR = cadeDR
    reflectDR = debilDR
    resDR = cadeDR
    
    emeraldStacks = variables["emerald"]
    absorbStacks = variables["absorb"]
    
    autosDR = protects("autos", variables["eof"], variables["enrage"])
    twinshotDR = protects("twinshot", variables["eof"], variables["enrage"])
    
    zerkAuraCheck, aegisCheck = auraCheck(variables["aura"])

    maxDivert = divertCalculation(maxDmg, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], variables["deflect"],
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"],
                              curseDR, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, autosDR, reflectDR, resDR)
    
    minDivert = divertCalculation(minDmg, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], variables["deflect"],
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"],
                              curseDR, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, autosDR, reflectDR, resDR)
    
    avgDivert = divertCalculation((maxDmg + minDmg)/2, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], variables["deflect"],
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"],
                              curseDR, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, autosDR, reflectDR, resDR)
    
    tsDivert = divertCalculation(ts, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], variables["deflect"],
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"],
                              curseDR, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, twinshotDR, reflectDR, resDR)
    
    return maxDivert, minDivert, avgDivert, tsDivert

def calcRangeAutosDivert():
    maxDmg, minDmg, ts = autos(variables["enrage"], variables["pad1"], variables["grey"], variables["aggro"], variables["totg"])
    curseDR = curse(variables["desolation"])
    
    cadeDR = disintegrateMod(100, variables["pad4"])
    debilDR = disintegrateMod(50, variables["pad4"])
    sdDR = disintegrateMod(variables["sd"], variables["pad4"])
    disruptDR = cadeDR
    reflectDR = debilDR
    resDR = cadeDR
    
    emeraldStacks = variables["emerald"]
    absorbStacks = variables["absorb"]
    
    autosDR = protects("autos", variables["eof"], variables["enrage"])
    twinshotDR = protects("twinshot", variables["eof"], variables["enrage"])
    zerkAuraCheck, aegisCheck = auraCheck(variables["aura"])

    maxDivert = divertCalculation(maxDmg, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], variables["deflect"],
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"],
                              curseDR, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, autosDR, reflectDR, resDR)
    
    minDivert = divertCalculation(minDmg, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], variables["deflect"],
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"],
                              curseDR, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, autosDR, reflectDR, resDR)
    
    avgDivert = divertCalculation((maxDmg + minDmg)/2, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], variables["deflect"],
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"],
                              curseDR, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, autosDR, reflectDR, resDR)
    
    tsDivert = divertCalculation(ts, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], variables["deflect"],
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"],
                              curseDR, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, twinshotDR, reflectDR, resDR)
    
    return maxDivert, minDivert, avgDivert, tsDivert

def calcSlamDivert():
    base1, base2 = slam(variables["enrage"], variables["slam"])
    
    cadeDR = disintegrateMod(100, variables["pad4"])
    debilDR = disintegrateMod(50, variables["pad4"])
    sdDR = disintegrateMod(variables["sd"], variables["pad4"])
    disruptDR = cadeDR
    reflectDR = debilDR
    resDR = cadeDR
    
    emeraldStacks = variables["emerald"]
    absorbStacks = variables["absorb"]
    
    slamDR = protects("slam", variables["eof"], variables["enrage"])
    zerkAuraCheck, aegisCheck = auraCheck(variables["aura"])

    slam1Divert = divertCalculation(base1, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], variables["deflect"],
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"],
                              1, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, slamDR, reflectDR, resDR)
    
    slam2Divert = divertCalculation(base2, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], variables["deflect"],
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"],
                              1, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, slamDR, reflectDR, resDR)
    
    return slam1Divert, slam2Divert

def calcSmokeDivert():
    smokeBase, flamesStacks = smoke(variables["enrage"], variables["smoke"], variables["infernus"])

    cadeDR = disintegrateMod(100, variables["pad4"], flamesStacks)
    debilDR = disintegrateMod(50, variables["pad4"], flamesStacks)
    sdDR = disintegrateMod(variables["sd"], variables["pad4"], flamesStacks)
    disruptDR = cadeDR
    reflectDR = debilDR
    resDR = cadeDR
    
    emeraldStacks = variables["emerald"]
    absorbStacks = variables["absorb"]
    
    zerkAuraCheck, aegisCheck = auraCheck(variables["aura"])

    smokeDivert = divertCalculation(smokeBase, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], False,
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"],
                              1, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, 0, reflectDR, resDR)
    
    return smokeDivert

def calcDecimationDivert(releaseTick):
    decimationBase = decimation(variables["enrage"], releaseTick)
    
    cadeDR = disintegrateMod(100, variables["pad4"], 0, 40)
    debilDR = disintegrateMod(50, variables["pad4"], 0, 40)
    sdDR = disintegrateMod(variables["sd"], variables["pad4"], 0, 40)
    disruptDR = cadeDR
    reflectDR = debilDR
    resDR = cadeDR
    
    emeraldStacks = variables["emerald"]
    absorbStacks = variables["absorb"]
    
    zerkAuraCheck, aegisCheck = auraCheck(variables["aura"])

    decimationDivert = divertCalculation(decimationBase, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], False,
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"],
                              1, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, 0, reflectDR, resDR)
    
    return decimationDivert

def calcCageDivert():
    base = cage(variables["enrage"], variables["teamsize"], variables["totg"])
    
    cadeDR = disintegrateMod(100, variables["pad4"])
    debilDR = disintegrateMod(50, variables["pad4"])
    sdDR = disintegrateMod(variables["sd"], variables["pad4"])
    disruptDR = cadeDR
    reflectDR = debilDR
    resDR = cadeDR
    
    emeraldStacks = variables["emerald"]
    absorbStacks = variables["absorb"]
    
    cageDR = protects("cage", variables["eof"], variables["enrage"])
    zerkAuraCheck, aegisCheck = auraCheck(variables["aura"])

    cageDivert = divertCalculation(base, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], variables["deflect"],
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"],
                              1, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, cageDR, reflectDR, resDR)
    
    return cageDivert

def calcBigBombDivert():
    bigBomb, smallBomb = p7(variables["mode"], variables["enrage"])

    bigBombMax = bigBomb * 1.1
    bigBombAvg = bigBomb * 1.05
    
    cadeDR = disintegrateMod(100, variables["pad4"], 0, 50)
    debilDR = disintegrateMod(50, variables["pad4"], 0, 50)
    sdDR = disintegrateMod(variables["sd"], variables["pad4"], 0, 50)
    disruptDR = cadeDR
    reflectDR = debilDR
    resDR = cadeDR
    
    emeraldStacks = variables["emerald"]
    absorbStacks = variables["absorb"]
    
    zerkAuraCheck, aegisCheck = auraCheck(variables["aura"])

    bigMaxDivertFinal = divertCalculation(bigBombMax, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], False,
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"],
                              1, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, 0, reflectDR, resDR)
    
    bigMinDivertFinal = divertCalculation(bigBomb, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], False,
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"],
                              1, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, 0, reflectDR, resDR)
    
    bigAvgDivertFinal = divertCalculation(bigBombAvg, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], False,
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"],
                              1, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, 0, reflectDR, resDR)
    
    return bigMaxDivertFinal, bigMinDivertFinal, bigAvgDivertFinal

def calcSmallBombDivert():
    bigBomb, smallBomb = p7(variables["mode"], variables["enrage"])
    smallTsBomb = math.floor((smallBomb * variables["pad1"])/10)
    
    cadeDR = disintegrateMod(100, variables["pad4"])
    debilDR = disintegrateMod(50, variables["pad4"])
    sdDR = disintegrateMod(variables["sd"], variables["pad4"])
    disruptDR = cadeDR
    reflectDR = debilDR
    resDR = cadeDR
    
    emeraldStacks = variables["emerald"]
    absorbStacks = variables["absorb"]
    
    zerkAuraCheck, aegisCheck = auraCheck(variables["aura"])

    smallFinalDivert = divertCalculation(smallBomb, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], False,
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"],
                              1, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, 0, reflectDR, resDR)
    
    smallTsFinalDivert = divertCalculation(smallTsBomb, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], False,
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"],
                              1, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, 0, reflectDR, resDR)
    
    return smallFinalDivert, smallTsFinalDivert

#Refl calcs
def calcMageAutosReflect():
    maxDmg, minDmg, ts = autos(variables["enrage"], variables["pad1"], variables["grey"], variables["aggro"], variables["totg"])
    curseDR = curse(variables["affliction"])
    
    cadeDR = disintegrateMod(100, variables["pad4"])
    debilDR = disintegrateMod(50, variables["pad4"])
    sdDR = disintegrateMod(variables["sd"], variables["pad4"])
    disruptDR = cadeDR
    reflectDR = debilDR
    resDR = cadeDR
    
    emeraldStacks = variables["emerald"]
    absorbStacks = variables["absorb"]
    
    autosDR = protects("autos", variables["eof"], variables["enrage"])
    twinshotDR = protects("twinshot", variables["eof"], variables["enrage"])
    armorDR = armorReduction(variables["helm"], variables["top"], variables["bottoms"], variables["gloves"], variables["boots"], variables["shield"], variables["fort"], variables["def"])
    cryptMelee, cryptMagic = cryptMod(variables["helm"], variables["top"], variables["bottoms"], variables["gloves"], variables["boots"])
    adDR = animateDead(variables["helm"], variables["top"], variables["bottoms"], variables["gloves"], variables["boots"], variables["shield"], variables["ovl"], variables["aura"], variables["def"])
    zerkAuraCheck, aegisCheck = auraCheck(variables["aura"])
    spiritCheck = spiritShieldCheck(variables["shield"])
    
    if variables["gloves"] == "Deathtouch bracelet":
        dtbEquipCheck = True
    else:
        dtbEquipCheck = False
    
    hpNeeded, pad6Stacks, healingReduction = pad6eff(variables["pad6"], variables["maxhp"], variables["currenthp"])
    pad6Stacks = 1 + pad6Stacks/100

    maxReflFinal, maxDeflFinal, maxDarkFinal, maxVengFinal, maxDtbFinal = reflectCalculation(maxDmg, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], variables["deflect"],
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"], variables["immort"], variables["zerk"],
                              variables["ful"], True, spiritCheck, True, variables["dw"], variables["hh"], variables["ad"],
                              curseDR, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, autosDR, reflectDR,
                              resDR, armorDR, cryptMagic, adDR, variables["ppoints"], variables["powder"], variables["currenthp"], variables["maxhp"],
                              variables["vuln"], variables["croe"], pad6Stacks, variables["veng_check"], dtbEquipCheck)
    
    minReflFinal, minDeflFinal, minDarkFinal, minVengFinal, minDtbFinal = reflectCalculation(minDmg, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], variables["deflect"],
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"], variables["immort"], variables["zerk"],
                              variables["ful"], True, spiritCheck, True, variables["dw"], variables["hh"], variables["ad"],
                              curseDR, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, autosDR, reflectDR,
                              resDR, armorDR, cryptMagic, adDR, variables["ppoints"], variables["powder"], variables["currenthp"], variables["maxhp"],
                              variables["vuln"], variables["croe"], pad6Stacks, variables["veng_check"], dtbEquipCheck)
    
    avgReflFinal, avgDeflFinal, avgDarkFinal, avgVengFinal, avgDtbFinal = reflectCalculation((maxDmg + minDmg)/2, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], variables["deflect"],
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"], variables["immort"], variables["zerk"],
                              variables["ful"], True, spiritCheck, True, variables["dw"], variables["hh"], variables["ad"],
                              curseDR, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, autosDR, reflectDR,
                              resDR, armorDR, cryptMagic, adDR, variables["ppoints"], variables["powder"], variables["currenthp"], variables["maxhp"],
                              variables["vuln"], variables["croe"], pad6Stacks, variables["veng_check"], dtbEquipCheck)
    
    tsReflFinal, tsDeflFinal, tsDarkFinal, tsVengFinal, tsDtbFinal = reflectCalculation(ts, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], variables["deflect"],
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"], variables["immort"], variables["zerk"],
                              variables["ful"], True, spiritCheck, True, variables["dw"], variables["hh"], variables["ad"],
                              curseDR, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, twinshotDR, reflectDR,
                              resDR, armorDR, cryptMagic, adDR, variables["ppoints"], variables["powder"], variables["currenthp"], variables["maxhp"],
                              variables["vuln"], variables["croe"], pad6Stacks, variables["veng_check"], dtbEquipCheck)

    if variables["hitcaps"] == "Grey Hp":
        Hitcap = 32500
        maxFinal = min(maxReflFinal + maxDeflFinal + maxDarkFinal + maxDtbFinal, Hitcap) + maxVengFinal
        minFinal = min(minReflFinal + minDeflFinal + minDarkFinal + minDtbFinal, Hitcap) + minVengFinal
        avgFinal = min(avgReflFinal + avgDeflFinal + avgDarkFinal + avgDtbFinal, Hitcap) + avgVengFinal
        tsFinal = min(tsReflFinal + tsDeflFinal + tsDarkFinal  + tsDtbFinal, Hitcap) + tsVengFinal

    elif variables["hitcaps"] == "Green Hp":
        Hitcap = 30000
        maxFinal = min(maxReflFinal + maxDeflFinal + maxDarkFinal + maxDtbFinal, Hitcap) + maxVengFinal
        minFinal = min(minReflFinal + minDeflFinal + minDarkFinal + minDtbFinal, Hitcap) + minVengFinal
        avgFinal = min(avgReflFinal + avgDeflFinal + avgDarkFinal + avgDtbFinal, Hitcap) + avgVengFinal
        tsFinal = min(tsReflFinal + tsDeflFinal + tsDarkFinal  + tsDtbFinal, Hitcap) + tsVengFinal

    else:
        maxFinal = maxReflFinal + maxDeflFinal + maxDarkFinal + maxDtbFinal + maxVengFinal
        minFinal = minReflFinal + minDeflFinal + minDarkFinal + minDtbFinal + minVengFinal
        avgFinal = avgReflFinal + avgDeflFinal + avgDarkFinal + avgDtbFinal + avgVengFinal
        tsFinal = tsReflFinal + tsDeflFinal + tsDarkFinal  + tsDtbFinal + tsVengFinal

    return int(maxFinal), int(minFinal), int(avgFinal), int(tsFinal)

def calcRangeAutosReflect():
    maxDmg, minDmg, ts = autos(variables["enrage"], variables["pad1"], variables["grey"], variables["aggro"], variables["totg"])
    curseDR = curse(variables["desolation"])
    
    cadeDR = disintegrateMod(100, variables["pad4"])
    debilDR = disintegrateMod(50, variables["pad4"])
    sdDR = disintegrateMod(variables["sd"], variables["pad4"])
    disruptDR = cadeDR
    reflectDR = debilDR
    resDR = cadeDR
    
    emeraldStacks = variables["emerald"]
    absorbStacks = variables["absorb"]
    
    autosDR = protects("autos", variables["eof"], variables["enrage"])
    twinshotDR = protects("twinshot", variables["eof"], variables["enrage"])
    armorDR = armorReduction(variables["helm"], variables["top"], variables["bottoms"], variables["gloves"], variables["boots"], variables["shield"], variables["fort"], variables["def"])

    adDR = animateDead(variables["helm"], variables["top"], variables["bottoms"], variables["gloves"], variables["boots"], variables["shield"], variables["ovl"], variables["aura"], variables["def"])
    zerkAuraCheck, aegisCheck = auraCheck(variables["aura"])
    spiritCheck = spiritShieldCheck(variables["shield"])
    
    if variables["gloves"] == "Deathtouch bracelet":
        dtbEquipCheck = True
    else:
        dtbEquipCheck = False
    
    hpNeeded, pad6Stacks, healingReduction = pad6eff(variables["pad6"], variables["maxhp"], variables["currenthp"])
    pad6Stacks = 1 + pad6Stacks/100

    maxReflFinal, maxDeflFinal, maxDarkFinal, maxVengFinal, maxDtbFinal = reflectCalculation(maxDmg, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], variables["deflect"],
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"], variables["immort"], variables["zerk"],
                              variables["ful"], True, spiritCheck, True, variables["dw"], variables["hh"], variables["ad"],
                              curseDR, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, autosDR, reflectDR,
                              resDR, armorDR, 1, adDR, variables["ppoints"], variables["powder"], variables["currenthp"], variables["maxhp"],
                              variables["vuln"], variables["croe"], pad6Stacks, variables["veng_check"], dtbEquipCheck)
    
    minReflFinal, minDeflFinal, minDarkFinal, minVengFinal, minDtbFinal = reflectCalculation(minDmg, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], variables["deflect"],
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"], variables["immort"], variables["zerk"],
                              variables["ful"], True, spiritCheck, True, variables["dw"], variables["hh"], variables["ad"],
                              curseDR, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, autosDR, reflectDR,
                              resDR, armorDR, 1, adDR, variables["ppoints"], variables["powder"], variables["currenthp"], variables["maxhp"],
                              variables["vuln"], variables["croe"], pad6Stacks, variables["veng_check"], dtbEquipCheck)
    
    avgReflFinal, avgDeflFinal, avgDarkFinal, avgVengFinal, avgDtbFinal = reflectCalculation((maxDmg + minDmg)/2, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], variables["deflect"],
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"], variables["immort"], variables["zerk"],
                              variables["ful"], True, spiritCheck, True, variables["dw"], variables["hh"], variables["ad"],
                              curseDR, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, autosDR, reflectDR,
                              resDR, armorDR, 1, adDR, variables["ppoints"], variables["powder"], variables["currenthp"], variables["maxhp"],
                              variables["vuln"], variables["croe"], pad6Stacks, variables["veng_check"], dtbEquipCheck)
    
    tsReflFinal, tsDeflFinal, tsDarkFinal, tsVengFinal, tsDtbFinal = reflectCalculation(ts, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], variables["deflect"],
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"], variables["immort"], variables["zerk"],
                              variables["ful"], True, spiritCheck, True, variables["dw"], variables["hh"], variables["ad"],
                              curseDR, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, twinshotDR, reflectDR,
                              resDR, armorDR, 1, adDR, variables["ppoints"], variables["powder"], variables["currenthp"], variables["maxhp"],
                              variables["vuln"], variables["croe"], pad6Stacks, variables["veng_check"], dtbEquipCheck)

    if variables["hitcaps"] == "Grey Hp":
        Hitcap = 32500
        maxFinal = min(maxReflFinal + maxDeflFinal + maxDarkFinal + maxDtbFinal, Hitcap) + maxVengFinal
        minFinal = min(minReflFinal + minDeflFinal + minDarkFinal + minDtbFinal, Hitcap) + minVengFinal
        avgFinal = min(avgReflFinal + avgDeflFinal + avgDarkFinal + avgDtbFinal, Hitcap) + avgVengFinal
        tsFinal = min(tsReflFinal + tsDeflFinal + tsDarkFinal  + tsDtbFinal, Hitcap) + tsVengFinal

    elif variables["hitcaps"] == "Green Hp":
        Hitcap = 30000
        maxFinal = min(maxReflFinal + maxDeflFinal + maxDarkFinal + maxDtbFinal, Hitcap) + maxVengFinal
        minFinal = min(minReflFinal + minDeflFinal + minDarkFinal + minDtbFinal, Hitcap) + minVengFinal
        avgFinal = min(avgReflFinal + avgDeflFinal + avgDarkFinal + avgDtbFinal, Hitcap) + avgVengFinal
        tsFinal = min(tsReflFinal + tsDeflFinal + tsDarkFinal  + tsDtbFinal, Hitcap) + tsVengFinal

    else:
        maxFinal = maxReflFinal + maxDeflFinal + maxDarkFinal + maxDtbFinal + maxVengFinal
        minFinal = minReflFinal + minDeflFinal + minDarkFinal + minDtbFinal + minVengFinal
        avgFinal = avgReflFinal + avgDeflFinal + avgDarkFinal + avgDtbFinal + avgVengFinal
        tsFinal = tsReflFinal + tsDeflFinal + tsDarkFinal  + tsDtbFinal + tsVengFinal

    return int(maxFinal), int(minFinal), int(avgFinal), int(tsFinal)

def calcSlamReflect():
    base1, base2 = slam(variables["enrage"], variables["slam"])
    
    cadeDR = disintegrateMod(100, variables["pad4"])
    debilDR = disintegrateMod(50, variables["pad4"])
    sdDR = disintegrateMod(variables["sd"], variables["pad4"])
    disruptDR = cadeDR
    reflectDR = debilDR
    resDR = cadeDR
    
    emeraldStacks = variables["emerald"]
    absorbStacks = variables["absorb"]
    
    slamDR = protects("slam", variables["eof"], variables["enrage"])
    armorDR = armorReduction(variables["helm"], variables["top"], variables["bottoms"], variables["gloves"], variables["boots"], variables["shield"], variables["fort"], variables["def"])
    cryptMelee, cryptMagic = cryptMod(variables["helm"], variables["top"], variables["bottoms"], variables["gloves"], variables["boots"])
    adDR = animateDead(variables["helm"], variables["top"], variables["bottoms"], variables["gloves"], variables["boots"], variables["shield"], variables["ovl"], variables["aura"], variables["def"])
    zerkAuraCheck, aegisCheck = auraCheck(variables["aura"])
    spiritCheck = spiritShieldCheck(variables["shield"])
    
    if variables["gloves"] == "Deathtouch bracelet":
        dtbEquipCheck = True
    else:
        dtbEquipCheck = False
    
    hpNeeded, pad6Stacks, healingReduction = pad6eff(variables["pad6"], variables["maxhp"], variables["currenthp"])
    pad6Stacks = 1 + pad6Stacks/100

    slam1ReflFinal, slam1DeflFinal, slam1DarkFinal, slam1VengFinal, slam1DtbFinal = reflectCalculation(base1, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], variables["deflect"],
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"], variables["immort"], variables["zerk"],
                              variables["ful"], True, spiritCheck, True, variables["dw"], variables["hh"], variables["ad"],
                              1, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, slamDR, reflectDR,
                              resDR, armorDR, cryptMelee, adDR, variables["ppoints"], variables["powder"], variables["currenthp"], variables["maxhp"],
                              variables["vuln"], variables["croe"], pad6Stacks, variables["veng_check"], dtbEquipCheck)
    
    slam2ReflFinal, slam2DeflFinal, slam2DarkFinal, slam2VengFinal, slam2DtbFinal = reflectCalculation(base2, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], variables["deflect"],
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"], variables["immort"], variables["zerk"],
                              variables["ful"], True, spiritCheck, True, variables["dw"], variables["hh"], variables["ad"],
                              1, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, slamDR, reflectDR,
                              resDR, armorDR, cryptMelee, adDR, variables["ppoints"], variables["powder"], variables["currenthp"], variables["maxhp"],
                              variables["vuln"], variables["croe"], pad6Stacks, variables["veng_check"], dtbEquipCheck)

    if variables["hitcaps"] == "Grey Hp":
        Hitcap = 32500
        slam1Final = min(slam1ReflFinal + slam1DeflFinal + slam1DarkFinal + slam1DtbFinal, Hitcap) + slam1VengFinal
        slam2Final = min(slam2ReflFinal + slam2DeflFinal + slam2DarkFinal  + slam2DtbFinal, Hitcap) + slam2VengFinal

    elif variables["hitcaps"] == "Green Hp":
        Hitcap = 30000
        slam1Final = min(slam1ReflFinal + slam1DeflFinal + slam1DarkFinal + slam1DtbFinal, Hitcap) + slam1VengFinal
        slam2Final = min(slam2ReflFinal + slam2DeflFinal + slam2DarkFinal  + slam2DtbFinal, Hitcap) + slam2VengFinal

    else:
        slam1Final = slam1ReflFinal + slam1DeflFinal + slam1DarkFinal + slam1DtbFinal + slam1VengFinal
        slam2Final = slam2ReflFinal + slam2DeflFinal + slam2DarkFinal  + slam2DtbFinal + slam2VengFinal

    return int(slam1Final), int(slam2Final)

def calcSmokeReflect():
    smokeBase, flamesStacks = smoke(variables["enrage"], variables["smoke"], variables["infernus"])
    
    cadeDR = disintegrateMod(100, variables["pad4"], flamesStacks)
    debilDR = disintegrateMod(50, variables["pad4"], flamesStacks)
    sdDR = disintegrateMod(variables["sd"], variables["pad4"], flamesStacks)
    disruptDR = cadeDR
    reflectDR = debilDR
    resDR = cadeDR
    
    emeraldStacks = variables["emerald"]
    absorbStacks = variables["absorb"]
    
    armorDR = armorReduction(variables["helm"], variables["top"], variables["bottoms"], variables["gloves"], variables["boots"], variables["shield"], variables["fort"], variables["def"])
    zerkAuraCheck, aegisCheck = auraCheck(variables["aura"])
    spiritCheck = spiritShieldCheck(variables["shield"])
    
    if variables["gloves"] == "Deathtouch bracelet":
        dtbEquipCheck = True
    else:
        dtbEquipCheck = False
    
    hpNeeded, pad6Stacks, healingReduction = pad6eff(variables["pad6"], variables["maxhp"], variables["currenthp"])
    pad6Stacks = 1 + pad6Stacks/100

    smokeReflFinal, smokeDeflFinal, smokeDarkFinal, smokeVengFinal, smokeDtbFinal = reflectCalculation(smokeBase, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], False,
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"], variables["immort"], variables["zerk"],
                              variables["ful"], True, spiritCheck, False, variables["dw"], variables["hh"], False,
                              1, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, 0, reflectDR,
                              resDR, armorDR, 1, 0, variables["ppoints"], variables["powder"], variables["currenthp"], variables["maxhp"],
                              variables["vuln"], variables["croe"], pad6Stacks, variables["veng_check"], dtbEquipCheck)
    
    if variables["hitcaps"] == "Grey Hp":
        Hitcap = 32500
        smokeFinal = min(smokeReflFinal + smokeDarkFinal, Hitcap)

    elif variables["hitcaps"] == "Green Hp":
        Hitcap = 30000
        smokeFinal = min(smokeReflFinal + smokeDarkFinal, Hitcap)

    else:
        smokeFinal = smokeReflFinal + smokeDarkFinal

    return int(smokeFinal)

def calcDecimationReflect(releaseTick):
    decimationBase = decimation(variables["enrage"], releaseTick)
    
    cadeDR = disintegrateMod(100, variables["pad4"], 0, 40)
    debilDR = disintegrateMod(50, variables["pad4"], 0, 40)
    sdDR = disintegrateMod(variables["sd"], variables["pad4"], 0, 40)
    disruptDR = cadeDR
    reflectDR = debilDR
    resDR = cadeDR
    
    emeraldStacks = variables["emerald"]
    absorbStacks = variables["absorb"]
    
    armorDR = armorReduction(variables["helm"], variables["top"], variables["bottoms"], variables["gloves"], variables["boots"], variables["shield"], variables["fort"], variables["def"])
    zerkAuraCheck, aegisCheck = auraCheck(variables["aura"])
    spiritCheck = spiritShieldCheck(variables["shield"])
    
    if variables["gloves"] == "Deathtouch bracelet":
        dtbEquipCheck = True
    else:
        dtbEquipCheck = False
    
    hpNeeded, pad6Stacks, healingReduction = pad6eff(variables["pad6"], variables["maxhp"], variables["currenthp"])
    pad6Stacks = 1 + pad6Stacks/100

    decimationReflFinal, decimationDeflFinal, decimationDarkFinal, decimationVengFinal, decimationDtbFinal = reflectCalculation(decimationBase, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], False,
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"], variables["immort"], variables["zerk"],
                              variables["ful"], True, spiritCheck, False, variables["dw"], variables["hh"], False,
                              1, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, 0, reflectDR,
                              resDR, armorDR, 1, 0, variables["ppoints"], variables["powder"], variables["currenthp"], variables["maxhp"],
                              variables["vuln"], variables["croe"], pad6Stacks, variables["veng_check"], dtbEquipCheck)
    
    if variables["hitcaps"] == "Grey Hp":
        Hitcap = 32500
        decimationFinal = min(decimationReflFinal + decimationDarkFinal, Hitcap)

    elif variables["hitcaps"] == "Green Hp":
        Hitcap = 30000
        decimationFinal = min(decimationReflFinal + decimationDarkFinal, Hitcap)

    else:
        decimationFinal = decimationReflFinal + decimationDarkFinal

    return int(decimationFinal)

def calcCageReflect():
    base = cage(variables["enrage"], variables["teamsize"], variables["totg"])
    
    cadeDR = disintegrateMod(100, variables["pad4"])
    debilDR = disintegrateMod(50, variables["pad4"])
    sdDR = disintegrateMod(variables["sd"], variables["pad4"])
    disruptDR = cadeDR
    reflectDR = debilDR
    resDR = cadeDR
    
    emeraldStacks = variables["emerald"]
    absorbStacks = variables["absorb"]
    
    cageDR = protects("cage", variables["eof"], variables["enrage"])
    armorDR = armorReduction(variables["helm"], variables["top"], variables["bottoms"], variables["gloves"], variables["boots"], variables["shield"], variables["fort"], variables["def"])
    cryptMelee, cryptMagic = cryptMod(variables["helm"], variables["top"], variables["bottoms"], variables["gloves"], variables["boots"])
    adDR = animateDead(variables["helm"], variables["top"], variables["bottoms"], variables["gloves"], variables["boots"], variables["shield"], variables["ovl"], variables["aura"], variables["def"])
    zerkAuraCheck, aegisCheck = auraCheck(variables["aura"])
    spiritCheck = spiritShieldCheck(variables["shield"])
    
    if variables["gloves"] == "Deathtouch bracelet":
        dtbEquipCheck = True
    else:
        dtbEquipCheck = False
    
    hpNeeded, pad6Stacks, healingReduction = pad6eff(variables["pad6"], variables["maxhp"], variables["currenthp"])
    pad6Stacks = 1 + pad6Stacks/100

    maxReflFinal, maxDeflFinal, maxDarkFinal, maxVengFinal, maxDtbFinal = reflectCalculation(base, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], variables["deflect"],
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"], variables["immort"], variables["zerk"],
                              variables["ful"], True, spiritCheck, True, variables["dw"], variables["hh"], variables["ad"],
                              1, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, cageDR, reflectDR,
                              resDR, armorDR, cryptMagic, adDR, variables["ppoints"], variables["powder"], variables["currenthp"], variables["maxhp"],
                              variables["vuln"], variables["croe"], pad6Stacks, variables["veng_check"], dtbEquipCheck)

    if variables["hitcaps"] == "Grey Hp":
        Hitcap = 32500
        cageFinal = min(maxReflFinal + maxDeflFinal + maxDarkFinal + maxDtbFinal, Hitcap) + maxVengFinal

    elif variables["hitcaps"] == "Green Hp":
        Hitcap = 30000
        cageFinal = min(maxReflFinal + maxDeflFinal + maxDarkFinal + maxDtbFinal, Hitcap) + maxVengFinal

    else:
        cageFinal = maxReflFinal + maxDeflFinal + maxDarkFinal + maxDtbFinal + maxVengFinal

    return int(cageFinal)

def calcBigBombReflect():
    bigBomb, smallBomb = p7(variables["mode"], variables["enrage"])
    bigBombMax = bigBomb * 1.1
    bigBombAvg = bigBomb * 1.05

    cadeDR = disintegrateMod(100, variables["pad4"], 0, 50)
    debilDR = disintegrateMod(50, variables["pad4"], 0, 50)
    sdDR = disintegrateMod(variables["sd"], variables["pad4"], 0, 50)
    disruptDR = cadeDR
    reflectDR = debilDR
    resDR = cadeDR
    
    emeraldStacks = variables["emerald"]
    absorbStacks = variables["absorb"]
    
    zerkAuraCheck, aegisCheck = auraCheck(variables["aura"])
    spiritCheck = spiritShieldCheck(variables["shield"])
    
    if variables["gloves"] == "Deathtouch bracelet":
        dtbEquipCheck = True
    else:
        dtbEquipCheck = False
    
    hpNeeded, pad6Stacks, healingReduction = pad6eff(variables["pad6"], variables["maxhp"], variables["currenthp"])
    pad6Stacks = 1 + pad6Stacks/100

    bigMaxReflFinal, bigMaxDeflFinal, bigMaxDarkFinal, bigMaxVengFinal, bigMaxDtbFinal = reflectCalculation(bigBombMax, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], False,
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"], variables["immort"], variables["zerk"],
                              variables["ful"], True, spiritCheck, False, variables["dw"], variables["hh"], False,
                              1, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, 0, reflectDR,
                              resDR, 1, 1, 0, variables["ppoints"], variables["powder"], variables["currenthp"], variables["maxhp"],
                              variables["vuln"], variables["croe"], pad6Stacks, variables["veng_check"], dtbEquipCheck)
    
    bigMinReflFinal, bigMinDeflFinal, bigMinDarkFinal, bigMinVengFinal, bigMinDtbFinal = reflectCalculation(bigBombMax, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], False,
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"], variables["immort"], variables["zerk"],
                              variables["ful"], True, spiritCheck, False, variables["dw"], variables["hh"], False,
                              1, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, 0, reflectDR,
                              resDR, 1, 1, 0, variables["ppoints"], variables["powder"], variables["currenthp"], variables["maxhp"],
                              variables["vuln"], variables["croe"], pad6Stacks, variables["veng_check"], dtbEquipCheck)
    
    bigAvgReflFinal, bigAvgDeflFinal, bigAvgDarkFinal, bigAvgVengFinal, bigAvgDtbFinal = reflectCalculation(bigBombMax, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], False,
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"], variables["immort"], variables["zerk"],
                              variables["ful"], True, spiritCheck, False, variables["dw"], variables["hh"], False,
                              1, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, 0, reflectDR,
                              resDR, 1, 1, 0, variables["ppoints"], variables["powder"], variables["currenthp"], variables["maxhp"],
                              variables["vuln"], variables["croe"], pad6Stacks, variables["veng_check"], dtbEquipCheck)
    
    if variables["hitcaps"] == "Grey Hp":
        Hitcap = 32500
        bigMaxFinal = min(bigMaxReflFinal + bigMaxDarkFinal, Hitcap)
        bigMinFinal = min(bigMinReflFinal + bigMinDarkFinal, Hitcap)
        bigAvgFinal = min(bigAvgReflFinal + bigAvgDarkFinal, Hitcap)

    elif variables["hitcaps"] == "Green Hp":
        Hitcap = 30000
        bigMaxFinal = min(bigMaxReflFinal + bigMaxDarkFinal, Hitcap)
        bigMinFinal = min(bigMinReflFinal + bigMinDarkFinal, Hitcap)
        bigAvgFinal = min(bigAvgReflFinal + bigAvgDarkFinal, Hitcap)

    else:
        bigMaxFinal = bigMaxReflFinal + bigMaxDarkFinal
        bigMinFinal = bigMinReflFinal + bigMinDarkFinal
        bigAvgFinal = bigAvgReflFinal + bigAvgDarkFinal

    return int(bigMaxFinal), int(bigMinFinal), int(bigAvgFinal)

def calcSmallBombReflect():
    bigBomb, smallBomb = p7(variables["mode"], variables["enrage"])
    smallTsBomb = math.floor((smallBomb * variables["pad1"])/10)

    cadeDR = disintegrateMod(100, variables["pad4"])
    debilDR = disintegrateMod(50, variables["pad4"])
    sdDR = disintegrateMod(variables["sd"], variables["pad4"])
    disruptDR = cadeDR
    reflectDR = debilDR
    resDR = cadeDR
    
    emeraldStacks = variables["emerald"]
    absorbStacks = variables["absorb"]
    
    armorDR = armorReduction(variables["helm"], variables["top"], variables["bottoms"], variables["gloves"], variables["boots"], variables["shield"], variables["fort"], variables["def"])
    zerkAuraCheck, aegisCheck = auraCheck(variables["aura"])
    spiritCheck = spiritShieldCheck(variables["shield"])
    
    if variables["gloves"] == "Deathtouch bracelet":
        dtbEquipCheck = True
    else:
        dtbEquipCheck = False
    
    hpNeeded, pad6Stacks, healingReduction = pad6eff(variables["pad6"], variables["maxhp"], variables["currenthp"])
    pad6Stacks = 1 + pad6Stacks/100

    smallReflFinal, smallDeflFinal, smallDarkFinal, smallVengFinal, smallDtbFinal = reflectCalculation(smallBomb, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], False,
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"], variables["immort"], variables["zerk"],
                              variables["ful"], True, spiritCheck, False, variables["dw"], variables["hh"], False,
                              1, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, 0, reflectDR,
                              resDR, armorDR, 1, 0, variables["ppoints"], variables["powder"], variables["currenthp"], variables["maxhp"],
                              variables["vuln"], variables["croe"], pad6Stacks, variables["veng_check"], dtbEquipCheck)
    
    smallTsReflFinal, smallTsDeflFinal, smallTsDarkFinal, smallTsVengFinal, smallTsDtbFinal = reflectCalculation(smallBomb, variables["pulv"], variables["cade"], variables["debil"], zerkAuraCheck, variables["sever"], variables["enfeeble"], 
                              variables["anchor"], aegisCheck, True, variables["disr"], variables["pad3"], variables["pad5"], False,
                              variables["anti"], variables["refl"], variables["darkness"], variables["divert"], variables["immort"], variables["zerk"],
                              variables["ful"], True, spiritCheck, False, variables["dw"], variables["hh"], False,
                              1, cadeDR, debilDR, absorbStacks, sdDR, emeraldStacks, disruptDR, 0, reflectDR,
                              resDR, armorDR, 1, 0, variables["ppoints"], variables["powder"], variables["currenthp"], variables["maxhp"],
                              variables["vuln"], variables["croe"], pad6Stacks, variables["veng_check"], dtbEquipCheck)
    
    if variables["hitcaps"] == "Grey Hp":
        Hitcap = 32500
        smallFinal = min(smallReflFinal + smallDarkFinal, Hitcap)
        smallTsFinal = min(smallTsReflFinal + smallTsDarkFinal, Hitcap)

    elif variables["hitcaps"] == "Green Hp":
        Hitcap = 30000
        smallFinal = min(smallReflFinal + smallDarkFinal, Hitcap)
        smallTsFinal = min(smallTsReflFinal + smallTsDarkFinal, Hitcap)

    else:
        smallFinal = smallReflFinal + smallDarkFinal
        smallTsFinal = smallTsReflFinal + smallTsDarkFinal

    return int(smallFinal), int(smallTsFinal)

