import sys
import json
import tkinter as tk
from tkinter import filedialog
from pathlib import Path

######################### File Input Dialog #########################

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

######################### Skill ID to Skill Name relation #########################

skills = {1: "Attack Boost",
          2: "Agitator",
          3: "Peak Performance",
          4: "Resentment",
          5: "Resuscitate",
          6: "Critical Eye",
          7: "Critical Boost",
          8: "Weakness Exploit",
          9: "Latent Power",
          10: "Maximum Might",
          11: "Critical Element",
          12: "Master's Touch",
          13: "Fire Attack",
          14: "Water Attack",
          15: "Ice Attack",
          16: "Thunder Attack",
          17: "Dragon Attack",
          18: "Poison Attack",
          19: "Paralysis Attack",
          20: "Sleep Attack",
          21: "Blast Attack",
          22: "Handicraft",
          23: "Razor Sharp",
          24: "Spare Shot",
          25: "Protective Polish",
          26: "Mind's Eye",
          27: "Ballistics",
          28: "Bludgeoner",
          30: "Focus",
          31: "Power Prolonger",
          32: "Marathon Runner",
          33: "Constitution",
          34: "Stamina Surge",
          35: "Guard",
          36: "Guard Up",
          37: "Offensive Guard",
          38: "Critical Draw",
          39: "Punishing Draw",
          40: "Quick Sheath",
          41: "Slugger",
          42: "Stamina Thief",
          43: "Affinity Sliding",
          44: "Horn Maestro",
          45: "Artillery",
          46: "Load Shells",
          47: "Special Ammo Boost",
          48: "Normal/Rapid Up",
          49: "Pierce Up",
          50: "Spread Up",
          51: "Ammo Up",
          52: "Reload Speed",
          53: "Recoil Down",
          54: "Steadiness",
          55: "Rapid Fire Up",
          56: "Defense Boost",
          57: "Divine Blessing",
          58: "Recovery Up",
          59: "Recovery Speed",
          60: "Speed Eating",
          61: "Earplugs",
          62: "Windproof",
          63: "Tremor Resistance",
          64: "Bubbly Dance",
          65: "Evade Window",
          66: "Evade Extender",
          67: "Fire Resistance",
          68: "Water Resistance",
          69: "Ice Resistance",
          70: "Thunder Resistance",
          71: "Dragon Resistance",
          72: "Blight Resistance",
          73: "Poison Resistance",
          74: "Paralysis Resistance",
          75: "Sleep Resistance",
          76: "Stun Resistance",
          77: "Muck Resistance",
          78: "Blast Resistance",
          79: "Botanist",
          80: "Geologist",
          81: "Partbreaker",
          84: "Good Luck",
          85: "Speed Sharpening",
          86: "Bombardier",
          87: "Mushroomancer",
          88: "Item Prolonger",
          89: "Wide-Range",
          90: "Free Meal",
          91: "Heroics",
          92: "Fortify",
          93: "Flinch Free",
          94: "Jump Master",
          95: "Carving Pro",
          96: "Hunger Resistance",
          97: "Leap of Faith",
          98: "Diversion",
          99: "Master Mounter",
          104: "Wirebug Whisperer",
          105: "Wall Runner",
          106: "Counterstrike",
          107: "Rapid Morph",
          108: "Hellfire Cloak",
          116: "Coalescence",
          122: "Redirection",
          123: "Spiribird's Call",
          124: "Charge Master",
          125: "Foray",
          126: "Tune-Up",
          127: "Grinder (S)",
          128: "Bladescale Hone",
          129: "Wall Runner (Boost)",
          131: "Chain Crit"}


######################### Function #########################

"""
Construct correctly formated strings from a JSON file of charms exported 
from 'Charm Editor and Item Cheat' mods to statisfy the formating of 
Monster Hunter Rise:Sunbreak Armorset Search on https://mhrise.wiki-db.com/sim/?hl=en

:param data: JSON file exported from 'Charm Editor and Item Cheat' mod for MH Rise
:return: returns a list of formated charm strings
"""
def stringbuilder(data):
    formated_strings = []
    
    for charm in data:
        try:
            skill_1 = skills[charm["Skills"][0]]

            tmp = f'{skill_1},{charm["SkillLevels"][0]}'

            if charm["Skills"][1] != 0:                         # if there are 2 skills
                skill_2 = skills[charm["Skills"][1]]
                tmp += f',{skill_2},{charm["SkillLevels"][0]}'
            else:
                tmp += ',,0'                                    # append ,,0 if there is only one skill on the charm

            if len(charm["Slots"]) >= 1:                        # dont think this check is neccessary but just to be sure
                tmp += f',{",".join(str(x) for x in charm["Slots"])}'

            formated_strings.append(tmp)
        
        except:
            print(charm)

    return formated_strings

######################### Reading and parsing JSON #########################

with open(file_path, "r") as f:
    file = f.read()

try:
    data = json.loads(file)
except:
    print("Please select a valid json file")
    _ = input("Press the enter button to exit")
    sys.exit(-1)

######################### Execute function #########################

charms = stringbuilder(data)


######################### Check if we missed some charms #########################

if len(data) != len(charms):
    print(f"somehow not all your charms could be exported. We are missing {len(data)-len(charms)} charms.")


######################### Write charms to text-file #########################

with open('charms.txt', "w") as file:
    for charm in charms:
        file.write(charm + "\n")
        
print(f"Successfully exported your charms to 'charms.txt' in {Path(__file__).parent.absolute()}.")
_ = input("Press the enter button to exit")
sys.exit(0)


        




