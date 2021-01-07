import Data

class MastermindLogik(Data.MastermindData):

    def __init__(self):
        self.Farvemap = {"Rød":1, "Lilla":2, "Blå":3, "Gul":4, "Grøn":5, "Orange":6, "Hvid":7, "Pink":8}

    def konverter(self, farve1, farve2, farve3, farve4):
       return [self.Farvemap[farve1], self.Farvemap[farve2], self.Farvemap[farve3], self.Farvemap[farve4]]


    def match(self, code, guess):

       codeconverted = self.konverter(code[0], code[1], code[2], code[3])
       guessconverted = self.konverter(guess[0], guess[1], guess[2], guess[3])

       return self.check(codeconverted, guessconverted)



