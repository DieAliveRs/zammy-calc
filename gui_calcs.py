import customtkinter as ctk
import calcs
import gui as g
from settings import variables, loadSettings, saveSettings

root = g.root

def loseFocus(event):
    x, y = event.x, event.y

    if 0 <= x <= g.enrageInput.winfo_width() and 0 <= y <= g.enrageInput.winfo_height():
        pass
    else:
        root.focus_set()

def checkboxCheck(value):
    if value == 1:
        return True
    else:
        return False

def startupSettings():
    loadedVariables = loadSettings()
    if loadedVariables == 1:
        g.enrageInput.insert(0, "4000")
        g.pad1Menu.set("0")
        g.pad2Menu.set("0")
        g.pad4Menu.set("0")
        g.pad6Menu.set("0")
        g.chokeInput.insert(0, "1")
        g.slamInput.insert(0, "3")
        g.smokeInput.insert(0, "4")
        g.tombInput.insert(0, "1")
        g.decimationInput.insert(0, "30")
        g.aggroCheckbox.select()
        g.p7modeMenu.set("Charge value")
        g.p7chargeEntry.insert(0, "0")
        g.p7iterationEntry.insert(0, "0")
        g.p7redBarEntry.insert(0, "0")

        g.helmMenu.set("Cryptbloom")
        g.topMenu.set("Cryptbloom")
        g.bottomsMenu.set("Cryptbloom")
        g.glovesMenu.set("Cryptbloom")
        g.bootsMenu.set("Cryptbloom")
        g.shieldMenu.set("Spirit")
        g.eofCheckbox.select()
        g.ovlMenu.set("Elder overload")
        g.defEntry.insert(0, "99")
        g.powderCheckbox.select()
        g.ppointsInput.insert(0, "990")
        g.afflictionInput.insert(0, "18")
        g.desolationInput.insert(0, "0")
        g.maxhpInput.insert(0, "13537")
        g.currenthpInput.insert(0, "13537")
        g.boneshieldInput.insert(0, "60")
        g.totgCheckbox.select()
        g.puzzleboxCheckbox.select()

        g.divertMenu.set("None")
        g.sdMenu.set("0")
        g.auraMenu.set("None")
        g.absorbMenu.set("0")
        g.emeraldMenu.set("0")
        g.deflectCheckbox.select()

        g.hitcapsMenu.set("Grey Hp")
        g.vulnCheckbox.select()

        teamsizeMenu.set("2")
        inputadrenEntry.insert(0, "9")
        drEntry.insert(0, "50")
        specMenu.set("P7 Bomb")
        specInfernusEntry.insert(0, "4")

    else:
        #Zamorak var
        g.enrageInput.insert(0, loadedVariables["enrage"])
        g.pad1Menu.set(loadedVariables["pad1"])
        g.pad2Menu.set(loadedVariables["pad2"])
        if loadedVariables["pad3"] == True: g.pad3Checkbox.select()
        g.pad4Menu.set(loadedVariables["pad4"])
        if loadedVariables["pad5"] == True: g.pad5Checkbox.select()
        g.pad6Menu.set(loadedVariables["pad6"])
        g.chokeInput.insert(0, loadedVariables["choke"])
        g.slamInput.insert(0, loadedVariables["slam"])
        g.smokeInput.insert(0, loadedVariables["smoke"])
        if loadedVariables["infernus"] == True: g.smokeCheckbox.select()
        g.tombInput.insert(0, loadedVariables["tomb"])
        g.decimationInput.insert(0, loadedVariables["decimation"])
        if loadedVariables["grey"] == True: g.greyCheckbox.select()
        if loadedVariables["aggro"] == True: g.aggroCheckbox.select()
        g.p7modeMenu.set(loadedVariables["mode"])
        g.p7chargeEntry.insert(0, loadedVariables["charge_input"])
        g.p7iterationEntry.insert(0, loadedVariables["iteration_input"])
        g.p7redBarEntry.insert(0, loadedVariables["red_input"])

        #Player var
        g.helmMenu.set(loadedVariables["helm"])
        g.topMenu.set(loadedVariables["top"])
        g.bottomsMenu.set(loadedVariables["bottoms"])
        g.glovesMenu.set(loadedVariables["gloves"])
        g.bootsMenu.set(loadedVariables["boots"])
        g.shieldMenu.set(loadedVariables["shield"])
        if loadedVariables["eof"] == True: g.eofCheckbox.select()
        g.ovlMenu.set(loadedVariables["ovl"])
        g.defEntry.insert(0, loadedVariables["def"])
        if loadedVariables["powder"] == True: g.powderCheckbox.select()
        g.ppointsInput.insert(0, loadedVariables["ppoints"])
        g.afflictionInput.insert(0, loadedVariables["affliction"])
        g.desolationInput.insert(0, loadedVariables["desolation"])
        g.maxhpInput.insert(0, loadedVariables["maxhp"])
        g.currenthpInput.insert(0, loadedVariables["currenthp"])
        g.boneshieldInput.insert(0, loadedVariables["boneshield"])
        if loadedVariables["totg"] == True: g.totgCheckbox.select()
        if loadedVariables["puzzlebox"] == True: g.puzzleboxCheckbox.select()

        #Modifiers var
        if loadedVariables["disr"] == True: g.disrCheckbox.select()
        if loadedVariables["cade"] == True: g.cadeCheckbox.select()
        g.divertMenu.set(loadedVariables["divert_res_check"])
        if loadedVariables["refl"] == True: g.reflCheckbox.select()
        if loadedVariables["debil"] == True: g.debilCheckbox.select()
        g.sdMenu.set(loadedVariables["sd"])
        if loadedVariables["immort"] == True: g.immortCheckbox.select()
        if loadedVariables["anti"] == True: g.antiCheckbox.select()
        if loadedVariables["ful"] == True: g.fulCheckbox.select()
        g.auraMenu.set(loadedVariables["aura"])
        if loadedVariables["zerk"] == True: g.zerkCheckbox.select()
        if loadedVariables["pulv"] == True: g.pulvCheckbox.select()
        if loadedVariables["sever"] == True: g.severCheckbox.select()
        g.absorbMenu.set(loadedVariables["absorb"])
        if loadedVariables["enfeeble"] == True: g.enfeebleCheckbox.select()
        g.emeraldMenu.set(loadedVariables["emerald"])
        if loadedVariables["anchor"] == True: g.anchorCheckbox.select()
        if loadedVariables["darkness"] == True: g.darknessCheckbox.select()
        if loadedVariables["deflect"] == True: g.deflectCheckbox.select()
        if loadedVariables["fort"] == True: g.fortCheckbox.select()
        if loadedVariables["dw"] == True: g.dwCheckbox.select()
        if loadedVariables["hh"] == True: g.hhCheckbox.select()
        if loadedVariables["ad"] == True: g.adCheckbox.select()

        #Reflect settings
        g.hitcapsMenu.set(loadedVariables["hitcaps"])
        if loadedVariables["vuln"] == True: g.vulnCheckbox.select()
        if loadedVariables["croe"] == True: g.cryptVulnCheckbox.select()
        if loadedVariables["defl_check"] == True: g.deflCheckbox.select()
        if loadedVariables["veng_check"] == True: g.vengCheckbox.select()
        if loadedVariables["dtb_check"] == True: g.dtbCheckbox.select()

        #Misc settings
        teamsizeMenu.set(loadedVariables["teamsize"])
        inputadrenEntry.insert(0, loadedVariables["adren"])
        drEntry.insert(0, loadedVariables["disint_dr"])
        specMenu.set(loadedVariables["spec"])
        specInfernusEntry.insert(0, loadedVariables["disint_smoke"])
        if loadedVariables["disint_infernus"] == True: specInfernusCheckbox.select()


