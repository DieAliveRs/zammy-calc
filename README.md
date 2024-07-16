# Zamorak Calculator

## Features
- Caculate damage received through multiple damage modifiers
- Healing from resonance
- Adrenaline gained from divert
- Total and isolated reflected damage from multiple sources
- Hp calculations
- Defensives effectiveness through different mechanics and defensives piercing
- Pads effects

### P7 calculations
Due to P7 having big bombs (chaos damage) and small bombs and how their calculations are related, there are three different methods to calculate the damage outputs listed as:
- Charge value
- Iteration
- Red bar

Chaos damage depends directly on the red bar while small bombs depend directly off the charge value. Charge value refers to the healing splat on zamorak, this value with the correct enrage gives enough information to be able to calculate both chaos damage and small bombs damage. Each time a healing splat appears on Zamorak is an Iteration that happens, it goes from 0 to 500 but gets paused when killing the runes. Red bar only provides information to calculate the chaos damage and small bombs damage wont be calculated when using this input mode.

### Settings
The settings can be exported/shared or saved by copying `settings.json` file created, or loaded by replacing it with a new settings file.

## How to run it
The source code provided can be executed with python from the CMD:

`cd <directory where main.py is located>`

`python main.py`

The source code can be built into an executable with Auto Py to Exe with the `auto_py_to_exe_config.json` file. After the conversion the `\icons` folder will be required to be added to the `...\Zammy_calc\` path.

Alternatively, an executable version is provided in `Zammy_calc.rar`. Simply extract the folder and run `Zammy_calc.exe`

