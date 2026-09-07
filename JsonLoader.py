#Test class for saving algebra equations
#TODO Make it work
from pathlib import Path
import json
class AlgebraLoader:
    #Initiallizes the file and looks for the absolute file folder
    def __init__(self, filepath= Path(__file__).resolve().parent):
        self.filepath = filepath / 'config.json'
        self.configs = self.load_settings()
    #Loads the file        
    def load_settings(self):        
        if not self.filepath.is_file():
            print("Json file not found.")
            return self.default_settings() 
        try:
            with  open(self.filepath) as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Error reading JSON.")
            return self.default_settings()
    def save_settings(self):
        with open(self.filepath, "w") as file:
            json.dump(self.configs, file, indent=4)
    def default_settings(self):
        default = {
            "A": 1,
            "Variables": "x",
            "B": 1,
            "C": 1
        }
        self.settings = default
        self.save_settings()
        return default