def updateVariables():
    #Zamorak var
    variables["enrage"] = int(g.enrageInput.get())
    variables["pad1"] = int(g.pad1Menu.get())
    variables["pad2"] = int(g.pad2Menu.get())
    variables["pad3"] = checkboxCheck(g.pad3Checkbox.get())
    variables["pad4"] = int(g.pad4Menu.get())
    variables["pad5"] = checkboxCheck(g.pad5Checkbox.get())
    variables["pad6"] = int(g.pad6Menu.get())
    variables["choke"] = int(g.chokeInput.get())
    variables["slam"] = int(g.slamInput.get())
    variables["smoke"] = int(g.smokeInput.get())
    variables["infernus"] = checkboxCheck(g.smokeCheckbox.get())
    variables["tomb"] = int(g.tombInput.get())
    variables["decimation"] = int(g.decimationInput.get())
    variables["grey"] = checkboxCheck(g.greyCheckbox.get())
    variables["aggro"] = checkboxCheck(g.aggroCheckbox.get())
    variables["mode"] = g.p7modeMenu.get()
    variables["charge_input"] = int(g.p7chargeEntry.get())
    variables["iteration_input"] = int(g.p7iterationEntry.get())
    variables["red_input"] = int(g.p7redBarEntry.get())
    
    #Player Var
    variables["helm"] = g.helmMenu.get()
    variables["top"] = g.topMenu.get()
    variables["bottoms"] = g.bottomsMenu.get()
    variables["gloves"] = g.glovesMenu.get()
    variables["boots"] = g.bootsMenu.get()
    variables["shield"] = g.shieldMenu.get()
    variables["eof"] = checkboxCheck(g.eofCheckbox.get())
    variables["ovl"] = g.ovlMenu.get()
    variables["def"] = int(g.defEntry.get())
    variables["powder"] = checkboxCheck(g.powderCheckbox.get())
    variables["ppoints"] = int(g.ppointsInput.get())
    variables["affliction"] = int(g.afflictionInput.get())
    variables["desolation"] = int(g.desolationInput.get())
    variables["maxhp"] = int(g.maxhpInput.get())
    variables["currenthp"] = int(g.currenthpInput.get())
    variables["boneshield"] = int(g.boneshieldInput.get())
    variables["totg"] = checkboxCheck(g.totgCheckbox.get())
    variables["puzzlebox"] = checkboxCheck(g.puzzleboxCheckbox.get())

    #Modifiers Var
    variables["disr"] = checkboxCheck(g.disrCheckbox.get())
    variables["cade"] = checkboxCheck(g.cadeCheckbox.get())
    variables["divert"] = True if g.divertMenu.get() == "Divert" or g.divertMenu.get() == "Resonance" else False
    variables["divert_res_check"] = g.divertMenu.get()
    variables["refl"] = checkboxCheck(g.reflCheckbox.get())
    variables["debil"] = checkboxCheck(g.debilCheckbox.get())
    variables["sd"] = int(g.sdMenu.get())
    variables["immort"] = checkboxCheck(g.immortCheckbox.get())
    variables["anti"] = checkboxCheck(g.antiCheckbox.get())
    variables["ful"] = checkboxCheck(g.fulCheckbox.get())
    variables["aura"] = g.auraMenu.get()
    variables["zerk"] = checkboxCheck(g.zerkCheckbox.get())
    variables["pulv"] = checkboxCheck(g.pulvCheckbox.get())
    variables["sever"] = checkboxCheck(g.severCheckbox.get())
    variables["absorb"] = int(g.absorbMenu.get())
    variables["enfeeble"] = checkboxCheck(g.enfeebleCheckbox.get())
    variables["emerald"] = int(g.emeraldMenu.get())
    variables["anchor"] = checkboxCheck(g.anchorCheckbox.get())
    variables["darkness"] = checkboxCheck(g.darknessCheckbox.get())
    variables["deflect"] = checkboxCheck(g.deflectCheckbox.get())
    variables["fort"] = checkboxCheck(g.fortCheckbox.get())
    variables["dw"] = checkboxCheck(g.dwCheckbox.get())
    variables["hh"] = checkboxCheck(g.hhCheckbox.get())
    variables["ad"] = checkboxCheck(g.adCheckbox.get())

    #Misc var
    variables["teamsize"] = int(teamsizeMenu.get())
    variables["vuln"] = checkboxCheck(g.vulnCheckbox.get())
    variables["croe"] = checkboxCheck(g.cryptVulnCheckbox.get())
    variables["veng_check"] = checkboxCheck(g.vengCheckbox.get())
    variables["defl_check"] = checkboxCheck(g.deflCheckbox.get())
    variables["dtb_check"] = checkboxCheck(g.dtbCheckbox.get())
    variables["hitcaps"] = g.hitcapsMenu.get()

def updateHp():
    p1Hp, p2Hp, p3Hp, p4Hp, p5Hp, p6Hp, p7Hp, grey, witch, demon, rune = calcs.phaseHp(variables["enrage"], variables["teamsize"])

    p1hpOutputLabel.configure(text=f'{p1Hp:,}')
    p2hpOutputLabel.configure(text=f'{p2Hp:,}')
    p3hpOutputLabel.configure(text=f'{p3Hp:,}')
    p4hpOutputLabel.configure(text=f'{p4Hp:,}')
    p5hpOutputLabel.configure(text=f'{p5Hp:,}')
    p6hpOutputLabel.configure(text=f'{p6Hp:,}')
    p7hpOutputLabel.configure(text=f'{p7Hp:,}')
    greyhpOutputLabel.configure(text=f'{grey:,}')
    witchhpOutputLabel.configure(text=f'{witch:,}')
    demonhpOutputLabel.configure(text=f'{demon:,}')
    runehpOutputLabel.configure(text=f'{rune:,}')

def updatePads():
    #Variables:
    variables["adren"] = float(inputadrenEntry.get())
    variables["disint_dr"] = int(drEntry.get())
    variables["spec"] = specMenu.get()
    variables["disint_smoke"] = int(specInfernusEntry.get())
    variables["disint_infernus"] = checkboxCheck(specInfernusCheckbox.get())

    #Pad1
    adren, tsDmg = calcs.pad1eff(variables["adren"], variables["pad1"])
    adrengainOutputLabel.configure(text=round(adren, 1))
    tsdmgOutputLabel.configure(text=tsDmg)

    #Pad2
    cdr, thresh, effHp = calcs.pad2eff(variables["pad2"], variables["maxhp"], variables["fort"])
    hasteOutputLabel.configure(text="{}%".format(cdr))
    smiteOutputLabel.configure(text=thresh)
    effhpOutputLabel.configure(text=effHp)

    #Pad4
    effectiveness = calcs.pad4eff(variables["disint_dr"], variables["pad4"], variables["spec"], variables["disint_smoke"], variables["disint_infernus"])
    effectivenessOutputLabel.configure(text="{}%".format(effectiveness))

    #Pad6
    hpNeeded, dmgBonus, healingReduction = calcs.pad6eff(variables["pad6"], variables["maxhp"], variables["currenthp"])
    hpNeededOutputLabel.configure(text="< {}".format(hpNeeded))
    pad6buffOutputLabel.configure(text="{}%".format(dmgBonus))
    pad6debuffOutputLabel.configure(text="{}%".format(healingReduction))

def updateSettings():
    if g.p7modeMenu.get() == "Charge value":
        redBar, smallBomb, iteration = calcs.p7(variables["mode"], variables["enrage"])
        chargeStart, chargeCap = calcs.chargeCalcs()

        g.p7infoLabel.configure(text="Red bar: {}".format(redBar))
        g.p7infoLabel.grid(row=3, column=0, columnspan=2, padx=g.imageXPad, pady=5, sticky="w")

        g.p7infoLabel1.configure(text="Iteration: {}".format(iteration))
        g.p7infoLabel1.grid(row=4, column=0, columnspan=2, padx=g.imageXPad, pady=5, sticky="w")

        g.p7infoLabel2.configure(text="Charge value starts at {} and caps at {}.".format(chargeStart, chargeCap))
        g.p7infoLabel2.grid(row=5, column=0, columnspan=2, padx=g.imageXPad, pady=5, sticky="w")

    elif g.p7modeMenu.get() == "Iteration":
        redBar, smallBomb, iteration = calcs.p7(variables["mode"], variables["enrage"])
        charge = calcs.iterationToCharge(variables["iteration_input"])

        g.p7infoLabel.configure(text="Red bar: {}".format(redBar))
        g.p7infoLabel.grid(row=3, column=0, columnspan=2, padx=g.imageXPad, pady=5, sticky="w")

        g.p7infoLabel1.configure(text="Current charge: {}".format(charge))
        g.p7infoLabel1.grid(row=4, column=0, columnspan=2, padx=g.imageXPad, pady=5, sticky="w")

        g.p7infoLabel2.configure(text="Iterations increase every tick, starts at 0 and caps at 500.")
        g.p7infoLabel2.grid(row=5, column=0, columnspan=2, padx=g.imageXPad, pady=5, sticky="w")

    elif g.p7modeMenu.get() == "Red bar":
        g.p7infoLabel.grid_forget()
        g.p7infoLabel1.grid_forget()

        g.p7infoLabel2.configure(text="Red bar input can only calculate Chaos damage.")
        g.p7infoLabel2.grid(row=3, column=0, columnspan=2, padx=g.imageXPad, pady=5, sticky="w")


def updateDamage():
    mageMax, mageMin, mageAvg, mageTS = calcs.calcMageAutos()
    rangeMax, rangeMin, rangeAvg, rangeTS = calcs.calcRangeAutos()
    slam1, slam2 = calcs.calcSlam()
    minInf, maxInf, avgInf = calcs.calcInfernus()
    smokeFixed = calcs.calcSmoke()
    tombFixed = calcs.calcDecimation(variables["tomb"])
    decimationFixed = calcs.calcDecimation(variables["decimation"])
    cageFixed = calcs.calcCage()
    bigMax, bigMin, bigAvg = calcs.calcBigBomb()
    smallFixed, smallTs = calcs.calcSmallBomb()

    mageMinDmgOutputLabel.configure(text=mageMin, font=textFont)
    mageMaxDmgOutputLabel.configure(text=mageMax, font=textFont)
    mageAvgDmgOutputLabel.configure(text=mageAvg, font=textFont)
    mageTsDmgOutputLabel.configure(text=mageTS, font=textFont)

    rangeMinDmgOutputLabel.configure(text=rangeMin, font=textFont)
    rangeMaxDmgOutputLabel.configure(text=rangeMax, font=textFont)
    rangeAvgDmgOutputLabel.configure(text=rangeAvg, font=textFont)
    rangeTsDmgOutputLabel.configure(text=rangeTS, font=textFont)

    slam1FixedDmgOutputLabel.configure(text=slam1, font=textFont)  
    slam2FixedDmgOutputLabel.configure(text=slam2, font=textFont)

    infernusMinDmgOutputLabel.configure(text=minInf, font=textFont)
    infernusMaxDmgOutputLabel.configure(text=maxInf, font=textFont)
    infernusAvgDmgOutputLabel.configure(text=avgInf, font=textFont)

    smokeFixedDmgOutputLabel.configure(text=smokeFixed, font=textFont)
    tombFixedDmgOutputLabel.configure(text=tombFixed, font=textFont)
    decimationFixedDmgOutputLabel.configure(text=decimationFixed, font=textFont)
    cageFixedDmgOutputLabel.configure(text=cageFixed, font=textFont)
    
    chaosMinDmgOutputLabel.configure(text=bigMin, font=textFont)
    chaosMaxDmgOutputLabel.configure(text=bigMax, font=textFont)
    chaosAvgDmgOutputLabel.configure(text=bigAvg, font=textFont)
    smallFixedDmgOutputLabel.configure(text=smallFixed, font=textFont)
    smallTsDmgOutputLabel.configure(text=smallTs, font=textFont)


