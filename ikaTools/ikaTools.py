import json
import random


class ikaTools:
    lang  = "ja_JP"
    weapons_path = "./weapon.json"
    json_open_wp = open(weapons_path)
    weapons=json.load(json_open_wp)
    def __init__(self):

    def getOneBuki(id = "rand"):   #when num is none,return weapon is random
        if id == "rand":
            return random.choice(weapons)
        else
            return weapons[id]
        

    def getBukiData(id="rand"):
        buki = self getOneBuki(id)
        return buki["name"][lang]
 
