from pathlib import Path
import json

"""
#Test class for saving algebra equations
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
"""


#TODO: Change logic to first check if its digit then check if alphanum or ignore it
equation = input()
equation = equation.replace(" ","")
sides = equation.split(sep="=")
if(len(sides[0])>len(sides[1])):
    if(sides[0].find("+")!=-1):
        sign = sides[0].find("+")
        part = sides[0][sign::1]
        if part.isalnum():
            a = int(part[:sides[0].find("x")])
            b = int(sides[0][:sign])
        else:
            b= int(part)
            a = int(sides[0][:sides[0].find("x")])
                        
    else:
        sign = sides[0].rfind("-")
        part = sides[0][sign::1]
        if part.lstrip("-").isalnum():
            a = int(part[:part.find("x")])
            b = int(sides[0][:sign])
        else:
            b= int(part)
            a = int(sides[0][:sides[0].find("x")])
               
    c = int(sides[1])
else:
    if(sides[1].find("+")!=-1):
           sign = sides[1].find("+")
           part = sides[1][sign::1]
           if part.isalnum():
               a = int(part[:sides[1].find("x")])
               b = int(sides[:sign])
           else:
               b= int(part)
               a = int(sides[1][:sides[1].find("x")])
                           
    else:
           sign = sides[1].rfind("-")
           part = sides[1][sign::1]
           if part.lstrip("-").isalnum():
               a = int(part[:part.find("x")])
               b = int(sides[1][:sign])
           else:
               b= int(part)
               a = int(sides[1][:sides[1].find("x")])
    c = int(sides[0])

default = {
            "A": a,
            "Variables": "x",
            "B": b,
            "C": c
        }
with open("config.json", "w") as file:
        json.dump(default, file, indent=4)