def updateHealing():
    if variables["divert_res_check"] == "Resonance":
        mageMaxHeal, mageMinHeal, mageAvgHeal, mageTsHeal = calcs.calcMageAutosHealing()
        rangeMaxHeal, rangeMinHeal, rangeAvgHeal, rangeTsHeal = calcs.calcRangeAutosHealing()
        slam1Heal, slam2Heal = calcs.calcSlamHealing()
        smokeHeal = calcs.calcSmokeHealing()
        tombHeal = calcs.calcDecimationHealing(variables["tomb"])
        decimationHeal = calcs.calcDecimationHealing(variables["decimation"])
        cageHeal = calcs.calcCageHealing()
        bigMaxHeal, bigMinHeal, bigAvgHeal = calcs.calcBigBombHealing()
        smallFixedHeal, smallTsHeal = calcs.calcSmallBombHealing()

        mageMinHealOutputLabel.configure(text=mageMinHeal, font=textFont)
        mageMaxHealOutputLabel.configure(text=mageMaxHeal, font=textFont)
        mageAvgHealOutputLabel.configure(text=mageAvgHeal, font=textFont)
        mageTsHealOutputLabel.configure(text=mageTsHeal, font=textFont)

        rangeMinHealOutputLabel.configure(text=rangeMinHeal, font=textFont)
        rangeMaxHealOutputLabel.configure(text=rangeMaxHeal, font=textFont)
        rangeAvgHealOutputLabel.configure(text=rangeAvgHeal, font=textFont)
        rangeTsHealOutputLabel.configure(text=rangeTsHeal, font=textFont)

        slam1FixedHealOutputLabel.configure(text=slam1Heal, font=textFont)  
        slam2FixedHealOutputLabel.configure(text=slam2Heal, font=textFont)

        smokeFixedHealOutputLabel.configure(text=smokeHeal, font=textFont)
        tombFixedHealOutputLabel.configure(text=tombHeal, font=textFont)
        decimationFixedHealOutputLabel.configure(text=decimationHeal, font=textFont)
        cageFixedHealOutputLabel.configure(text=cageHeal, font=textFont)

        chaosMinHealOutputLabel.configure(text=bigMinHeal, font=textFont)
        chaosMaxHealOutputLabel.configure(text=bigMaxHeal, font=textFont)
        chaosAvgHealOutputLabel.configure(text=bigAvgHeal, font=textFont)
        smallFixedHealOutputLabel.configure(text=smallFixedHeal, font=textFont)
        smallTsHealOutputLabel.configure(text=smallTsHeal, font=textFont)


    elif variables["divert_res_check"] == "Divert":
        mageMaxDivert, mageMinDivert, mageAvgDivert, mageTsDivert = calcs.calcMageAutosDivert()
        rangeMaxDivert, rangeMinDivert, rangeAvgDivert, rangeTsDivert = calcs.calcRangeAutosDivert()
        slam1Divert, slam2Divert = calcs.calcSlamDivert()
        smokeDivert = calcs.calcSmokeDivert()
        tombDivert = calcs.calcDecimationDivert(variables["tomb"])
        decimationDivert = calcs.calcDecimationDivert(variables["decimation"])
        cageDivert = calcs.calcCageDivert()
        bigMaxDivert, bigMinDivert, bigAvgDivert = calcs.calcBigBombDivert()
        smallFixedDivert, smallTsDivert = calcs.calcSmallBombDivert()

        mageMinHealOutputLabel.configure(text=mageMinDivert, font=textFont)
        mageMaxHealOutputLabel.configure(text=mageMaxDivert, font=textFont)
        mageAvgHealOutputLabel.configure(text=mageAvgDivert, font=textFont)
        mageTsHealOutputLabel.configure(text=mageTsDivert, font=textFont)

        rangeMinHealOutputLabel.configure(text=rangeMinDivert, font=textFont)
        rangeMaxHealOutputLabel.configure(text=rangeMaxDivert, font=textFont)
        rangeAvgHealOutputLabel.configure(text=rangeAvgDivert, font=textFont)
        rangeTsHealOutputLabel.configure(text=rangeTsDivert, font=textFont)

        slam1FixedHealOutputLabel.configure(text=slam1Divert, font=textFont)  
        slam2FixedHealOutputLabel.configure(text=slam2Divert, font=textFont)

        smokeFixedHealOutputLabel.configure(text=smokeDivert, font=textFont)
        tombFixedHealOutputLabel.configure(text=tombDivert, font=textFont)
        decimationFixedHealOutputLabel.configure(text=decimationDivert, font=textFont)
        cageFixedHealOutputLabel.configure(text=cageDivert, font=textFont)

        chaosMinHealOutputLabel.configure(text=bigMinDivert, font=textFont)
        chaosMaxHealOutputLabel.configure(text=bigMaxDivert, font=textFont)
        chaosAvgHealOutputLabel.configure(text=bigAvgDivert, font=textFont)
        smallFixedHealOutputLabel.configure(text=smallFixedDivert, font=textFont)
        smallTsHealOutputLabel.configure(text=smallTsDivert, font=textFont)

    else:
        mageMinHealOutputLabel.configure(text=0, font=textFont)
        mageMaxHealOutputLabel.configure(text=0, font=textFont)
        mageAvgHealOutputLabel.configure(text=0, font=textFont)
        mageTsHealOutputLabel.configure(text=0, font=textFont)

        rangeMinHealOutputLabel.configure(text=0, font=textFont)
        rangeMaxHealOutputLabel.configure(text=0, font=textFont)
        rangeAvgHealOutputLabel.configure(text=0, font=textFont)
        rangeTsHealOutputLabel.configure(text=0, font=textFont)

        slam1FixedHealOutputLabel.configure(text=0, font=textFont)  
        slam2FixedHealOutputLabel.configure(text=0, font=textFont)

        smokeFixedHealOutputLabel.configure(text=0, font=textFont)
        tombFixedHealOutputLabel.configure(text=0, font=textFont)
        decimationFixedHealOutputLabel.configure(text=0, font=textFont)
        cageFixedHealOutputLabel.configure(text=0, font=textFont)

        chaosMinHealOutputLabel.configure(text=0, font=textFont)
        chaosMaxHealOutputLabel.configure(text=0, font=textFont)
        chaosAvgHealOutputLabel.configure(text=0, font=textFont)
        smallFixedHealOutputLabel.configure(text=0, font=textFont)
        smallTsHealOutputLabel.configure(text=0, font=textFont)


def updateReflect():
    mageMax, mageMin, mageAvg, mageTS = calcs.calcMageAutosReflect()
    rangeMax, rangeMin, rangeAvg, rangeTS = calcs.calcRangeAutosReflect()
    slam1, slam2 = calcs.calcSlamReflect()
    smokeFixed = calcs.calcSmokeReflect()
    tombFixed = calcs.calcDecimationReflect(variables["tomb"])
    decimationFixed = calcs.calcDecimationReflect(variables["decimation"])
    cageFixed = calcs.calcCageReflect()
    bigMax, bigMin, bigAvg = calcs.calcBigBombReflect()
    smallFixed, smallTs = calcs.calcSmallBombReflect()

    mageMinReflOutputLabel.configure(text=mageMin, font=textFont)
    mageMaxReflOutputLabel.configure(text=mageMax, font=textFont)
    mageAvgReflOutputLabel.configure(text=mageAvg, font=textFont)
    mageTsReflOutputLabel.configure(text=mageTS, font=textFont)

    rangeMinReflOutputLabel.configure(text=rangeMin, font=textFont)
    rangeMaxReflOutputLabel.configure(text=rangeMax, font=textFont)
    rangeAvgReflOutputLabel.configure(text=rangeAvg, font=textFont)
    rangeTsReflOutputLabel.configure(text=rangeTS, font=textFont)

    slam1FixedReflOutputLabel.configure(text=slam1, font=textFont)  
    slam2FixedReflOutputLabel.configure(text=slam2, font=textFont)

    smokeFixedReflOutputLabel.configure(text=smokeFixed, font=textFont)
    tombFixedReflOutputLabel.configure(text=tombFixed, font=textFont)
    decimationFixedReflOutputLabel.configure(text=decimationFixed, font=textFont)
    cageFixedReflOutputLabel.configure(text=cageFixed, font=textFont)
    
    chaosMinReflOutputLabel.configure(text=bigMin, font=textFont)
    chaosMaxReflOutputLabel.configure(text=bigMax, font=textFont)
    chaosAvgReflOutputLabel.configure(text=bigAvg, font=textFont)
    smallFixedReflOutputLabel.configure(text=smallFixed, font=textFont)
    smallTsReflOutputLabel.configure(text=smallTs, font=textFont)

def update(event):
    if event != "":
        loseFocus(event)
    updateVariables()
    updateHp()
    updatePads()
    updateSettings()
    updateDamage()
    updateHealing()
    updateReflect()


root.bind("<Button-1>", update)
root.bind("<Button-2>", update)

titleFont = ("Arial Greek", 14, 'bold')
subtitleFont = ("Arial Greek", 12, "bold")
textFont = ("Arial Greek", 12)

frameWidth = 20
column1Weight=1

#Column=1 frame
column1Frame = ctk.CTkFrame(master=root, width=frameWidth, corner_radius=0)
column1Frame.grid(row=0, column=2, rowspan=5, padx=5, pady=10, sticky="nsew")
column1Frame.grid_columnconfigure(0, weight=0)
column1Frame.grid_columnconfigure(1, weight=column1Weight)

# Misc frame (column=1)
miscFrame = ctk.CTkFrame(master=column1Frame, width=frameWidth, corner_radius=0)
miscFrame.grid(row=0, column=1, padx=10, pady=(10,5), sticky="nsew")
miscFrame.grid_columnconfigure(0, weight=0)
miscFrame.grid_columnconfigure(1, weight=column1Weight)

hpLabel = ctk.CTkLabel(master=miscFrame, text="Health points scaling", font=titleFont)
hpLabel.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

teamsizeLabel = ctk.CTkLabel(master=miscFrame, text="Teamsize", font=subtitleFont)
teamsizeLabel.grid(row=1, column=0, padx=5, pady=5)

