import numpy as np
import customtkinter as ctk
from PIL import Image

digitMenuWidth = 80

# green, blue, pink, cyan 
theme = "light"
color = "cyan"

if theme == "dark":
    frameBg = "#333333"
else:
    frameBg = "#cfcfcf"

ctk.set_appearance_mode(theme)
ctk.set_default_color_theme(color)

root = ctk.CTk()
root.title("Zamorak calculator")
root.iconbitmap("icons/zam.ico")
# root.geometry("1920x1080")
# root.geometry("1240, 1080")
# root.attributes("zoomed", True)

appWidth = 1240
appHeight = 1080
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
xPos = (screenWidth // 2) - (appWidth // 2)
yPos = (screenHeight // 2) - (appHeight // 2)
root.geometry(f"{appWidth}x{appHeight}+{xPos}+{yPos}")


# root.after(0, lambda:root.state('zoomed'))
# root.resizable(width=True, height=True)

root.grid_columnconfigure(0, weight=0)
root.grid_columnconfigure(1, weight=0)
root.grid_columnconfigure(2, weight=0)
root.grid_columnconfigure(3, weight=1)
root.grid_rowconfigure(0, weight=0)
root.grid_rowconfigure(1, weight=0)
root.grid_rowconfigure(2, weight=0)
root.grid_rowconfigure(3, weight=0)
root.grid_rowconfigure(4, weight=0)


def loadImage(path, output):
    image = Image.open(path).convert("RGBA")
    
    arrayImage = np.array(image)
    imageHeight = len(arrayImage[:,0,0])
    imageWidth = len(arrayImage[0,:,0])
    
    if imageHeight > imageWidth:
        ratio = imageWidth/imageHeight
        newHeight = 20
        newWidth = int(newHeight * ratio)
        
    elif imageWidth > imageHeight:
        ratio = imageHeight/imageWidth
        newWidth = 20
        newHeight = int(newWidth * ratio)
        
    else:
        newWidth = 20
        newHeight = 20
    
    image = image.resize((newWidth, newHeight))
    
    if output == "Image":
        return image
    else:
        return (newWidth, newHeight)


titleFont = ("Arial Greek", 14, 'bold')
subtitleFont = ("Arial Greek", 12, "bold")
textFont = ("Arial Greek", 12)


column1Frame = ctk.CTkFrame(master=root, corner_radius=0)
column1Frame.grid(row=0, column=1, padx=5, pady=10, sticky="nsew")

settingsTabs = ctk.CTkTabview(master=column1Frame, corner_radius=0)
settingsTabs.grid(row=0, column=0, padx=10, pady=0, sticky="nsew")
settingsTabs._segmented_button.configure(font=titleFont)

column1Frame.grid_rowconfigure(0, weight=0, minsize=790)

zamorakTab = settingsTabs.add("Zamorak settings")
playerTab = settingsTabs.add("Player settings")
modifiersTab = settingsTabs.add("Damage modifiers")

# Loading icons
#tab1
zam = ctk.CTkImage(dark_image=loadImage("icons/zam.png", "Image"), size=loadImage("icons/zam.png", "Size"))
pad1_red = ctk.CTkImage(dark_image=loadImage("icons/pad1_red.png", "Image"), size=loadImage("icons/pad1_red.png", "Size"))
pad2_red = ctk.CTkImage(dark_image=loadImage("icons/pad2_red.png", "Image"), size=loadImage("icons/pad2_red.png", "Size"))
pad3_green = ctk.CTkImage(dark_image=loadImage("icons/pad3_green.png", "Image"), size=loadImage("icons/pad3_green.png", "Size"))
pad4_red = ctk.CTkImage(dark_image=loadImage("icons/pad4_red.png", "Image"), size=loadImage("icons/pad4_red.png", "Size"))
pad5_green = ctk.CTkImage(dark_image=loadImage("icons/pad5_green.png", "Image"), size=loadImage("icons/pad5_green.png", "Size"))
pad6_green = ctk.CTkImage(dark_image=loadImage("icons/pad6_green.png", "Image"), size=loadImage("icons/pad6_green.png", "Size"))
choke = ctk.CTkImage(dark_image=loadImage("icons/choke.png", "Image"), size=loadImage("icons/choke.png", "Size"))
slam = ctk.CTkImage(dark_image=loadImage("icons/slam.png", "Image"), size=loadImage("icons/slam.png", "Size"))
smoke = ctk.CTkImage(dark_image=loadImage("icons/smoke.png", "Image"), size=loadImage("icons/smoke.png", "Size"))
tomb = ctk.CTkImage(dark_image=loadImage("icons/tomb.png", "Image"), size=loadImage("icons/tomb.png", "Size"))
decimation = ctk.CTkImage(dark_image=loadImage("icons/decimation.png", "Image"), size=loadImage("icons/decimation.png", "Size"))
aggro = ctk.CTkImage(dark_image=loadImage("icons/aggro.png", "Image"), size=loadImage("icons/aggro.png", "Size"))
charge = ctk.CTkImage(dark_image=loadImage("icons/charge.png", "Image"), size=loadImage("icons/charge.png", "Size"))
# iteration = ctk.CTkImage(dark_image=loadImage("icons/iteration.png", "Image"), size=loadImage("icons/iteration.png", "Size"))
redbar = ctk.CTkImage(dark_image=loadImage("icons/nuke.png", "Image"), size=loadImage("icons/nuke.png", "Size"))

#tab2
helm = ctk.CTkImage(dark_image=loadImage("icons/helm.png", "Image"), size=loadImage("icons/helm.png", "Size"))
top = ctk.CTkImage(dark_image=loadImage("icons/top.png", "Image"), size=loadImage("icons/top.png", "Size"))
bottoms = ctk.CTkImage(dark_image=loadImage("icons/bottoms.png", "Image"), size=loadImage("icons/bottoms.png", "Size"))
gloves = ctk.CTkImage(dark_image=loadImage("icons/gloves.png", "Image"), size=loadImage("icons/gloves.png", "Size"))
boots = ctk.CTkImage(dark_image=loadImage("icons/boots.png", "Image"), size=loadImage("icons/boots.png", "Size"))
shield = ctk.CTkImage(dark_image=loadImage("icons/shield.png", "Image"), size=loadImage("icons/shield.png", "Size"))
eof = ctk.CTkImage(dark_image=loadImage("icons/eof.png", "Image"), size=loadImage("icons/eof.png", "Size"))
ovl = ctk.CTkImage(dark_image=loadImage("icons/ovl.png", "Image"), size=loadImage("icons/ovl.png", "Size"))
defence = ctk.CTkImage(dark_image=loadImage("icons/def.png", "Image"), size=loadImage("icons/def.png", "Size"))
powder = ctk.CTkImage(dark_image=loadImage("icons/powder.png", "Image"), size=loadImage("icons/powder.png", "Size"))
ppoints = ctk.CTkImage(dark_image=loadImage("icons/ppoints.png", "Image"), size=loadImage("icons/ppoints.png", "Size"))
affliction = ctk.CTkImage(dark_image=loadImage("icons/affliction.png", "Image"), size=loadImage("icons/affliction.png", "Size"))
desolation = ctk.CTkImage(dark_image=loadImage("icons/desolation.png", "Image"), size=loadImage("icons/desolation.png", "Size"))
maxhp = ctk.CTkImage(dark_image=loadImage("icons/maxhp.png", "Image"), size=loadImage("icons/maxhp.png", "Size"))
currenthp = ctk.CTkImage(dark_image=loadImage("icons/currenthp.png", "Image"), size=loadImage("icons/currenthp.png", "Size"))
boneshield = ctk.CTkImage(dark_image=loadImage("icons/boneshield.png", "Image"), size=loadImage("icons/boneshield.png", "Size"))
totg = ctk.CTkImage(dark_image=loadImage("icons/totg.png", "Image"), size=loadImage("icons/totg.png", "Size"))
puzzlebox = ctk.CTkImage(dark_image=loadImage("icons/puzzlebox.png", "Image"), size=loadImage("icons/puzzlebox.png", "Size"))

#tab3
disr = ctk.CTkImage(dark_image=loadImage("icons/disr.png", "Image"), size=loadImage("icons/disr.png", "Size"))
cade = ctk.CTkImage(dark_image=loadImage("icons/cade.png", "Image"), size=loadImage("icons/cade.png", "Size"))
divert = ctk.CTkImage(dark_image=loadImage("icons/divert.png", "Image"), size=loadImage("icons/divert.png", "Size"))
refl = ctk.CTkImage(dark_image=loadImage("icons/refl.png", "Image"), size=loadImage("icons/refl.png", "Size"))
debil = ctk.CTkImage(dark_image=loadImage("icons/debil.png", "Image"), size=loadImage("icons/debil.png", "Size"))
sd = ctk.CTkImage(dark_image=loadImage("icons/sd.png", "Image"), size=loadImage("icons/sd.png", "Size"))
immort = ctk.CTkImage(dark_image=loadImage("icons/immort.png", "Image"), size=loadImage("icons/immort.png", "Size"))
anti = ctk.CTkImage(dark_image=loadImage("icons/anti.png", "Image"), size=loadImage("icons/anti.png", "Size"))
ful = ctk.CTkImage(dark_image=loadImage("icons/ful.png", "Image"), size=loadImage("icons/ful.png", "Size"))
aegis = ctk.CTkImage(dark_image=loadImage("icons/aegis.png", "Image"), size=loadImage("icons/aegis.png", "Size"))
zerk = ctk.CTkImage(dark_image=loadImage("icons/zerk.png", "Image"), size=loadImage("icons/zerk.png", "Size"))
pulv = ctk.CTkImage(dark_image=loadImage("icons/pulv.png", "Image"), size=loadImage("icons/pulv.png", "Size"))
sever = ctk.CTkImage(dark_image=loadImage("icons/sever.png", "Image"), size=loadImage("icons/sever.png", "Size"))
absorb = ctk.CTkImage(dark_image=loadImage("icons/absorb.png", "Image"), size=loadImage("icons/absorb.png", "Size"))
enfeeble = ctk.CTkImage(dark_image=loadImage("icons/enfeeble.png", "Image"), size=loadImage("icons/enfeeble.png", "Size"))
emerald = ctk.CTkImage(dark_image=loadImage("icons/emerald.png", "Image"), size=loadImage("icons/emerald.png", "Size"))
anchor = ctk.CTkImage(dark_image=loadImage("icons/anchor.png", "Image"), size=loadImage("icons/anchor.png", "Size"))
darkness = ctk.CTkImage(dark_image=loadImage("icons/darkness.png", "Image"), size=loadImage("icons/darkness.png", "Size"))
deflect = ctk.CTkImage(dark_image=loadImage("icons/deflect.png", "Image"), size=loadImage("icons/deflect.png", "Size"))
fort = ctk.CTkImage(dark_image=loadImage("icons/fort.png", "Image"), size=loadImage("icons/fort.png", "Size"))
dw = ctk.CTkImage(dark_image=loadImage("icons/dw.png", "Image"), size=loadImage("icons/dw.png", "Size"))
hh = ctk.CTkImage(dark_image=loadImage("icons/hh.png", "Image"), size=loadImage("icons/hh.png", "Size"))
ad = ctk.CTkImage(dark_image=loadImage("icons/ad.png", "Image"), size=loadImage("icons/ad.png", "Size"))

#other
pad1_green = ctk.CTkImage(dark_image=loadImage("icons/pad1_green.png", "Image"), size=loadImage("icons/pad1_green.png", "Size"))
vuln = ctk.CTkImage(dark_image=loadImage("icons/vuln.png", "Image"), size=loadImage("icons/vuln.png", "Size"))
veng = ctk.CTkImage(dark_image=loadImage("icons/veng.png", "Image"), size=loadImage("icons/veng.png", "Size"))
dtb = ctk.CTkImage(dark_image=loadImage("icons/dtb.png", "Image"), size=loadImage("icons/dtb.png", "Size"))
magicIcon = ctk.CTkImage(dark_image=loadImage("icons/magic.png", "Image"), size=loadImage("icons/magic.png", "Size"))
rangeIcon = ctk.CTkImage(dark_image=loadImage("icons/ranged.png", "Image"), size=loadImage("icons/ranged.png", "Size"))
meleeIcon = ctk.CTkImage(dark_image=loadImage("icons/slam.png", "Image"), size=loadImage("icons/slam.png", "Size"))
cageIcon = ctk.CTkImage(dark_image=loadImage("icons/cage.png", "Image"), size=loadImage("icons/cage.png", "Size"))
smallIcon = ctk.CTkImage(dark_image=loadImage("icons/nukes.png", "Image"), size=loadImage("icons/nukes.png", "Size"))

boxWidth = 60
imageXPad = 10
settingsYPad = 2
gearMenuWidth = 155


def commandUpdate(*args):
    from gui_calcs import update
    update("")


# def appearanceUpdate(*args):
#     global frameBg
#     if themeSwitch.get() == 0:
#         ctk.set_appearance_mode("dark")
#         # themeSwitch.configure(text="Dark mode", font=subtitleFont)
#         frameBg = "#333333"
#     elif themeSwitch.get() == 1:
#         ctk.set_appearance_mode("light")
#         themeSwitch.configure(text="Light mode", font=subtitleFont)
#         frameBg = "#cfcfcf"
#     commandUpdate()

# def themeUpdate(*args):
#     print("test")
#     if colorMenu.get() == "Green":
#         ctk.set_default_color_theme("green")
#     elif colorMenu.get() == "Blue":
#         print("test1")
#         ctk.set_default_color_theme("blue")
#     elif colorMenu.get() == "Cyan":
#         ctk.set_default_color_theme("cyan")
#     elif colorMenu.get() == "Pink":
#         ctk.set_default_color_theme("pink")
#     commandUpdate()

# column0Frame = ctk.CTkFrame(master=root, corner_radius=0)
# column0Frame.grid(row=0, column=0, padx=(10, 5), pady=10, sticky="nsew")

# calcSettings = ctk.CTkLabel(master=column0Frame, text="Info", font=titleFont)
# calcSettings.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
# calcSettings.grid_columnconfigure(0, weight=0, minsize=400)


# colorMenu = ctk.CTkOptionMenu(master=column0Frame, values=["Green", "Blue", "Cyan", "Pink"], command=themeUpdate, corner_radius=0)
# colorMenu.grid(row=1, column=0, padx=0, pady=0, sticky="w")
# colorMenu.set("Green")

# themeSwitch = ctk.CTkSwitch(master=column0Frame, text="Light mode", command=appearanceUpdate, font=subtitleFont)
# themeSwitch.grid(row=2, column=0, padx=0, pady=0, sticky="w")

# Zamorak settings
zamImage = ctk.CTkLabel(master=settingsTabs.tab("Zamorak settings"), image=zam, text="")
zamImage.grid(row=0, column=0, padx=imageXPad, pady=(10, settingsYPad))
enrageLabel = ctk.CTkLabel(master=settingsTabs.tab("Zamorak settings"), text="Enrage", font=subtitleFont)
enrageLabel.grid(row=0, column=1, padx=5, pady=(10, settingsYPad), sticky="w")
enrageInput = ctk.CTkEntry(master=settingsTabs.tab("Zamorak settings"), width=boxWidth, corner_radius=0)
enrageInput.grid(row=0, column=2, padx=20, pady=(10, settingsYPad), sticky="w")

pad1_redImage = ctk.CTkLabel(master=settingsTabs.tab("Zamorak settings"), image=pad1_red, text="")
pad1_redImage.grid(row=1, column=0, padx=imageXPad, pady=settingsYPad)
pad1Label = ctk.CTkLabel(master=settingsTabs.tab("Zamorak settings"), text="Pad 1", font=subtitleFont)
pad1Label.grid(row=1, column=1, padx=5, pady=settingsYPad, sticky="w")
pad1Menu = ctk.CTkOptionMenu(master=settingsTabs.tab("Zamorak settings"), values=["0", "1", "2", "3", "4", "5", "6"], command=commandUpdate, width=digitMenuWidth, corner_radius=0)
pad1Menu.grid(row=1, column=2, padx=20, pady=settingsYPad, sticky="w")

pad2_redImage = ctk.CTkLabel(master=settingsTabs.tab("Zamorak settings"), image=pad2_red, text="")
pad2_redImage.grid(row=2, column=0, padx=imageXPad, pady=settingsYPad)
pad2Label = ctk.CTkLabel(master=settingsTabs.tab("Zamorak settings"), text="Pad 2", font=subtitleFont)
pad2Label.grid(row=2, column=1, padx=5, pady=settingsYPad, sticky="w")
pad2Menu = ctk.CTkOptionMenu(master=settingsTabs.tab("Zamorak settings"), values=["0", "1", "2", "3", "4", "5", "6"], command=commandUpdate, width=digitMenuWidth, corner_radius=0)
pad2Menu.grid(row=2, column=2, padx=20, pady=settingsYPad, sticky="w")

pad3_greenImage = ctk.CTkLabel(master=settingsTabs.tab("Zamorak settings"), image=pad3_green, text="")
pad3_greenImage.grid(row=3, column=0, padx=imageXPad, pady=settingsYPad)
pad3Label = ctk.CTkLabel(master=settingsTabs.tab("Zamorak settings"), text="Pad 3", font=subtitleFont)
pad3Label.grid(row=3, column=1, padx=5, pady=settingsYPad, sticky="w")
pad3Checkbox = ctk.CTkCheckBox(master=settingsTabs.tab("Zamorak settings"), text="", width=0, corner_radius=0)
pad3Checkbox.grid(row=3, column=2, padx=20, pady=settingsYPad, sticky="w")

pad4_redImage = ctk.CTkLabel(master=settingsTabs.tab("Zamorak settings"), image=pad4_red, text="")
pad4_redImage.grid(row=4, column=0, padx=imageXPad, pady=settingsYPad)
pad4Label = ctk.CTkLabel(master=settingsTabs.tab("Zamorak settings"), text="Pad 4", font=subtitleFont)
pad4Label.grid(row=4, column=1, padx=5, pady=settingsYPad, sticky="w")
pad4Menu = ctk.CTkOptionMenu(master=settingsTabs.tab("Zamorak settings"), values=["0", "1", "2", "3", "4", "5", "6"], command=commandUpdate, width=digitMenuWidth,  corner_radius=0)
pad4Menu.grid(row=4, column=2, padx=20, pady=settingsYPad, sticky="w")

pad5_greenImage = ctk.CTkLabel(master=settingsTabs.tab("Zamorak settings"), image=pad5_green, text="")
pad5_greenImage.grid(row=5, column=0, padx=imageXPad, pady=settingsYPad)
pad5Label = ctk.CTkLabel(master=settingsTabs.tab("Zamorak settings"), text="Pad 5", font=subtitleFont)
pad5Label.grid(row=5, column=1, padx=5, pady=settingsYPad, sticky="w")
pad5Checkbox = ctk.CTkCheckBox(master=settingsTabs.tab("Zamorak settings"), text="", width=0, corner_radius=0)
pad5Checkbox.grid(row=5, column=2, padx=20, pady=settingsYPad, sticky="w")

pad6_greenImage = ctk.CTkLabel(master=settingsTabs.tab("Zamorak settings"), image=pad6_green, text="")
pad6_greenImage.grid(row=6, column=0, padx=imageXPad, pady=settingsYPad)
pad6Label = ctk.CTkLabel(master=settingsTabs.tab("Zamorak settings"), text="Pad 6", font=subtitleFont)
pad6Label.grid(row=6, column=1, padx=5, pady=settingsYPad, sticky="w")
pad6Menu = ctk.CTkOptionMenu(master=settingsTabs.tab("Zamorak settings"), values=["0", "1", "2", "3", "4", "5", "6"], command=commandUpdate, width=digitMenuWidth, corner_radius=0)
pad6Menu.grid(row=6, column=2, padx=20, pady=settingsYPad, sticky="w")

chokeImage = ctk.CTkLabel(master=settingsTabs.tab("Zamorak settings"), image=choke, text="")
chokeImage.grid(row=7, column=0, padx=imageXPad, pady=settingsYPad)
chokeLabel = ctk.CTkLabel(master=settingsTabs.tab("Zamorak settings"), text="Choke stacks", font=subtitleFont)
chokeLabel.grid(row=7, column=1, padx=5, pady=settingsYPad, sticky="w")
chokeInput = ctk.CTkEntry(master=settingsTabs.tab("Zamorak settings"), width=boxWidth, corner_radius=0)
chokeInput.grid(row=7, column=2, padx=20, pady=settingsYPad, sticky="w")

slamImage = ctk.CTkLabel(master=settingsTabs.tab("Zamorak settings"), image=slam, text="")
slamImage.grid(row=8, column=0, padx=imageXPad, pady=settingsYPad)
slamLabel = ctk.CTkLabel(master=settingsTabs.tab("Zamorak settings"), text="Melee slam distance", font=subtitleFont)
slamLabel.grid(row=8, column=1, padx=5, pady=settingsYPad, sticky="w")
slamInput = ctk.CTkEntry(master=settingsTabs.tab("Zamorak settings"), width=boxWidth, corner_radius=0)
slamInput.grid(row=8, column=2, padx=20, pady=settingsYPad, sticky="w")

smokeImage = ctk.CTkLabel(master=settingsTabs.tab("Zamorak settings"), image=smoke, text="")
smokeImage.grid(row=9, column=0, padx=imageXPad, pady=settingsYPad)
smokeLabel = ctk.CTkLabel(master=settingsTabs.tab("Zamorak settings"), text="Flames of Zamorak", font=subtitleFont)
smokeLabel.grid(row=9, column=1, padx=5, pady=settingsYPad, sticky="w")
smokeInput = ctk.CTkEntry(master=settingsTabs.tab("Zamorak settings"), width=boxWidth, corner_radius=0)
smokeInput.grid(row=9, column=2, padx=20, pady=settingsYPad, sticky="w")
infernusLabel = ctk.CTkLabel(master=settingsTabs.tab("Zamorak settings"), text="Infernus", font=subtitleFont)
infernusLabel.grid(row=9, column=3, padx=0, pady=settingsYPad, sticky="w")
smokeCheckbox = ctk.CTkCheckBox(master=settingsTabs.tab("Zamorak settings"), text="", width=10, corner_radius=0)
smokeCheckbox.grid(row=9, column=4, padx=5, pady=settingsYPad, sticky="w")

tombImage = ctk.CTkLabel(master=settingsTabs.tab("Zamorak settings"), image=tomb, text="")
tombImage.grid(row=10, column=0, padx=imageXPad, pady=settingsYPad)
tombLabel = ctk.CTkLabel(master=settingsTabs.tab("Zamorak settings"), text="Tomb", font=subtitleFont)
tombLabel.grid(row=10, column=1, padx=5, pady=settingsYPad, sticky="w")
tombInput = ctk.CTkEntry(master=settingsTabs.tab("Zamorak settings"), width=boxWidth, corner_radius=0)
tombInput.grid(row=10, column=2, padx=20, pady=settingsYPad, sticky="w")

decimationImage = ctk.CTkLabel(master=settingsTabs.tab("Zamorak settings"), image=decimation, text="")
decimationImage.grid(row=11, column=0, padx=imageXPad, pady=settingsYPad)
decimationLabel = ctk.CTkLabel(master=settingsTabs.tab("Zamorak settings"), text="Decimation", font=subtitleFont)
decimationLabel.grid(row=11, column=1, padx=5, pady=settingsYPad, sticky="w")
decimationInput = ctk.CTkEntry(master=settingsTabs.tab("Zamorak settings"), width=boxWidth, corner_radius=0)
decimationInput.grid(row=11, column=2, padx=20, pady=settingsYPad, sticky="w")

greyImage = ctk.CTkLabel(master=settingsTabs.tab("Zamorak settings"), image=decimation, text="")
# greyImage.grid(row=12, column=0, padx=imageXPad, pady=settingsYPad)
greyLabel = ctk.CTkLabel(master=settingsTabs.tab("Zamorak settings"), text="Grey/Red Hp", font=subtitleFont)
greyLabel.grid(row=12, column=1, padx=5, pady=settingsYPad, sticky="w")
greyCheckbox = ctk.CTkCheckBox(master=settingsTabs.tab("Zamorak settings"), text="", width=0, corner_radius=0)
greyCheckbox.grid(row=12, column=2, padx=20, pady=settingsYPad, sticky="w")

aggroImage = ctk.CTkLabel(master=settingsTabs.tab("Zamorak settings"), image=aggro, text="")
aggroImage.grid(row=13, column=0, padx=imageXPad, pady=(settingsYPad, 10))
aggroLabel = ctk.CTkLabel(master=settingsTabs.tab("Zamorak settings"), text="Aggro", font=subtitleFont)
aggroLabel.grid(row=13, column=1, padx=5, pady=(settingsYPad, 10), sticky="w")
aggroCheckbox = ctk.CTkCheckBox(master=settingsTabs.tab("Zamorak settings"), text="", width=0, corner_radius=0)
aggroCheckbox.grid(row=13, column=2, padx=20, pady=(settingsYPad, 10), sticky="w")

# p7 stuff
def p7modeCallback(*args):
    if p7modeMenu.get() == "Charge value":
        p7iterationImage.grid_forget()
        p7iterationLabel.grid_forget()
        p7iterationEntry.grid_forget()
        p7redBarImage.grid_forget()
        p7redBarLabel.grid_forget()
        p7redBarEntry.grid_forget()

        p7chargeImage.grid(row=0, column=0, padx=imageXPad, pady=settingsYPad)
        p7chargeLabel.grid(row=0, column=1, padx=0, pady=settingsYPad, sticky="w")
        p7chargeEntry.grid(row=0, column=2, padx=10, pady=settingsYPad, sticky="w")

    elif p7modeMenu.get() == "Iteration":
        p7chargeImage.grid_forget()
        p7chargeLabel.grid_forget()
        p7chargeEntry.grid_forget()
        p7redBarImage.grid_forget()
        p7redBarLabel.grid_forget()
        p7redBarEntry.grid_forget()

        p7iterationImage.grid(row=0, column=0, padx=imageXPad, pady=settingsYPad)
        p7iterationLabel.grid(row=0, column=1, padx=0, pady=settingsYPad, sticky="w")
        p7iterationEntry.grid(row=0, column=2, padx=10, pady=settingsYPad, sticky="w")

    elif p7modeMenu.get() == "Red bar":
        p7chargeImage.grid_forget()
        p7chargeLabel.grid_forget()
        p7chargeEntry.grid_forget()
        p7iterationImage.grid_forget()
        p7iterationLabel.grid_forget()
        p7iterationEntry.grid_forget()

        p7redBarImage.grid(row=0, column=0, padx=imageXPad, pady=settingsYPad)
        p7redBarLabel.grid(row=0, column=1, padx=0, pady=settingsYPad, sticky="w")
        p7redBarEntry.grid(row=0, column=2, padx=10, pady=settingsYPad, sticky="w")

    commandUpdate()

p7Frame = ctk.CTkFrame(master=settingsTabs.tab("Zamorak settings"), corner_radius=0, fg_color=frameBg)
p7Frame.grid(row=14, column=0, columnspan=5, padx=0, pady=10, sticky="nsew")
p7Frame.grid_columnconfigure(0, weight=0)
p7Frame.grid_columnconfigure(1, weight=1)

p7Label = ctk.CTkLabel(master=p7Frame, text="P7 settings", font=titleFont)
p7Label.grid(row=0, column=0, columnspan=2, padx=imageXPad, pady=10, sticky="w")
p7modeLabel = ctk.CTkLabel(master=p7Frame, text="Input mode", font=subtitleFont)
p7modeLabel.grid(row=1, column=0, padx=imageXPad, pady=10, sticky="w")
p7modeMenu = ctk.CTkOptionMenu(master=p7Frame, values=["Charge value", "Iteration", "Red bar"], command=p7modeCallback, width=120, corner_radius=0)
p7modeMenu.grid(row=1, column=1, padx=5, pady=5, sticky="w")

p7inputFrame = ctk.CTkFrame(master=p7Frame, corner_radius=0, fg_color=frameBg)
p7inputFrame.grid(row=2, column=0, columnspan=2, padx=0, pady=0, sticky="nsew")

p7chargeImage = ctk.CTkLabel(master=p7inputFrame, image=charge, text="")
p7chargeLabel = ctk.CTkLabel(master=p7inputFrame, text="Charge value", font=subtitleFont)
p7chargeEntry = ctk.CTkEntry(master=p7inputFrame, width=boxWidth, corner_radius=0)
p7iterationImage = ctk.CTkLabel(master=p7inputFrame, image=charge, text="")
p7iterationLabel = ctk.CTkLabel(master=p7inputFrame, text="Iteration", font=subtitleFont)
p7iterationEntry = ctk.CTkEntry(master=p7inputFrame, width=boxWidth, corner_radius=0)
p7redBarImage = ctk.CTkLabel(master=p7inputFrame, image=redbar, text="")
p7redBarLabel = ctk.CTkLabel(master=p7inputFrame, text="Red Bar", font=subtitleFont)
p7redBarEntry = ctk.CTkEntry(master=p7inputFrame, width=boxWidth, corner_radius=0)

p7chargeImage.grid(row=0, column=0, padx=imageXPad, pady=5)
p7chargeLabel.grid(row=0, column=1, padx=0, pady=5, sticky="w")
p7chargeEntry.grid(row=0, column=2, padx=10, pady=5, sticky="w")

p7infoLabel = ctk.CTkLabel(master=p7Frame, text="")
p7infoLabel1 = ctk.CTkLabel(master=p7Frame, text="")
p7infoLabel2 = ctk.CTkLabel(master=p7Frame, text="")

# Player settings
helmImage = ctk.CTkLabel(master=settingsTabs.tab("Player settings"), image=helm, text="")
helmImage.grid(row=0, column=0, padx=imageXPad, pady=(10, settingsYPad))
helmLabel = ctk.CTkLabel(master=settingsTabs.tab("Player settings"), text="Helm", font=subtitleFont)
helmLabel.grid(row=0, column=1, padx=5, pady=(10, settingsYPad), sticky="w")
helmMenu = ctk.CTkOptionMenu(master=settingsTabs.tab("Player settings"), values=["Other/Dps", "Cryptbloom", "Achto (mage)", "Achto (non mage)", "Deathwarden", "Sub. Ports", "Ganodermic"], command=commandUpdate, width=gearMenuWidth, corner_radius=0)
helmMenu.grid(row=0, column=2, padx=20, pady=(10, settingsYPad), sticky="w")

topImage = ctk.CTkLabel(master=settingsTabs.tab("Player settings"), image=top, text="")
topImage.grid(row=1, column=0, padx=imageXPad, pady=settingsYPad)
topLabel = ctk.CTkLabel(master=settingsTabs.tab("Player settings"), text="Top", font=subtitleFont)
topLabel.grid(row=1, column=1, padx=5, pady=settingsYPad, sticky="w")
topMenu = ctk.CTkOptionMenu(master=settingsTabs.tab("Player settings"), values=["Other/Dps", "Cryptbloom", "Achto (mage)", "Achto (non mage)", "Deathwarden", "Sub. Ports", "Ganodermic"], command=commandUpdate, width=gearMenuWidth, corner_radius=0)
topMenu.grid(row=1, column=2, padx=20, pady=settingsYPad, sticky="w")

bottomsImage = ctk.CTkLabel(master=settingsTabs.tab("Player settings"), image=bottoms, text="")
bottomsImage.grid(row=2, column=0, padx=imageXPad, pady=settingsYPad)
bottomsLabel = ctk.CTkLabel(master=settingsTabs.tab("Player settings"), text="Bottoms", font=subtitleFont)
bottomsLabel.grid(row=2, column=1, padx=5, pady=settingsYPad, sticky="w")
bottomsMenu = ctk.CTkOptionMenu(master=settingsTabs.tab("Player settings"), values=["Other/Dps", "Deathtouch bracelet", "Cryptbloom", "Achto (mage)", "Achto (non mage)", "Deathwarden", "Sub. Ports", "Ganodermic"], command=commandUpdate, width=gearMenuWidth, corner_radius=0)
bottomsMenu.grid(row=2, column=2, padx=20, pady=settingsYPad, sticky="w")

glovesImage = ctk.CTkLabel(master=settingsTabs.tab("Player settings"), image=gloves, text="")
glovesImage.grid(row=3, column=0, padx=imageXPad, pady=settingsYPad)
glovesLabel = ctk.CTkLabel(master=settingsTabs.tab("Player settings"), text="Gloves", font=subtitleFont)
glovesLabel.grid(row=3, column=1, padx=5, pady=settingsYPad, sticky="w")
glovesMenu = ctk.CTkOptionMenu(master=settingsTabs.tab("Player settings"), values=["Other/Dps", "Deathtouch bracelet", "Cryptbloom", "Achto (mage)", "Achto (non mage)", "Deathwarden", "Sub. Ports", "Ganodermic"], command=commandUpdate, width=gearMenuWidth, corner_radius=0)
glovesMenu.grid(row=3, column=2, padx=20, pady=settingsYPad, sticky="w")

bootsImage = ctk.CTkLabel(master=settingsTabs.tab("Player settings"), image=boots, text="")
bootsImage.grid(row=4, column=0, padx=imageXPad, pady=settingsYPad)
bootsLabel = ctk.CTkLabel(master=settingsTabs.tab("Player settings"), text="Boots", font=subtitleFont)
bootsLabel.grid(row=4, column=1, padx=5, pady=settingsYPad, sticky="w")
bootsMenu = ctk.CTkOptionMenu(master=settingsTabs.tab("Player settings"), values=["Other/Dps", "Cryptbloom", "Achto (mage)", "Achto (non mage)", "Deathwarden", "Sub. Ports", "Ganodermic"], command=commandUpdate, width=gearMenuWidth, corner_radius=0)
bootsMenu.grid(row=4, column=2, padx=20, pady=settingsYPad, sticky="w")

shieldImage = ctk.CTkLabel(master=settingsTabs.tab("Player settings"), image=shield, text="")
shieldImage.grid(row=5, column=0, padx=imageXPad, pady=settingsYPad)
shieldLabel = ctk.CTkLabel(master=settingsTabs.tab("Player settings"), text="Shield", font=subtitleFont)
shieldLabel.grid(row=5, column=1, padx=5, pady=settingsYPad, sticky="w")
shieldMenu = ctk.CTkOptionMenu(master=settingsTabs.tab("Player settings"), values=["None", "T90", "Spirit", "T90 defender"], command=commandUpdate, width=gearMenuWidth, corner_radius=0)
shieldMenu.grid(row=5, column=2, padx=20, pady=settingsYPad, sticky="w")

eofImage = ctk.CTkLabel(master=settingsTabs.tab("Player settings"), image=eof, text="")
eofImage.grid(row=6, column=0, padx=imageXPad, pady=settingsYPad)
eofLabel = ctk.CTkLabel(master=settingsTabs.tab("Player settings"), text="EoF/Amulet of Souls", font=subtitleFont)
eofLabel.grid(row=6, column=1, padx=5, pady=settingsYPad, sticky="w")
eofCheckbox = ctk.CTkCheckBox(master=settingsTabs.tab("Player settings"), text="", width=0, corner_radius=0)
eofCheckbox.grid(row=6, column=2, padx=20, pady=settingsYPad, sticky="w")

ovlImage = ctk.CTkLabel(master=settingsTabs.tab("Player settings"), image=ovl, text="")
ovlImage.grid(row=7, column=0, padx=imageXPad, pady=settingsYPad)
ovlLabel = ctk.CTkLabel(master=settingsTabs.tab("Player settings"), text="Overload", font=subtitleFont)
ovlLabel.grid(row=7, column=1, padx=5, pady=settingsYPad, sticky="w")
ovlMenu = ctk.CTkOptionMenu(master=settingsTabs.tab("Player settings"), values=["None", "Elder overload"], command=commandUpdate, width=gearMenuWidth, corner_radius=0)
ovlMenu.grid(row=7, column=2, padx=20, pady=settingsYPad, sticky="w")

defImage = ctk.CTkLabel(master=settingsTabs.tab("Player settings"), image=defence, text="")
defImage.grid(row=8, column=0, padx=imageXPad, pady=settingsYPad)
defLabel = ctk.CTkLabel(master=settingsTabs.tab("Player settings"), text="Defence level", font=subtitleFont)
defLabel.grid(row=8, column=1, padx=5, pady=settingsYPad, sticky="w")
defEntry = ctk.CTkEntry(master=settingsTabs.tab("Player settings"), width=boxWidth, corner_radius=0)
defEntry.grid(row=8, column=2, padx=20, pady=settingsYPad, sticky="w")

powderImage = ctk.CTkLabel(master=settingsTabs.tab("Player settings"), image=powder, text="")
powderImage.grid(row=9, column=0, padx=imageXPad, pady=settingsYPad)
powderLabel = ctk.CTkLabel(master=settingsTabs.tab("Player settings"), text="Penance Powder", font=subtitleFont)
powderLabel.grid(row=9, column=1, padx=5, pady=settingsYPad, sticky="w")
powderCheckbox = ctk.CTkCheckBox(master=settingsTabs.tab("Player settings"), text="", width=0, corner_radius=0)
powderCheckbox.grid(row=9, column=2, padx=20, pady=settingsYPad, sticky="w")

ppointsImage = ctk.CTkLabel(master=settingsTabs.tab("Player settings"), image=ppoints, text="")
ppointsImage.grid(row=10, column=0, padx=imageXPad, pady=settingsYPad)
ppointsLabel = ctk.CTkLabel(master=settingsTabs.tab("Player settings"), text="Prayer Points", font=subtitleFont)
ppointsLabel.grid(row=10, column=1, padx=5, pady=settingsYPad, sticky="w")
ppointsInput = ctk.CTkEntry(master=settingsTabs.tab("Player settings"), width=boxWidth, corner_radius=0)
ppointsInput.grid(row=10, column=2, padx=20, pady=settingsYPad, sticky="w")

afflictionImage = ctk.CTkLabel(master=settingsTabs.tab("Player settings"), image=affliction, text="")
afflictionImage.grid(row=11, column=0, padx=imageXPad, pady=settingsYPad)
afflictionLabel = ctk.CTkLabel(master=settingsTabs.tab("Player settings"), text="Affliction", font=subtitleFont)
afflictionLabel.grid(row=11, column=1, padx=5, pady=settingsYPad, sticky="w")
afflictionInput = ctk.CTkEntry(master=settingsTabs.tab("Player settings"), width=boxWidth, corner_radius=0)
afflictionInput.grid(row=11, column=2, padx=20, pady=settingsYPad, sticky="w")

desolationImage = ctk.CTkLabel(master=settingsTabs.tab("Player settings"), image=desolation, text="")
desolationImage.grid(row=12, column=0, padx=imageXPad, pady=settingsYPad)
desolationLabel = ctk.CTkLabel(master=settingsTabs.tab("Player settings"), text="Desolation", font=subtitleFont)
desolationLabel.grid(row=12, column=1, padx=5, pady=settingsYPad, sticky="w")
desolationInput = ctk.CTkEntry(master=settingsTabs.tab("Player settings"), width=boxWidth, corner_radius=0)
desolationInput.grid(row=12, column=2, padx=20, pady=settingsYPad, sticky="w")

maxhpImage = ctk.CTkLabel(master=settingsTabs.tab("Player settings"), image=maxhp, text="")
maxhpImage.grid(row=13, column=0, padx=imageXPad, pady=settingsYPad)
maxhpLabel = ctk.CTkLabel(master=settingsTabs.tab("Player settings"), text="Max Life points", font=subtitleFont)
maxhpLabel.grid(row=13, column=1, padx=5, pady=settingsYPad, sticky="w")
maxhpInput = ctk.CTkEntry(master=settingsTabs.tab("Player settings"), width=boxWidth, corner_radius=0)
maxhpInput.grid(row=13, column=2, padx=20, pady=settingsYPad, sticky="w")

currenthpImage = ctk.CTkLabel(master=settingsTabs.tab("Player settings"), image=currenthp, text="")
currenthpImage.grid(row=14, column=0, padx=imageXPad, pady=settingsYPad)
currenthpLabel = ctk.CTkLabel(master=settingsTabs.tab("Player settings"), text="Current Life points", font=subtitleFont)
currenthpLabel.grid(row=14, column=1, padx=5, pady=settingsYPad, sticky="w")
currenthpInput = ctk.CTkEntry(master=settingsTabs.tab("Player settings"), width=boxWidth, corner_radius=0)
currenthpInput.grid(row=14, column=2, padx=20, pady=settingsYPad, sticky="w")

boneshieldImage = ctk.CTkLabel(master=settingsTabs.tab("Player settings"), image=boneshield, text="")
boneshieldImage.grid(row=15, column=0, padx=imageXPad, pady=settingsYPad)
boneshieldLabel = ctk.CTkLabel(master=settingsTabs.tab("Player settings"), text="Boneshield tier", font=subtitleFont)
boneshieldLabel.grid(row=15, column=1, padx=5, pady=settingsYPad, sticky="w")
boneshieldInput = ctk.CTkEntry(master=settingsTabs.tab("Player settings"), width=boxWidth, corner_radius=0)
boneshieldInput.grid(row=15, column=2, padx=20, pady=settingsYPad, sticky="w")

totgImage = ctk.CTkLabel(master=settingsTabs.tab("Player settings"), image=totg, text="")
totgImage.grid(row=16, column=0, padx=imageXPad, pady=settingsYPad)
totgLabel = ctk.CTkLabel(master=settingsTabs.tab("Player settings"), text="Twilight of the Gods", font=subtitleFont)
totgLabel.grid(row=16, column=1, padx=5, pady=5, sticky="w")
totgCheckbox = ctk.CTkCheckBox(master=settingsTabs.tab("Player settings"), text="", width=0, corner_radius=0)
totgCheckbox.grid(row=16, column=2, padx=20, pady=settingsYPad, sticky="w")

puzzleboxImage = ctk.CTkLabel(master=settingsTabs.tab("Player settings"), image=puzzlebox, text="")
puzzleboxImage.grid(row=17, column=0, padx=imageXPad, pady=(settingsYPad, 10))
puzzleboxLabel = ctk.CTkLabel(master=settingsTabs.tab("Player settings"), text="Infernal Puzzle Box", font=subtitleFont)
puzzleboxLabel.grid(row=17, column=1, padx=5, pady=(settingsYPad, 10), sticky="w")
puzzleboxCheckbox = ctk.CTkCheckBox(master=settingsTabs.tab("Player settings"), text="", width=0, corner_radius=0)
puzzleboxCheckbox.grid(row=17, column=2, padx=20, pady=(settingsYPad, 10), sticky="w")

# Modifiers settings
disrImage = ctk.CTkLabel(master=settingsTabs.tab("Damage modifiers"), image=disr, text="")
disrImage.grid(row=0, column=0, padx=imageXPad, pady=(10, settingsYPad))
disrLabel = ctk.CTkLabel(master=settingsTabs.tab("Damage modifiers"), text="Disruption Shield", font=subtitleFont)
disrLabel.grid(row=0, column=1, padx=5, pady=(10, settingsYPad), sticky="w")
disrCheckbox = ctk.CTkCheckBox(master=settingsTabs.tab("Damage modifiers"), text="", width=0, corner_radius=0)
disrCheckbox.grid(row=0, column=2, padx=20, pady=(10, settingsYPad), sticky="w")

cadeImage = ctk.CTkLabel(master=settingsTabs.tab("Damage modifiers"), image=cade, text="")
cadeImage.grid(row=1, column=0, padx=imageXPad, pady=settingsYPad)
cadeLabel = ctk.CTkLabel(master=settingsTabs.tab("Damage modifiers"), text="Barricade", font=subtitleFont)
cadeLabel.grid(row=1, column=1, padx=5, pady=settingsYPad, sticky="w")
cadeCheckbox = ctk.CTkCheckBox(master=settingsTabs.tab("Damage modifiers"), text="", width=0, corner_radius=0)
cadeCheckbox.grid(row=1, column=2, padx=20, pady=settingsYPad, sticky="w")

divertImage = ctk.CTkLabel(master=settingsTabs.tab("Damage modifiers"), image=divert, text="")
divertImage.grid(row=2, column=0, padx=imageXPad, pady=settingsYPad)
divertLabel = ctk.CTkLabel(master=settingsTabs.tab("Damage modifiers"), text="Divert/Resonance", font=subtitleFont)
divertLabel.grid(row=2, column=1, padx=5, pady=settingsYPad, sticky="w")
divertMenu = ctk.CTkOptionMenu(master=settingsTabs.tab("Damage modifiers"), values=["None", "Divert", "Resonance"], command=commandUpdate, width=120, corner_radius=0)
divertMenu.grid(row=2, column=2, padx=20, pady=settingsYPad, sticky="w")

reflImage = ctk.CTkLabel(master=settingsTabs.tab("Damage modifiers"), image=refl, text="")
reflImage.grid(row=3, column=0, padx=imageXPad, pady=settingsYPad)
reflLabel = ctk.CTkLabel(master=settingsTabs.tab("Damage modifiers"), text="Reflect", font=subtitleFont)
reflLabel.grid(row=3, column=1, padx=5, pady=settingsYPad, sticky="w")
reflCheckbox = ctk.CTkCheckBox(master=settingsTabs.tab("Damage modifiers"), text="", width=0, corner_radius=0)
reflCheckbox.grid(row=3, column=2, padx=20, pady=settingsYPad, sticky="w")

debilImage = ctk.CTkLabel(master=settingsTabs.tab("Damage modifiers"), image=debil, text="")
debilImage.grid(row=4, column=0, padx=imageXPad, pady=settingsYPad)
debilLabel = ctk.CTkLabel(master=settingsTabs.tab("Damage modifiers"), text="Debilitate", font=subtitleFont)
debilLabel.grid(row=4, column=1, padx=5, pady=settingsYPad, sticky="w")
debilCheckbox = ctk.CTkCheckBox(master=settingsTabs.tab("Damage modifiers"), text="", width=0, corner_radius=0)
debilCheckbox.grid(row=4, column=2, padx=20, pady=settingsYPad, sticky="w")

sdImage = ctk.CTkLabel(master=settingsTabs.tab("Damage modifiers"), image=sd, text="")
sdImage.grid(row=5, column=0, padx=imageXPad, pady=settingsYPad)
sdLabel = ctk.CTkLabel(master=settingsTabs.tab("Damage modifiers"), text="Shield Dome", font=subtitleFont)
sdLabel.grid(row=5, column=1, padx=5, pady=settingsYPad, sticky="w")
sdMenu = ctk.CTkOptionMenu(master=settingsTabs.tab("Damage modifiers"), values=["50", "25", "12", "6", "3", "1", "0"], command=commandUpdate, width=digitMenuWidth, corner_radius=0)
sdMenu.grid(row=5, column=2, padx=20, pady=settingsYPad, sticky="w")

immortImage = ctk.CTkLabel(master=settingsTabs.tab("Damage modifiers"), image=immort, text="")
immortImage.grid(row=6, column=0, padx=imageXPad, pady=settingsYPad)
immortLabel = ctk.CTkLabel(master=settingsTabs.tab("Damage modifiers"), text="Immortality", font=subtitleFont)
immortLabel.grid(row=6, column=1, padx=5, pady=settingsYPad, sticky="w")
immortCheckbox = ctk.CTkCheckBox(master=settingsTabs.tab("Damage modifiers"), text="", width=0, corner_radius=0)
immortCheckbox.grid(row=6, column=2, padx=20, pady=settingsYPad, sticky="w")

antiImage = ctk.CTkLabel(master=settingsTabs.tab("Damage modifiers"), image=anti, text="")
antiImage.grid(row=7, column=0, padx=imageXPad, pady=settingsYPad)
antiLabel = ctk.CTkLabel(master=settingsTabs.tab("Damage modifiers"), text="anticipation", font=subtitleFont)
antiLabel.grid(row=7, column=1, padx=5, pady=settingsYPad, sticky="w")
antiCheckbox = ctk.CTkCheckBox(master=settingsTabs.tab("Damage modifiers"), text="", width=0, corner_radius=0)
antiCheckbox.grid(row=7, column=2, padx=20, pady=settingsYPad, sticky="w")

fulImage = ctk.CTkLabel(master=settingsTabs.tab("Damage modifiers"), image=ful, text="")
fulImage.grid(row=8, column=0, padx=imageXPad, pady=settingsYPad)
fulLabel = ctk.CTkLabel(master=settingsTabs.tab("Damage modifiers"), text="Scripture of Ful", font=subtitleFont)
fulLabel.grid(row=8, column=1, padx=5, pady=settingsYPad, sticky="w")
fulCheckbox = ctk.CTkCheckBox(master=settingsTabs.tab("Damage modifiers"), text="", width=0, corner_radius=0)
fulCheckbox.grid(row=8, column=2, padx=20, pady=settingsYPad, sticky="w")

auraImage = ctk.CTkLabel(master=settingsTabs.tab("Damage modifiers"), image=aegis, text="")
auraImage.grid(row=9, column=0, padx=imageXPad, pady=settingsYPad)
auraLabel = ctk.CTkLabel(master=settingsTabs.tab("Damage modifiers"), text="Aura", font=subtitleFont)
auraLabel.grid(row=9, column=1, padx=5, pady=settingsYPad, sticky="w")
auraMenu = ctk.CTkOptionMenu(master=settingsTabs.tab("Damage modifiers"), values=["None", "Aegis", "Zerk aura"], command=commandUpdate, width=120, corner_radius=0)
auraMenu.grid(row=9, column=2, padx=20, pady=settingsYPad, sticky="w")

zerkImage = ctk.CTkLabel(master=settingsTabs.tab("Damage modifiers"), image=zerk, text="")
zerkImage.grid(row=10, column=0, padx=imageXPad, pady=settingsYPad)
zerkLabel = ctk.CTkLabel(master=settingsTabs.tab("Damage modifiers"), text="Berserker", font=subtitleFont)
zerkLabel.grid(row=10, column=1, padx=5, pady=settingsYPad, sticky="w")
zerkCheckbox = ctk.CTkCheckBox(master=settingsTabs.tab("Damage modifiers"), text="", width=0, corner_radius=0)
zerkCheckbox.grid(row=10, column=2, padx=20, pady=settingsYPad, sticky="w")

pulvImage = ctk.CTkLabel(master=settingsTabs.tab("Damage modifiers"), image=pulv, text="")
pulvImage.grid(row=11, column=0, padx=imageXPad, pady=settingsYPad)
pulvLabel = ctk.CTkLabel(master=settingsTabs.tab("Damage modifiers"), text="Pulverize", font=subtitleFont)
pulvLabel.grid(row=11, column=1, padx=5, pady=settingsYPad, sticky="w")
pulvCheckbox = ctk.CTkCheckBox(master=settingsTabs.tab("Damage modifiers"), text="", width=0, corner_radius=0)
pulvCheckbox.grid(row=11, column=2, padx=20, pady=settingsYPad, sticky="w")

severImage = ctk.CTkLabel(master=settingsTabs.tab("Damage modifiers"), image=sever, text="")
severImage.grid(row=12, column=0, padx=imageXPad, pady=settingsYPad)
severLabel = ctk.CTkLabel(master=settingsTabs.tab("Damage modifiers"), text="Sever", font=subtitleFont)
severLabel.grid(row=12, column=1, padx=5, pady=settingsYPad, sticky="w")
severCheckbox = ctk.CTkCheckBox(master=settingsTabs.tab("Damage modifiers"), text="", width=0, corner_radius=0)
severCheckbox.grid(row=12, column=2, padx=20, pady=settingsYPad, sticky="w")

absorbImage = ctk.CTkLabel(master=settingsTabs.tab("Damage modifiers"), image=absorb, text="")
absorbImage.grid(row=13, column=0, padx=imageXPad, pady=settingsYPad)
absorbLabel = ctk.CTkLabel(master=settingsTabs.tab("Damage modifiers"), text="Absorbative", font=subtitleFont)
absorbLabel.grid(row=13, column=1, padx=5, pady=settingsYPad, sticky="w")
absorbMenu = ctk.CTkOptionMenu(master=settingsTabs.tab("Damage modifiers"), values=["0", "1", "2", "3", "4"], command=commandUpdate, width=digitMenuWidth, corner_radius=0)
absorbMenu.grid(row=13, column=2, padx=20, pady=settingsYPad, sticky="w")

enfeebleImage = ctk.CTkLabel(master=settingsTabs.tab("Damage modifiers"), image=enfeeble, text="")
enfeebleImage.grid(row=14, column=0, padx=imageXPad, pady=settingsYPad)
enfeebleLabel = ctk.CTkLabel(master=settingsTabs.tab("Damage modifiers"), text="Enfeeble", font=subtitleFont)
enfeebleLabel.grid(row=14, column=1, padx=5, pady=settingsYPad, sticky="w")
enfeebleCheckbox = ctk.CTkCheckBox(master=settingsTabs.tab("Damage modifiers"), text="", width=0, corner_radius=0)
enfeebleCheckbox.grid(row=14, column=2, padx=20, pady=settingsYPad, sticky="w")

emeraldImage = ctk.CTkLabel(master=settingsTabs.tab("Damage modifiers"), image=emerald, text="")
emeraldImage.grid(row=15, column=0, padx=imageXPad, pady=settingsYPad)
emeraldLabel = ctk.CTkLabel(master=settingsTabs.tab("Damage modifiers"), text="Emerald Aurora", font=subtitleFont)
emeraldLabel.grid(row=15, column=1, padx=5, pady=settingsYPad, sticky="w")
emeraldMenu = ctk.CTkOptionMenu(master=settingsTabs.tab("Damage modifiers"), values=["0", "1", "2", "3", "4"], command=commandUpdate, width=digitMenuWidth, corner_radius=0)
emeraldMenu.grid(row=15, column=2, padx=20, pady=settingsYPad, sticky="w")

anchorImage = ctk.CTkLabel(master=settingsTabs.tab("Damage modifiers"), image=anchor, text="")
anchorImage.grid(row=16, column=0, padx=imageXPad, pady=settingsYPad)
anchorLabel = ctk.CTkLabel(master=settingsTabs.tab("Damage modifiers"), text="Barrelchest Anchor", font=subtitleFont)
anchorLabel.grid(row=16, column=1, padx=5, pady=settingsYPad, sticky="w")
anchorCheckbox = ctk.CTkCheckBox(master=settingsTabs.tab("Damage modifiers"), text="", width=0, corner_radius=0)
anchorCheckbox.grid(row=16, column=2, padx=20, pady=settingsYPad, sticky="w")

darknessImage = ctk.CTkLabel(master=settingsTabs.tab("Damage modifiers"), image=darkness, text="")
darknessImage.grid(row=17, column=0, padx=imageXPad, pady=settingsYPad)
darknessLabel = ctk.CTkLabel(master=settingsTabs.tab("Damage modifiers"), text="Power of Darkness", font=subtitleFont)
darknessLabel.grid(row=17, column=1, padx=5, pady=settingsYPad, sticky="w")
darknessCheckbox = ctk.CTkCheckBox(master=settingsTabs.tab("Damage modifiers"), text="", width=0, corner_radius=0)
darknessCheckbox.grid(row=17, column=2, padx=20, pady=settingsYPad, sticky="w")

deflectImage = ctk.CTkLabel(master=settingsTabs.tab("Damage modifiers"), image=deflect, text="")
deflectImage.grid(row=18, column=0, padx=imageXPad, pady=settingsYPad)
deflectLabel = ctk.CTkLabel(master=settingsTabs.tab("Damage modifiers"), text="Deflect prayer", font=subtitleFont)
deflectLabel.grid(row=18, column=1, padx=5, pady=settingsYPad, sticky="w")
deflectCheckbox = ctk.CTkCheckBox(master=settingsTabs.tab("Damage modifiers"), text="", width=0, corner_radius=0)
deflectCheckbox.grid(row=18, column=2, padx=20, pady=settingsYPad, sticky="w")

fortImage = ctk.CTkLabel(master=settingsTabs.tab("Damage modifiers"), image=fort, text="")
fortImage.grid(row=19, column=0, padx=imageXPad, pady=settingsYPad)
fortLabel = ctk.CTkLabel(master=settingsTabs.tab("Damage modifiers"), text="Fortitude", font=subtitleFont)
fortLabel.grid(row=19, column=1, padx=5, pady=settingsYPad, sticky="w")
fortCheckbox = ctk.CTkCheckBox(master=settingsTabs.tab("Damage modifiers"), text="", width=0, corner_radius=0)
fortCheckbox.grid(row=19, column=2, padx=20, pady=settingsYPad, sticky="w")

dwImage = ctk.CTkLabel(master=settingsTabs.tab("Damage modifiers"), image=dw, text="")
dwImage.grid(row=20, column=0, padx=imageXPad, pady=settingsYPad)
dwLabel = ctk.CTkLabel(master=settingsTabs.tab("Damage modifiers"), text="Death ward", font=subtitleFont)
dwLabel.grid(row=20, column=1, padx=5, pady=settingsYPad, sticky="w")
dwCheckbox = ctk.CTkCheckBox(master=settingsTabs.tab("Damage modifiers"), text="", width=0, corner_radius=0)
dwCheckbox.grid(row=20, column=2, padx=20, pady=settingsYPad, sticky="w")

hhImage = ctk.CTkLabel(master=settingsTabs.tab("Damage modifiers"), image=hh, text="")
hhImage.grid(row=21, column=0, padx=imageXPad, pady=settingsYPad)
hhLabel = ctk.CTkLabel(master=settingsTabs.tab("Damage modifiers"), text="Hellhound", font=subtitleFont)
hhLabel.grid(row=21, column=1, padx=5, pady=settingsYPad, sticky="w")
hhCheckbox = ctk.CTkCheckBox(master=settingsTabs.tab("Damage modifiers"), text="", width=0, corner_radius=0)
hhCheckbox.grid(row=21, column=2, padx=20, pady=settingsYPad, sticky="w")

adImage = ctk.CTkLabel(master=settingsTabs.tab("Damage modifiers"), image=ad, text="")
adImage.grid(row=22, column=0, padx=imageXPad, pady=(settingsYPad, 10))
adLabel = ctk.CTkLabel(master=settingsTabs.tab("Damage modifiers"), text="Animate dead", font=subtitleFont)
adLabel.grid(row=22, column=1, padx=5, pady=(settingsYPad, 10), sticky="w")
adCheckbox = ctk.CTkCheckBox(master=settingsTabs.tab("Damage modifiers"), text="", width=0, corner_radius=0)
adCheckbox.grid(row=22, column=2, padx=20, pady=(settingsYPad, 10), sticky="w")
adCheckbox.select()



# Reflect settings frame
settingsFrame = ctk.CTkFrame(master=column1Frame, corner_radius=0)
settingsFrame.grid(row=1, column=0, padx=10, pady=(10, 5), sticky="nsew")

settingsLabel = ctk.CTkLabel(master=settingsFrame, text="Reflect settings", font=titleFont, corner_radius=0)
settingsLabel.grid(row=0, column=0, columnspan=6, padx=imageXPad, pady=5, sticky="w")

hitcapsFrame = ctk.CTkFrame(master=settingsFrame, corner_radius=0, fg_color=frameBg)
hitcapsFrame.grid(row=1, column=0, padx=0, pady=0, columnspan=6, sticky="nsew")
hitcapsLabel = ctk.CTkLabel(master=hitcapsFrame, text="Hitcap mode", font=subtitleFont, corner_radius=0)
hitcapsLabel.grid(row=0, column=0, padx=imageXPad, pady=5, sticky="w")
hitcapsMenu = ctk.CTkOptionMenu(master=hitcapsFrame, values=["None", "Green Hp", "Grey Hp"], command=commandUpdate, width=100, corner_radius=0)
hitcapsMenu.grid(row=0, column=1, padx=imageXPad, pady=5, sticky="w")

vulnImage = ctk.CTkLabel(master=settingsFrame, image=vuln, text="")
cryptVulnImage = ctk.CTkLabel(master=settingsFrame, image=helm, text="")
deflImage = ctk.CTkLabel(master=settingsFrame, image=deflect, text="")
vengImage = ctk.CTkLabel(master=settingsFrame, image=veng, text="")
dtbImage = ctk.CTkLabel(master=settingsFrame, image=dtb, text="")
vulnImage.grid(row=2, column=0, padx=imageXPad, pady=0, sticky="w")
cryptVulnImage.grid(row=3, column=0, padx=imageXPad, pady=(0, 10), sticky="w")
deflImage.grid(row=2, column=2, padx=imageXPad, pady=0, sticky="w")
vengImage.grid(row=3, column=2, padx=imageXPad, pady=(0, 10), sticky="w")
dtbImage.grid(row=2, column=4, padx=imageXPad, pady=0, sticky="w")

vulnCheckbox = ctk.CTkCheckBox(master=settingsFrame, text="", width=0, corner_radius=0)
cryptVulnCheckbox = ctk.CTkCheckBox(master=settingsFrame, text="", width=0, corner_radius=0)
deflCheckbox = ctk.CTkCheckBox(master=settingsFrame, text="", width=0, corner_radius=0)
vengCheckbox = ctk.CTkCheckBox(master=settingsFrame, text="", width=0, corner_radius=0)
dtbCheckbox = ctk.CTkCheckBox(master=settingsFrame, text="", width=0, corner_radius=0)
vulnCheckbox.grid(row=2, column=1, padx=5, pady=0, sticky="w")
cryptVulnCheckbox.grid(row=3, column=1, padx=5, pady=(0, 10), sticky="w")
deflCheckbox.grid(row=2, column=3, padx=5, pady=0, sticky="w")
vengCheckbox.grid(row=3, column=3, padx=5, pady=(0, 10), sticky="w")
dtbCheckbox.grid(row=2, column=5, padx=5, pady=0, sticky="w")




