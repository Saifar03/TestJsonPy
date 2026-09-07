import json


#TODO Finish the parser, for Ax+B=C where all A,B,C are integers. 
# Fixing needs to work when A = 1(not visible) and B = 0 (Also not visible)
# Future make it work with Fractions
# Implement the OCR
class EquationParser:
    def __init__(self, equation):
        equation.replace(" ","")
        self.sides = equation.split(sep="=")
    def paserHelper(self):
        side = 0
        sign = "+"
        biggest = -1
        for i in enumerate(self.sides):
            ind = self.sides[i[0]].find("x")
            if(ind>biggest):
                side = i[0]
        if(self.sides[side].find("+")==-1):
            sign = "-"
        self.parser(side, sign)
    def parser(self,side,sign):
        self.sideSign = self.sides[side].rfind(sign)
        self.part = self.sides[side][self.sideSign::1]
        if self.part.lstrip(sign).isdigit():
            self.b = int(self.part)
            self.a = int(self.sides[side][:self.sides[side].find("x")])
        else:
            self.a = int(self.part[self.part.find(sign):self.part.find("x")])
            self.b = int(self.sides[side][:self.sideSign])
        self.c = int(self.sides[side-1])


equation = input()
eq = EquationParser(equation)
eq.paserHelper()

default = {
            "A": eq.a,
            "OpInX": None,
            "Variables": "x",
            "B": eq.b,
            "C": eq.c
        }
with open("config.json", "w") as file:
        json.dump(default, file, indent=4)