teamsizeMenu = ctk.CTkOptionMenu(master=miscFrame, values=["1", "2", "3", "4", "5"], command=g.commandUpdate, width=g.digitMenuWidth, corner_radius=0)
teamsizeMenu.grid(row=1, column=1, padx=5, pady=5)

hp_yspacing = 0
yspacing = 1
xspacing = 10

p1hpLabel = ctk.CTkLabel(master=miscFrame, text="P1")
p1hpLabel.grid(row=2, column=0, padx=xspacing, pady=hp_yspacing)
p1hpOutputLabel = ctk.CTkLabel(master=miscFrame, text="")
p1hpOutputLabel.grid(row=2, column=1, padx=xspacing, pady=hp_yspacing)

p2hpLabel = ctk.CTkLabel(master=miscFrame, text="P2")
p2hpLabel.grid(row=3, column=0, padx=xspacing, pady=hp_yspacing)
p2hpOutputLabel = ctk.CTkLabel(master=miscFrame, text="")
p2hpOutputLabel.grid(row=3, column=1, padx=xspacing, pady=hp_yspacing)

p3hpLabel = ctk.CTkLabel(master=miscFrame, text="P3")
p3hpLabel.grid(row=4, column=0, padx=xspacing, pady=hp_yspacing)
p3hpOutputLabel = ctk.CTkLabel(master=miscFrame, text="")
p3hpOutputLabel.grid(row=4, column=1, padx=xspacing, pady=hp_yspacing)

p4hpLabel = ctk.CTkLabel(master=miscFrame, text="P4")
p4hpLabel.grid(row=5, column=0, padx=xspacing, pady=hp_yspacing)
p4hpOutputLabel = ctk.CTkLabel(master=miscFrame, text="")
p4hpOutputLabel.grid(row=5, column=1, padx=xspacing, pady=hp_yspacing)

p5hpLabel = ctk.CTkLabel(master=miscFrame, text="P5")
p5hpLabel.grid(row=6, column=0, padx=xspacing, pady=hp_yspacing)
p5hpOutputLabel = ctk.CTkLabel(master=miscFrame, text="")
p5hpOutputLabel.grid(row=6, column=1, padx=xspacing, pady=hp_yspacing)

p6hpLabel = ctk.CTkLabel(master=miscFrame, text="P6")
p6hpLabel.grid(row=7, column=0, padx=xspacing, pady=hp_yspacing)
p6hpOutputLabel = ctk.CTkLabel(master=miscFrame, text="")
p6hpOutputLabel.grid(row=7, column=1, padx=xspacing, pady=hp_yspacing)

p7hpLabel = ctk.CTkLabel(master=miscFrame, text="P7")
p7hpLabel.grid(row=8, column=0, padx=xspacing, pady=hp_yspacing)
p7hpOutputLabel = ctk.CTkLabel(master=miscFrame, text="")
p7hpOutputLabel.grid(row=8, column=1, padx=xspacing, pady=hp_yspacing)

greyhpLabel = ctk.CTkLabel(master=miscFrame, text="Initial grey Hp")
greyhpLabel.grid(row=9, column=0, padx=xspacing, pady=hp_yspacing)
greyhpOutputLabel = ctk.CTkLabel(master=miscFrame, text="")
greyhpOutputLabel.grid(row=9, column=1, padx=xspacing, pady=hp_yspacing)

witchhpLabel = ctk.CTkLabel(master=miscFrame, text="Witch")
witchhpLabel.grid(row=10, column=0, padx=xspacing, pady=hp_yspacing)
witchhpOutputLabel = ctk.CTkLabel(master=miscFrame, text="")
witchhpOutputLabel.grid(row=10, column=1, padx=xspacing, pady=hp_yspacing)

demonhpLabel = ctk.CTkLabel(master=miscFrame, text="Demon")
demonhpLabel.grid(row=11, column=0, padx=xspacing, pady=hp_yspacing)
demonhpOutputLabel = ctk.CTkLabel(master=miscFrame, text="")
demonhpOutputLabel.grid(row=11, column=1, padx=xspacing, pady=hp_yspacing)

runehpLabel = ctk.CTkLabel(master=miscFrame, text="Rune respawn")
runehpLabel.grid(row=12, column=0, padx=xspacing, pady=hp_yspacing)
runehpOutputLabel = ctk.CTkLabel(master=miscFrame, text="")
runehpOutputLabel.grid(row=12, column=1, padx=xspacing, pady=hp_yspacing)

midPadding = (5,5)
boxWidth = 60
# Pad effects frames (column=1)
# Pad 1 frame
padEffectsFrame1 = ctk.CTkFrame(master=column1Frame, width=frameWidth, corner_radius=0)
padEffectsFrame1.grid(row=1, column=1, padx=10, pady=midPadding, sticky="nsew")
padEffectsFrame1.grid_columnconfigure(0, weight=0)
padEffectsFrame1.grid_columnconfigure(1, weight=column1Weight)
padEffectsFrame1.grid_columnconfigure(2, weight=0, minsize=100)
# padEffectsFrame1.grid_rowconfigure(0, weight=1)


padEffectsLabel = ctk.CTkLabel(master=padEffectsFrame1, text="Pad effects", font=titleFont)
padEffectsLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=yspacing, sticky="nsew")

animaflowLabel = ctk.CTkLabel(master=padEffectsFrame1, text="Anima Flow", font=subtitleFont)
animaflowLabel.grid(row=1, column=0, columnspan=3, padx=10, pady=yspacing)

inputadrenLabel = ctk.CTkLabel(master=padEffectsFrame1, text="Base adrenaline gain:")
inputadrenLabel.grid(row=2, column=0, columnspan=2, padx=10, pady=yspacing, sticky="w")
inputadrenEntry = ctk.CTkEntry(master=padEffectsFrame1, width=boxWidth, corner_radius=0)
inputadrenEntry.grid(row=2, column=2, padx=5, pady=yspacing, sticky="w")

adrengainImage = ctk.CTkLabel(master=padEffectsFrame1, image=g.pad1_green, text="")
adrengainImage.grid(row=3, column=0, padx=10, pady=yspacing)
adrengainLabel = ctk.CTkLabel(master=padEffectsFrame1, text="Adrenaline gained")
adrengainLabel.grid(row=3, column=1, padx=0, pady=yspacing, sticky="w")
adrengainOutputLabel = ctk.CTkLabel(master=padEffectsFrame1, text="")
adrengainOutputLabel.grid(row=3, column=2, padx=5, pady=yspacing, sticky="w")

tsdmgImage = ctk.CTkLabel(master=padEffectsFrame1, image=g.pad1_red, text="")
tsdmgImage.grid(row=4, column=0, padx=10, pady=yspacing)
tsdmgLabel = ctk.CTkLabel(master=padEffectsFrame1, text="Twinshot damage")
tsdmgLabel.grid(row=4, column=1, padx=0, pady=yspacing, sticky="w")
tsdmgOutputLabel = ctk.CTkLabel(master=padEffectsFrame1, text="")
tsdmgOutputLabel.grid(row=4, column=2, padx=5, pady=yspacing, sticky="w")

# Pad 2 frame
padEffectsFrame2 = ctk.CTkFrame(master=column1Frame, width=frameWidth, corner_radius=0)
padEffectsFrame2.grid(row=2, column=1, padx=10, pady=midPadding, sticky="nsew")
padEffectsFrame2.grid_columnconfigure(0, weight=0)
padEffectsFrame2.grid_columnconfigure(1, weight=column1Weight)
padEffectsFrame2.grid_columnconfigure(2, weight=0, minsize=100)

smiteLabel = ctk.CTkLabel(master=padEffectsFrame2, text="Smite", font=subtitleFont)
smiteLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=yspacing, sticky="nsew")

hasteImage = ctk.CTkLabel(master=padEffectsFrame2, image=g.pad6_green, text="")
hasteImage.grid(row=1, column=0, padx=10, pady=yspacing)
hasteLabel = ctk.CTkLabel(master=padEffectsFrame2, text="Cooldown reduction")
hasteLabel.grid(row=1, column=1, padx=0, pady=yspacing, sticky="w")
hasteOutputLabel = ctk.CTkLabel(master=padEffectsFrame2, text="")
hasteOutputLabel.grid(row=1, column=2, padx=5, pady=yspacing, sticky="w")

smiteImage = ctk.CTkLabel(master=padEffectsFrame2, image=g.pad2_red, text="")
smiteImage.grid(row=2, column=0, padx=10, pady=yspacing)
smiteLabel = ctk.CTkLabel(master=padEffectsFrame2, text="Execute threshold")
smiteLabel.grid(row=2, column=1, padx=0, pady=yspacing, sticky="w")
smiteOutputLabel = ctk.CTkLabel(master=padEffectsFrame2, text="")
smiteOutputLabel.grid(row=2, column=2, padx=5, pady=yspacing, sticky="w")

effhpImage = ctk.CTkLabel(master=padEffectsFrame2, image=g.maxhp, text="")
effhpImage.grid(row=3, column=0, padx=10, pady=yspacing)
effhpLabel = ctk.CTkLabel(master=padEffectsFrame2, text="Effective max hp")
effhpLabel.grid(row=3, column=1, padx=0, pady=yspacing, sticky="w")
effhpOutputLabel = ctk.CTkLabel(master=padEffectsFrame2, text="")
effhpOutputLabel.grid(row=3, column=2, padx=5, pady=yspacing, sticky="w")

# Pad 4 frame
padEffectsFrame4 = ctk.CTkFrame(master=column1Frame, width=frameWidth, corner_radius=0)
padEffectsFrame4.grid(row=3, column=1, padx=10, pady=midPadding, sticky="nsew")
padEffectsFrame4.grid_columnconfigure(0, weight=0)
padEffectsFrame4.grid_columnconfigure(1, weight=column1Weight, minsize=100)
padEffectsFrame4.grid_columnconfigure(2, weight=0)

