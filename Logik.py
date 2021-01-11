import Data

class MastermindLogik(Data.MastermindData):

    def __init__(self):
        self.Farvemap = {"Rød":1, "Lilla":2, "Blå":3, "Gul":4, "Grøn":5, "Orange":6, "Hvid":7, "Pink":8}
        self.Talmap = {1: "Rød", 2: "Lilla", 3: "Blå", 4: "Gul", 5: "Grøn", 6: "Orange", 7: "Hvid", 8: "Pink"}

    def konverter(self, farve1, farve2, farve3, farve4):
       return [self.Farvemap[farve1], self.Farvemap[farve2], self.Farvemap[farve3], self.Farvemap[farve4]]

    def talkonverter(self, tal1, tal2, tal3, tal4):
        return [self.Talmap[tal1], self.Talmap[tal2], self.Talmap[tal3], self.Talmap[tal4]]

    def match(self, code, guess):

       codeconverted = self.konverter(code[0], code[1], code[2], code[3])
       guessconverted = self.konverter(guess[0], guess[1], guess[2], guess[3])

       return self.check(codeconverted, guessconverted)

    def randomkode(self):
        kode = self.randomcode()
        return self.talkonverter(kode[0], kode[1], kode[2], kode[3])


