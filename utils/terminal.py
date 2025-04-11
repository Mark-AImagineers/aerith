import random
import json

class TerminalManager:
    def __init__(self):
        pass
    
    def get_voiceline(self, type):
        with open(f"resources/aerith_{type}.json", "r", encoding="utf-8") as f:
            voice_list = json.load(f)
        
        chosen_line = random.choice(voice_list)
        return chosen_line