disintegrateLabel = ctk.CTkLabel(master=padEffectsFrame4, text="Disintegrate", font=subtitleFont)
disintegrateLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=yspacing)

drLabel = ctk.CTkLabel(master=padEffectsFrame4, text="Defensives' DR %:")
drLabel.grid(row=1, column=0, columnspan=2, padx=10, pady=yspacing, sticky="w")
drEntry = ctk.CTkEntry(master=padEffectsFrame4, width=boxWidth, corner_radius=0)
drEntry.grid(row=1, column=2, padx=10, pady=yspacing, sticky="w")

def infernusCallback(*args):
    if specMenu.get() != "Smoke":
        specInfernusImage.grid_forget()
        specInfernusLabel.grid_forget()
        specInfernusEntry.grid_forget()
        specInfernusCheckbox.grid_forget()

        effectivenessImage.grid(row=3, column=0, padx=10, pady=yspacing)
        effectivenessLabel.grid(row=3, column=1, padx=0, pady=yspacing, sticky="w")
        effectivenessOutputLabel.grid(row=3, column=2, padx=10, pady=yspacing, sticky="w")
    else:
        specInfernusImage.grid(row=3, column=0, columnspan=2, padx=10, pady=yspacing, sticky="w")
        specInfernusLabel.grid(row=3, column=1, columnspan=2, padx=0, pady=yspacing, sticky="w")
        specInfernusEntry.grid(row=3, column=2, padx=10, pady=yspacing, sticky="w")
        specInfernusCheckbox.grid(row=3, column=2, padx=5, pady=yspacing, sticky="e")

        effectivenessImage.grid(row=4, column=0, padx=10, pady=yspacing)
        effectivenessLabel.grid(row=4, column=1, padx=0, pady=yspacing, sticky="w")
        effectivenessOutputLabel.grid(row=4, column=2, padx=10, pady=yspacing, sticky="w")
    g.commandUpdate()

specLabel = ctk.CTkLabel(master=padEffectsFrame4, text="Spec:")
specLabel.grid(row=2, column=0, columnspan=2, padx=10, pady=yspacing, sticky="w")
specMenu = ctk.CTkOptionMenu(master=padEffectsFrame4, values=["Other", "Smoke", "Decimation", "P7 Bomb"], command=infernusCallback, width=120, corner_radius=0)
specMenu.grid(row=2, column=2, padx=10, pady=yspacing, sticky="w")

specInfernusImage = ctk.CTkLabel(master=padEffectsFrame4, image=g.smoke, text="")
specInfernusLabel = ctk.CTkLabel(master=padEffectsFrame4, text="Stacks / Infernus:")
specInfernusEntry = ctk.CTkEntry(master=padEffectsFrame4, width=g.boxWidth, corner_radius=0)
specInfernusCheckbox = ctk.CTkCheckBox(padEffectsFrame4, text="", width=10, corner_radius=0)

effectivenessImage = ctk.CTkLabel(master=padEffectsFrame4, image=g.pad4_red, text="")
effectivenessImage.grid(row=3, column=0, padx=10, pady=yspacing)
effectivenessLabel = ctk.CTkLabel(master=padEffectsFrame4, text="Effectiveness")
effectivenessLabel.grid(row=3, column=1, padx=0, pady=yspacing, sticky="w")
effectivenessOutputLabel = ctk.CTkLabel(master=padEffectsFrame4, text="")
effectivenessOutputLabel.grid(row=3, column=2, padx=10, pady=yspacing, sticky="w")

# Pad 6 frame
padEffectsFrame5 = ctk.CTkFrame(master=column1Frame, width=frameWidth, corner_radius=0)
padEffectsFrame5.grid(row=4, column=1, padx=10, pady=(5,10), sticky="nsew")
padEffectsFrame5.grid_columnconfigure(0, weight=0)
padEffectsFrame5.grid_columnconfigure(1, weight=column1Weight)
padEffectsFrame5.grid_columnconfigure(2, weight=0, minsize=100)

disintegrateLabel = ctk.CTkLabel(master=padEffectsFrame5, text="Balance of Power", font=subtitleFont)
disintegrateLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=yspacing)

hpNeededImage = ctk.CTkLabel(master=padEffectsFrame5, image=g.maxhp, text="")
hpNeededImage.grid(row=1, column=0, padx=10, pady=yspacing)
hpNeededLabel = ctk.CTkLabel(master=padEffectsFrame5, text="Hp needed")
hpNeededLabel.grid(row=1, column=1, padx=0, pady=yspacing, sticky="w")
hpNeededOutputLabel = ctk.CTkLabel(master=padEffectsFrame5, text="")
hpNeededOutputLabel.grid(row=1, column=2, padx=5, pady=yspacing, sticky="w")

pad6buffImage = ctk.CTkLabel(master=padEffectsFrame5, image=g.pad6_green, text="")
pad6buffImage.grid(row=2, column=0, padx=10, pady=yspacing)
pad6buffLabel = ctk.CTkLabel(master=padEffectsFrame5, text="Damage bonus")
pad6buffLabel.grid(row=2, column=1, padx=0, pady=yspacing, sticky="w")
pad6buffOutputLabel = ctk.CTkLabel(master=padEffectsFrame5, text="")
pad6buffOutputLabel.grid(row=2, column=2, padx=5, pady=yspacing, sticky="w")

pad6debuffImage = ctk.CTkLabel(master=padEffectsFrame5, image=g.pad2_red, text="")
pad6debuffImage.grid(row=3, column=0, padx=10, pady=yspacing)
pad6debuffLabel = ctk.CTkLabel(master=padEffectsFrame5, text="Healing reduction")
pad6debuffLabel.grid(row=3, column=1, padx=0, pady=yspacing, sticky="w")
pad6debuffOutputLabel = ctk.CTkLabel(master=padEffectsFrame5, text="")
pad6debuffOutputLabel.grid(row=3, column=2, padx=5, pady=yspacing, sticky="w")


#column=2 frame
# optionsFrame = ctk.CTkFrame(master=reflectOutputFrame, corner_radius=0, fg_color="#2b2b2b")
# optionsFrame.grid(row=0, column=6, rowspan=11, padx=0, pady=(10,0), sticky="ns")

column2frame = ctk.CTkFrame(master=root, corner_radius=0)
column2frame.grid(row=0, column=3, padx=5, pady=10, sticky="nsw")

# Dmg received output frame (column=2)
dmgOutputFrame = ctk.CTkFrame(master=column2frame, width=1000, corner_radius=0)
dmgOutputFrame.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")
dmgOutputFrame.grid_columnconfigure(0, weight=0)
dmgOutputFrame.grid_columnconfigure(1, weight=0, minsize=75)
dmgOutputFrame.grid_columnconfigure(2, weight=0, minsize=75)
dmgOutputFrame.grid_columnconfigure(3, weight=0, minsize=75)

magicDmgImage = ctk.CTkLabel(master=dmgOutputFrame, image=g.magicIcon, text="")
rangedDmgImage = ctk.CTkLabel(master=dmgOutputFrame, image=g.rangeIcon, text="")
slamDmgImage = ctk.CTkLabel(master=dmgOutputFrame, image=g.meleeIcon, text="")
infernusDmgImage = ctk.CTkLabel(master=dmgOutputFrame, image=g.choke, text="")
smokeDmgImage = ctk.CTkLabel(master=dmgOutputFrame, image=g.smoke, text="")
tombDmgImage = ctk.CTkLabel(master=dmgOutputFrame, image=g.tomb, text="")
decimationDmgImage = ctk.CTkLabel(master=dmgOutputFrame, image=g.decimation, text="")
cageDmgImage = ctk.CTkLabel(master=dmgOutputFrame, image=g.cageIcon, text="")
nukeDmgImage = ctk.CTkLabel(master=dmgOutputFrame, image=g.redbar, text="")
smallDmgImage = ctk.CTkLabel(master=dmgOutputFrame, image=g.smallIcon, text="")

subtitlesDLabel = ctk.CTkLabel(master=dmgOutputFrame, text="Damage taken", font=titleFont)
dmgtypeDLabel = ctk.CTkLabel(master=dmgOutputFrame, text="Damage type", font=subtitleFont)
magicDmgLabel = ctk.CTkLabel(master=dmgOutputFrame, text="Magic auto", font=subtitleFont)
rangedDmgLabel = ctk.CTkLabel(master=dmgOutputFrame, text="Ranged auto", font=subtitleFont)
slamDmgLabel = ctk.CTkLabel(master=dmgOutputFrame, text="Melee slam", font=subtitleFont)
infernusDmgLabel = ctk.CTkLabel(master=dmgOutputFrame, text="Infernus", font=subtitleFont)
smokeDmgLabel = ctk.CTkLabel(master=dmgOutputFrame, text="Flames of Zamorak", font=subtitleFont)
tombDmgLabel = ctk.CTkLabel(master=dmgOutputFrame, text="Tomb", font=subtitleFont)
deciDmgLabel = ctk.CTkLabel(master=dmgOutputFrame, text="Decimation", font=subtitleFont)
cageDmgLabel = ctk.CTkLabel(master=dmgOutputFrame, text="Cage", font=subtitleFont)
nukeDmgLabel = ctk.CTkLabel(master=dmgOutputFrame, text="Chaos damage", font=subtitleFont)
smallDmgLabel = ctk.CTkLabel(master=dmgOutputFrame, text="Small bombs", font=subtitleFont)

minDLabel = ctk.CTkLabel(master=dmgOutputFrame, text="Min", font=subtitleFont)
mageMinDmgOutputLabel = ctk.CTkLabel(master=dmgOutputFrame, text="", font=textFont)
rangeMinDmgOutputLabel = ctk.CTkLabel(master=dmgOutputFrame, text="", font=textFont)
infernusMinDmgOutputLabel = ctk.CTkLabel(master=dmgOutputFrame, text="", font=textFont)
chaosMinDmgOutputLabel = ctk.CTkLabel(master=dmgOutputFrame, text="", font=textFont)

