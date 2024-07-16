import json
import os

variables = {}
settings = "settings.json"

def saveSettings(variables):
    with open(settings, 'w') as f:
        json.dump(variables, f)

def loadSettings():
    if os.path.exists(settings):
        with open(settings, 'r') as f:
            variables = json.load(f)
            return variables
    return 1
