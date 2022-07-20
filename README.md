# MH Rise Charm Parser
Simple python script to convert an exported JSON file from the **[Charm Editor and Item Cheat](https://www.nexusmods.com/monsterhunterrise/mods/17)** mod for Monster Hunter Rise to the format of the **[MH Rise Armor Search Tool](https://mhrise.wiki-db.com/sim/?hl=en)**. <br><br>
I wrote this mostly for myself. If you encounter any errors please open an issue and maybe I'll get around to fixing it. The script is really short so you may be able to fix it yourself. <br><br>
Currently only english is supported.


# Usage
1. Export your charms with this **[mod](https://www.nexusmods.com/monsterhunterrise/mods/17)**
2. Download / Clone this repo
3. Open the charm_parser.py file (either double click or open with terminal)
    - (if you only see the terminal pop up for a second and then close there is an error somewhere. Try to run the file from the terminal to see the error message)
4. Select the exported JSON file
5. If you see the success message there should be a file called "charms.txt" in the directory where you started the python script
    - You will see an error message if the JSON file can not be parsed or if not all charms could be converted (in this case all other charms will be saved tho) 



# Requirements
- Python (i guess)
- All modules should be build-in. If you get errors maybe pip install the missing dependencies



# Alternatives
If you don't want to mod your game or you are playing on Nintendo Switch there is this (way more advanced) app: **[Utsushi's Charm](https://github.com/chpoit/utsushis-charm)**



# Disclaimer
I do not own any of the trademarks or brands. 