maxDLabel = ctk.CTkLabel(master=dmgOutputFrame, text="Max", font=subtitleFont)
mageMaxDmgOutputLabel = ctk.CTkLabel(master=dmgOutputFrame, text="", font=textFont)
rangeMaxDmgOutputLabel = ctk.CTkLabel(master=dmgOutputFrame, text="", font=textFont)
infernusMaxDmgOutputLabel = ctk.CTkLabel(master=dmgOutputFrame, text="", font=textFont)
chaosMaxDmgOutputLabel = ctk.CTkLabel(master=dmgOutputFrame, text="", font=textFont)

avgDLabel = ctk.CTkLabel(master=dmgOutputFrame, text="Avg / Fixed", font=subtitleFont)
mageAvgDmgOutputLabel = ctk.CTkLabel(master=dmgOutputFrame, text="", font=textFont)
rangeAvgDmgOutputLabel = ctk.CTkLabel(master=dmgOutputFrame, text="", font=textFont)
slam1FixedDmgOutputLabel = ctk.CTkLabel(master=dmgOutputFrame, text="", font=textFont)
infernusAvgDmgOutputLabel = ctk.CTkLabel(master=dmgOutputFrame, text="", font=textFont)
smokeFixedDmgOutputLabel = ctk.CTkLabel(master=dmgOutputFrame, text="", font=textFont)
tombFixedDmgOutputLabel = ctk.CTkLabel(master=dmgOutputFrame, text="", font=textFont)
decimationFixedDmgOutputLabel = ctk.CTkLabel(master=dmgOutputFrame, text="", font=textFont)
cageFixedDmgOutputLabel = ctk.CTkLabel(master=dmgOutputFrame, text="", font=textFont)
chaosAvgDmgOutputLabel = ctk.CTkLabel(master=dmgOutputFrame, text="", font=textFont)
smallFixedDmgOutputLabel = ctk.CTkLabel(master=dmgOutputFrame, text="", font=textFont)

tsDLabel = ctk.CTkLabel(master=dmgOutputFrame, text="Twinshot (2nd hits)", font=subtitleFont)
mageTsDmgOutputLabel = ctk.CTkLabel(master=dmgOutputFrame, text="", font=textFont)
rangeTsDmgOutputLabel = ctk.CTkLabel(master=dmgOutputFrame, text="", font=textFont)
slam2FixedDmgOutputLabel = ctk.CTkLabel(master=dmgOutputFrame, text="", font=textFont)
smallTsDmgOutputLabel = ctk.CTkLabel(master=dmgOutputFrame, text="", font=textFont)

imageXPadding = (10,5)
dmgXpadding = 5
dmgYpadding = 0

magicDmgImage.grid(row=2, column=0, padx=imageXPadding, pady=dmgYpadding, sticky="w")
rangedDmgImage.grid(row=3, column=0, padx=imageXPadding, pady=dmgYpadding, sticky="w")
slamDmgImage.grid(row=4, column=0, padx=imageXPadding, pady=dmgYpadding, sticky="w")
infernusDmgImage.grid(row=5, column=0, padx=imageXPadding, pady=dmgYpadding, sticky="w")
smokeDmgImage.grid(row=6, column=0, padx=imageXPadding, pady=dmgYpadding, sticky="w")
tombDmgImage.grid(row=7, column=0, padx=imageXPadding, pady=dmgYpadding, sticky="w")
decimationDmgImage.grid(row=8, column=0, padx=imageXPadding, pady=dmgYpadding, sticky="w")
cageDmgImage.grid(row=9, column=0, padx=imageXPadding, pady=dmgYpadding, sticky="w")
nukeDmgImage.grid(row=10, column=0, padx=imageXPadding, pady=dmgYpadding, sticky="w")
smallDmgImage.grid(row=11, column=0, padx=imageXPadding, pady=dmgYpadding, sticky="w")

subtitlesDLabel.grid(row=0, column=0, columnspan=6)
# dmgtypeDLabel.grid(row=1, column=0, columnspan=2, padx=dmgXpadding, pady=dmgYpadding)
magicDmgLabel.grid(row=2, column=1, padx=dmgXpadding, pady=dmgYpadding, sticky="w")
rangedDmgLabel.grid(row=3, column=1, padx=dmgXpadding, pady=dmgYpadding, sticky="w")
slamDmgLabel.grid(row=4, column=1, padx=dmgXpadding, pady=dmgYpadding, sticky="w")
infernusDmgLabel.grid(row=5, column=1, padx=dmgXpadding, pady=dmgYpadding, sticky="w")
smokeDmgLabel.grid(row=6, column=1, padx=dmgXpadding, pady=dmgYpadding, sticky="w")
tombDmgLabel.grid(row=7, column=1, padx=dmgXpadding, pady=dmgYpadding, sticky="w")
deciDmgLabel.grid(row=8, column=1, padx=dmgXpadding, pady=dmgYpadding, sticky="w")
cageDmgLabel.grid(row=9, column=1, padx=dmgXpadding, pady=dmgYpadding, sticky="w")
nukeDmgLabel.grid(row=10, column=1, padx=dmgXpadding, pady=dmgYpadding, sticky="w")
smallDmgLabel.grid(row=11, column=1, padx=dmgXpadding, pady=dmgYpadding, sticky="w")

minDLabel.grid(row=1, column=2, padx=dmgXpadding, pady=dmgYpadding)
mageMinDmgOutputLabel.grid(row=2, column=2, padx=dmgXpadding, pady=dmgYpadding)
rangeMinDmgOutputLabel.grid(row=3, column=2, padx=dmgXpadding, pady=dmgYpadding)
infernusMinDmgOutputLabel.grid(row=5, column=2, padx=dmgXpadding, pady=dmgYpadding)
chaosMinDmgOutputLabel.grid(row=10, column=2, padx=dmgXpadding, pady=dmgYpadding)

maxDLabel.grid(row=1, column=3, padx=dmgXpadding, pady=dmgYpadding)
mageMaxDmgOutputLabel.grid(row=2, column=3, padx=dmgXpadding, pady=dmgYpadding)
rangeMaxDmgOutputLabel.grid(row=3, column=3, padx=dmgXpadding, pady=dmgYpadding)
infernusMaxDmgOutputLabel.grid(row=5, column=3, padx=dmgXpadding, pady=dmgYpadding)
chaosMaxDmgOutputLabel.grid(row=10, column=3, padx=dmgXpadding, pady=dmgYpadding)

avgDLabel.grid(row=1, column=4, padx=dmgXpadding, pady=dmgYpadding)
mageAvgDmgOutputLabel.grid(row=2, column=4, padx=dmgXpadding, pady=dmgYpadding)
rangeAvgDmgOutputLabel.grid(row=3, column=4, padx=dmgXpadding, pady=dmgYpadding)
slam1FixedDmgOutputLabel.grid(row=4, column=4, padx=dmgXpadding, pady=dmgYpadding)
infernusAvgDmgOutputLabel.grid(row=5, column=4, padx=dmgXpadding, pady=dmgYpadding)
smokeFixedDmgOutputLabel.grid(row=6, column=4, padx=dmgXpadding, pady=dmgYpadding)
tombFixedDmgOutputLabel.grid(row=7, column=4, padx=dmgXpadding, pady=dmgYpadding)
decimationFixedDmgOutputLabel.grid(row=8, column=4, padx=dmgXpadding, pady=dmgYpadding)
cageFixedDmgOutputLabel.grid(row=9, column=4, padx=dmgXpadding, pady=dmgYpadding)
chaosAvgDmgOutputLabel.grid(row=10, column=4, padx=dmgXpadding, pady=dmgYpadding)
smallFixedDmgOutputLabel.grid(row=11, column=4, padx=dmgXpadding, pady=dmgYpadding)

tsDLabel.grid(row=1, column=5, padx=dmgXpadding, pady=dmgYpadding)
mageTsDmgOutputLabel.grid(row=2, column=5, padx=dmgXpadding, pady=dmgYpadding)
rangeTsDmgOutputLabel.grid(row=3, column=5, padx=dmgXpadding, pady=dmgYpadding)
slam2FixedDmgOutputLabel.grid(row=4, column=5, padx=dmgXpadding, pady=dmgYpadding)
smallTsDmgOutputLabel.grid(row=11, column=5, padx=dmgXpadding, pady=dmgYpadding)


# Healing/divert output frame (column=2)
healingOutputFrame = ctk.CTkFrame(master=column2frame, width=1000, corner_radius=0)
healingOutputFrame.grid(row=1, column=2, padx=10, pady=0, sticky="nsew")
healingOutputFrame.grid_columnconfigure(0, weight=0)
healingOutputFrame.grid_columnconfigure(1, weight=0, minsize=75)
healingOutputFrame.grid_columnconfigure(2, weight=0, minsize=75)
healingOutputFrame.grid_columnconfigure(3, weight=0, minsize=75)

magicHealImage = ctk.CTkLabel(master=healingOutputFrame, image=g.magicIcon, text="")
rangedHealImage = ctk.CTkLabel(master=healingOutputFrame, image=g.rangeIcon, text="")
slamHealImage = ctk.CTkLabel(master=healingOutputFrame, image=g.meleeIcon, text="")
smokeHealImage = ctk.CTkLabel(master=healingOutputFrame, image=g.smoke, text="")
tombHealImage = ctk.CTkLabel(master=healingOutputFrame, image=g.tomb, text="")
decimationHealImage = ctk.CTkLabel(master=healingOutputFrame, image=g.decimation, text="")
cageHealImage = ctk.CTkLabel(master=healingOutputFrame, image=g.cageIcon, text="")
nukeHealImage = ctk.CTkLabel(master=healingOutputFrame, image=g.redbar, text="")
smallHealImage = ctk.CTkLabel(master=healingOutputFrame, image=g.smallIcon, text="")

