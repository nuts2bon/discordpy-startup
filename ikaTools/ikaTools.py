import json
import random

class ikaTools:
    lang  = "ja_JP"
    weapons_path = "./weapon.json"
    json_open_wp = open(weapons_path)
    weapons=json.load(json_open_wp)
    def __init__(self):
        self.setOneBuki()
        	
    def setOneBuki(self,id = "rand"):   #when num is none,return weapon is random
        """self.setOneBuki=random.choice(weapons)
    """
        if id == "rand":
            self.buki=random.choice(self.weapons)
            #return random.choice(weapons)
        else:
            self.buki=weapons[id]
            #return self.weapons[id]
    

    def getBukiData(self,id="rand"):
        #buki = self.setOneBuki(id)
        return self.buki["name"][self.lang]
        