subtitleHLabel = ctk.CTkLabel(master=healingOutputFrame, text="Healing / Adren gain", font=titleFont)
dmgtypeHLabel = ctk.CTkLabel(master=healingOutputFrame, text="Damage type", font=subtitleFont)
magicHealLabel = ctk.CTkLabel(master=healingOutputFrame, text="Magic auto", font=subtitleFont)
rangedHealLabel = ctk.CTkLabel(master=healingOutputFrame, text="Ranged auto", font=subtitleFont)
slamHealLabel = ctk.CTkLabel(master=healingOutputFrame, text="Melee slam", font=subtitleFont)
smokeHealLabel = ctk.CTkLabel(master=healingOutputFrame, text="Flames of Zamorak", font=subtitleFont)
tombHealLabel = ctk.CTkLabel(master=healingOutputFrame, text="Tomb", font=subtitleFont)
deciHealLabel = ctk.CTkLabel(master=healingOutputFrame, text="Decimation", font=subtitleFont)
cageHealLabel = ctk.CTkLabel(master=healingOutputFrame, text="Cage", font=subtitleFont)
nukeHealLabel = ctk.CTkLabel(master=healingOutputFrame, text="Chaos damage", font=subtitleFont)
smallHealLabel = ctk.CTkLabel(master=healingOutputFrame, text="Small bombs", font=subtitleFont)

minHLabel = ctk.CTkLabel(master=healingOutputFrame, text="Min", font=subtitleFont)
mageMinHealOutputLabel = ctk.CTkLabel(master=healingOutputFrame, text="", font=textFont)
rangeMinHealOutputLabel = ctk.CTkLabel(master=healingOutputFrame, text="", font=textFont)
chaosMinHealOutputLabel = ctk.CTkLabel(master=healingOutputFrame, text="", font=textFont)

maxHLabel = ctk.CTkLabel(master=healingOutputFrame, text="Max", font=subtitleFont)
mageMaxHealOutputLabel = ctk.CTkLabel(master=healingOutputFrame, text="", font=textFont)
rangeMaxHealOutputLabel = ctk.CTkLabel(master=healingOutputFrame, text="", font=textFont)
chaosMaxHealOutputLabel = ctk.CTkLabel(master=healingOutputFrame, text="", font=textFont)

avgHLabel = ctk.CTkLabel(master=healingOutputFrame, text="Avg / Fixed", font=subtitleFont)
mageAvgHealOutputLabel = ctk.CTkLabel(master=healingOutputFrame, text="", font=textFont)
rangeAvgHealOutputLabel = ctk.CTkLabel(master=healingOutputFrame, text="", font=textFont)
slam1FixedHealOutputLabel = ctk.CTkLabel(master=healingOutputFrame, text="", font=textFont)
smokeFixedHealOutputLabel = ctk.CTkLabel(master=healingOutputFrame, text="", font=textFont)
tombFixedHealOutputLabel = ctk.CTkLabel(master=healingOutputFrame, text="", font=textFont)
decimationFixedHealOutputLabel = ctk.CTkLabel(master=healingOutputFrame, text="", font=textFont)
cageFixedHealOutputLabel = ctk.CTkLabel(master=healingOutputFrame, text="", font=textFont)
chaosAvgHealOutputLabel = ctk.CTkLabel(master=healingOutputFrame, text="", font=textFont)
smallFixedHealOutputLabel = ctk.CTkLabel(master=healingOutputFrame, text="", font=textFont)

tsHLabel = ctk.CTkLabel(master=healingOutputFrame, text="Twinshot (2nd hits)", font=subtitleFont)
mageTsHealOutputLabel = ctk.CTkLabel(master=healingOutputFrame, text="", font=textFont)
rangeTsHealOutputLabel = ctk.CTkLabel(master=healingOutputFrame, text="", font=textFont)
slam2FixedHealOutputLabel = ctk.CTkLabel(master=healingOutputFrame, text="", font=textFont)
smallTsHealOutputLabel = ctk.CTkLabel(master=healingOutputFrame, text="", font=textFont)

magicHealImage.grid(row=2, column=0, padx=imageXPadding, pady=dmgYpadding, sticky="w")
rangedHealImage.grid(row=3, column=0, padx=imageXPadding, pady=dmgYpadding, sticky="w")
slamHealImage.grid(row=4, column=0, padx=imageXPadding, pady=dmgYpadding, sticky="w")
smokeHealImage.grid(row=6, column=0, padx=imageXPadding, pady=dmgYpadding, sticky="w")
tombHealImage.grid(row=7, column=0, padx=imageXPadding, pady=dmgYpadding, sticky="w")
decimationHealImage.grid(row=8, column=0, padx=imageXPadding, pady=dmgYpadding, sticky="w")
cageHealImage.grid(row=9, column=0, padx=imageXPadding, pady=dmgYpadding, sticky="w")
nukeHealImage.grid(row=10, column=0, padx=imageXPadding, pady=dmgYpadding, sticky="w")
smallHealImage.grid(row=11, column=0, padx=imageXPadding, pady=dmgYpadding, sticky="w")

subtitleHLabel.grid(row=0, column=0, columnspan=6)
# dmgtypeHLabel.grid(row=1, column=0, columnspan=2, padx=dmgXpadding, pady=dmgYpadding)
magicHealLabel.grid(row=2, column=1, padx=dmgXpadding, pady=dmgYpadding, sticky="w")
rangedHealLabel.grid(row=3, column=1, padx=dmgXpadding, pady=dmgYpadding, sticky="w")
slamHealLabel.grid(row=4, column=1, padx=dmgXpadding, pady=dmgYpadding, sticky="w")
smokeHealLabel.grid(row=6, column=1, padx=dmgXpadding, pady=dmgYpadding, sticky="w")
tombHealLabel.grid(row=7, column=1, padx=dmgXpadding, pady=dmgYpadding, sticky="w")
deciHealLabel.grid(row=8, column=1, padx=dmgXpadding, pady=dmgYpadding, sticky="w")
cageHealLabel.grid(row=9, column=1, padx=dmgXpadding, pady=dmgYpadding, sticky="w")
nukeHealLabel.grid(row=10, column=1, padx=dmgXpadding, pady=dmgYpadding, sticky="w")
smallHealLabel.grid(row=11, column=1, padx=dmgXpadding, pady=dmgYpadding, sticky="w")

minHLabel.grid(row=1, column=2, padx=dmgXpadding, pady=dmgYpadding)
mageMinHealOutputLabel.grid(row=2, column=2, padx=dmgXpadding, pady=dmgYpadding)
rangeMinHealOutputLabel.grid(row=3, column=2, padx=dmgXpadding, pady=dmgYpadding)
chaosMinHealOutputLabel.grid(row=10, column=2, padx=dmgXpadding, pady=dmgYpadding)

maxHLabel.grid(row=1, column=3, padx=dmgXpadding, pady=dmgYpadding)
mageMaxHealOutputLabel.grid(row=2, column=3, padx=dmgXpadding, pady=dmgYpadding)
rangeMaxHealOutputLabel.grid(row=3, column=3, padx=dmgXpadding, pady=dmgYpadding)
chaosMaxHealOutputLabel.grid(row=10, column=3, padx=dmgXpadding, pady=dmgYpadding)

avgHLabel.grid(row=1, column=4, padx=dmgXpadding, pady=dmgYpadding)
mageAvgHealOutputLabel.grid(row=2, column=4, padx=dmgXpadding, pady=dmgYpadding)
rangeAvgHealOutputLabel.grid(row=3, column=4, padx=dmgXpadding, pady=dmgYpadding)
slam1FixedHealOutputLabel.grid(row=4, column=4, padx=dmgXpadding, pady=dmgYpadding)
smokeFixedHealOutputLabel.grid(row=6, column=4, padx=dmgXpadding, pady=dmgYpadding)
tombFixedHealOutputLabel.grid(row=7, column=4, padx=dmgXpadding, pady=dmgYpadding)
decimationFixedHealOutputLabel.grid(row=8, column=4, padx=dmgXpadding, pady=dmgYpadding)
cageFixedHealOutputLabel.grid(row=9, column=4, padx=dmgXpadding, pady=dmgYpadding)
chaosAvgHealOutputLabel.grid(row=10, column=4, padx=dmgXpadding, pady=dmgYpadding)
smallFixedHealOutputLabel.grid(row=11, column=4, padx=dmgXpadding, pady=dmgYpadding)

tsHLabel.grid(row=1, column=5, padx=dmgXpadding, pady=dmgYpadding)
mageTsHealOutputLabel.grid(row=2, column=5, padx=dmgXpadding, pady=dmgYpadding)
rangeTsHealOutputLabel.grid(row=3, column=5, padx=dmgXpadding, pady=dmgYpadding)
slam2FixedHealOutputLabel.grid(row=4, column=5, padx=dmgXpadding, pady=dmgYpadding)
smallTsHealOutputLabel.grid(row=11, column=5, padx=dmgXpadding, pady=dmgYpadding)


# Dmg reflected (refl) output frame
reflectOutputFrame = ctk.CTkFrame(master=column2frame, width=1000, corner_radius=0)
reflectOutputFrame.grid(row=2, column=2, padx=10, pady=10, sticky="nsew")
reflectOutputFrame.grid_columnconfigure(0, weight=0)
reflectOutputFrame.grid_columnconfigure(1, weight=0, minsize=75)
reflectOutputFrame.grid_columnconfigure(2, weight=0, minsize=75)
reflectOutputFrame.grid_columnconfigure(3, weight=0, minsize=75)

magicReflImage = ctk.CTkLabel(master=reflectOutputFrame, image=g.magicIcon, text="")
rangedReflImage = ctk.CTkLabel(master=reflectOutputFrame, image=g.rangeIcon, text="")
slamReflImage = ctk.CTkLabel(master=reflectOutputFrame, image=g.meleeIcon, text="")
smokeReflImage = ctk.CTkLabel(master=reflectOutputFrame, image=g.smoke, text="")
tombReflImage = ctk.CTkLabel(master=reflectOutputFrame, image=g.tomb, text="")
decimationReflImage = ctk.CTkLabel(master=reflectOutputFrame, image=g.decimation, text="")
cageReflImage = ctk.CTkLabel(master=reflectOutputFrame, image=g.cageIcon, text="")
nukeReflImage = ctk.CTkLabel(master=reflectOutputFrame, image=g.redbar, text="")
smallReflImage = ctk.CTkLabel(master=reflectOutputFrame, image=g.smallIcon, text="")

subtitleRLabel = ctk.CTkLabel(master=reflectOutputFrame, text="Reflect damage", font=titleFont)
dmgtypeRLabel = ctk.CTkLabel(master=reflectOutputFrame, text="Damage type", font=subtitleFont)
magicReflLabel = ctk.CTkLabel(master=reflectOutputFrame, text="Magic auto", font=subtitleFont)
rangedReflLabel = ctk.CTkLabel(master=reflectOutputFrame, text="Ranged auto", font=subtitleFont)
slamReflLabel = ctk.CTkLabel(master=reflectOutputFrame, text="Melee slam", font=subtitleFont)
smokeReflLabel = ctk.CTkLabel(master=reflectOutputFrame, text="Flames of Zamorak", font=subtitleFont)
tombReflLabel = ctk.CTkLabel(master=reflectOutputFrame, text="Tomb", font=subtitleFont)
deciReflLabel = ctk.CTkLabel(master=reflectOutputFrame, text="Decimation", font=subtitleFont)
cageReflLabel = ctk.CTkLabel(master=reflectOutputFrame, text="Cage", font=subtitleFont)
nukeReflLabel = ctk.CTkLabel(master=reflectOutputFrame, text="Chaos damage", font=subtitleFont)
smallReflLabel = ctk.CTkLabel(master=reflectOutputFrame, text="Small bombs", font=subtitleFont)

minRLabel = ctk.CTkLabel(master=reflectOutputFrame, text="Min", font=subtitleFont)
mageMinReflOutputLabel = ctk.CTkLabel(master=reflectOutputFrame, text="", font=textFont)
rangeMinReflOutputLabel = ctk.CTkLabel(master=reflectOutputFrame, text="", font=textFont)
chaosMinReflOutputLabel = ctk.CTkLabel(master=reflectOutputFrame, text="", font=textFont)

maxRLabel = ctk.CTkLabel(master=reflectOutputFrame, text="Max", font=subtitleFont)
mageMaxReflOutputLabel = ctk.CTkLabel(master=reflectOutputFrame, text="", font=textFont)
rangeMaxReflOutputLabel = ctk.CTkLabel(master=reflectOutputFrame, text="", font=textFont)
chaosMaxReflOutputLabel = ctk.CTkLabel(master=reflectOutputFrame, text="", font=textFont)

avgRLabel = ctk.CTkLabel(master=reflectOutputFrame, text="Avg / Fixed", font=subtitleFont)
mageAvgReflOutputLabel = ctk.CTkLabel(master=reflectOutputFrame, text="", font=textFont)
rangeAvgReflOutputLabel = ctk.CTkLabel(master=reflectOutputFrame, text="", font=textFont)
slam1FixedReflOutputLabel = ctk.CTkLabel(master=reflectOutputFrame, text="", font=textFont)
smokeFixedReflOutputLabel = ctk.CTkLabel(master=reflectOutputFrame, text="", font=textFont)
tombFixedReflOutputLabel = ctk.CTkLabel(master=reflectOutputFrame, text="", font=textFont)
decimationFixedReflOutputLabel = ctk.CTkLabel(master=reflectOutputFrame, text="", font=textFont)
cageFixedReflOutputLabel = ctk.CTkLabel(master=reflectOutputFrame, text="", font=textFont)
chaosAvgReflOutputLabel  = ctk.CTkLabel(master=reflectOutputFrame, text="", font=textFont)
smallFixedReflOutputLabel = ctk.CTkLabel(master=reflectOutputFrame, text="", font=textFont)

tsRLabel = ctk.CTkLabel(master=reflectOutputFrame, text="Twinshot (2nd hits)", font=subtitleFont)
mageTsReflOutputLabel = ctk.CTkLabel(master=reflectOutputFrame, text="", font=textFont)
rangeTsReflOutputLabel = ctk.CTkLabel(master=reflectOutputFrame, text="", font=textFont)
slam2FixedReflOutputLabel = ctk.CTkLabel(master=reflectOutputFrame, text="", font=textFont)
smallTsReflOutputLabel = ctk.CTkLabel(master=reflectOutputFrame, text="", font=textFont)

magicReflImage.grid(row=2, column=0, padx=imageXPadding, pady=dmgYpadding, sticky="w")
rangedReflImage.grid(row=3, column=0, padx=imageXPadding, pady=dmgYpadding, sticky="w")
slamReflImage.grid(row=4, column=0, padx=imageXPadding, pady=dmgYpadding, sticky="w")
smokeReflImage.grid(row=6, column=0, padx=imageXPadding, pady=dmgYpadding, sticky="w")
tombReflImage.grid(row=7, column=0, padx=imageXPadding, pady=dmgYpadding, sticky="w")
decimationReflImage.grid(row=8, column=0, padx=imageXPadding, pady=dmgYpadding, sticky="w")
cageReflImage.grid(row=9, column=0, padx=imageXPadding, pady=dmgYpadding, sticky="w")
nukeReflImage.grid(row=10, column=0, padx=imageXPadding, pady=dmgYpadding, sticky="w")
smallReflImage.grid(row=11, column=0, padx=imageXPadding, pady=dmgYpadding, sticky="w")

subtitleRLabel.grid(row=0, column=0, columnspan=6)
# dmgtypeRLabel.grid(row=1, column=0, columnspan=2, padx=dmgXpadding, pady=dmgYpadding)
magicReflLabel.grid(row=2, column=1, padx=dmgXpadding, pady=dmgYpadding, sticky="w")
rangedReflLabel.grid(row=3, column=1, padx=dmgXpadding, pady=dmgYpadding, sticky="w")
slamReflLabel.grid(row=4, column=1, padx=dmgXpadding, pady=dmgYpadding, sticky="w")
smokeReflLabel.grid(row=6, column=1, padx=dmgXpadding, pady=dmgYpadding, sticky="w")
tombReflLabel.grid(row=7, column=1, padx=dmgXpadding, pady=dmgYpadding, sticky="w")
deciReflLabel.grid(row=8, column=1, padx=dmgXpadding, pady=dmgYpadding, sticky="w")
cageReflLabel.grid(row=9, column=1, padx=dmgXpadding, pady=dmgYpadding, sticky="w")
nukeReflLabel.grid(row=10, column=1, padx=dmgXpadding, pady=dmgYpadding, sticky="w")
smallReflLabel.grid(row=11, column=1, padx=dmgXpadding, pady=dmgYpadding, sticky="w")

minRLabel.grid(row=1, column=2, padx=dmgXpadding, pady=dmgYpadding)
mageMinReflOutputLabel.grid(row=2, column=2, padx=dmgXpadding, pady=dmgYpadding)
rangeMinReflOutputLabel.grid(row=3, column=2, padx=dmgXpadding, pady=dmgYpadding)
chaosMinReflOutputLabel.grid(row=10, column=2, padx=dmgXpadding, pady=dmgYpadding)

maxRLabel.grid(row=1, column=3, padx=dmgXpadding, pady=dmgYpadding)
mageMaxReflOutputLabel.grid(row=2, column=3, padx=dmgXpadding, pady=dmgYpadding)
rangeMaxReflOutputLabel.grid(row=3, column=3, padx=dmgXpadding, pady=dmgYpadding)
chaosMaxReflOutputLabel.grid(row=10, column=3, padx=dmgXpadding, pady=dmgYpadding)

avgRLabel.grid(row=1, column=4, padx=dmgXpadding, pady=dmgYpadding)
mageAvgReflOutputLabel.grid(row=2, column=4, padx=dmgXpadding, pady=dmgYpadding)
rangeAvgReflOutputLabel.grid(row=3, column=4, padx=dmgXpadding, pady=dmgYpadding)
slam1FixedReflOutputLabel.grid(row=4, column=4, padx=dmgXpadding, pady=dmgYpadding)
smokeFixedReflOutputLabel.grid(row=6, column=4, padx=dmgXpadding, pady=dmgYpadding)
tombFixedReflOutputLabel.grid(row=7, column=4, padx=dmgXpadding, pady=dmgYpadding)
decimationFixedReflOutputLabel.grid(row=8, column=4, padx=dmgXpadding, pady=dmgYpadding)
cageFixedReflOutputLabel.grid(row=9, column=4, padx=dmgXpadding, pady=dmgYpadding)
chaosAvgReflOutputLabel.grid(row=10, column=4, padx=dmgXpadding, pady=dmgYpadding)
smallFixedReflOutputLabel.grid(row=11, column=4, padx=dmgXpadding, pady=dmgYpadding)

tsRLabel.grid(row=1, column=5, padx=dmgXpadding, pady=dmgYpadding)
mageTsReflOutputLabel.grid(row=2, column=5, padx=dmgXpadding, pady=dmgYpadding)
rangeTsReflOutputLabel.grid(row=3, column=5, padx=dmgXpadding, pady=dmgYpadding)
slam2FixedReflOutputLabel.grid(row=4, column=5, padx=dmgXpadding, pady=dmgYpadding)
smallTsReflOutputLabel.grid(row=11, column=5, padx=dmgXpadding, pady=dmgYpadding)


startupSettings()
infernusCallback()
g.commandUpdate()

def closingWindow():
    saveSettings(variables)
    root.destroy()

root.protocol("WM_DELETE_WINDOW", closingWindow)
