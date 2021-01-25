import Data

class MastermindLogik(Data.MastermindData):

    def __init__(self):
        self.Farvemap = {"Rød":1, "Lilla":2, "Blå":3, "Gul":4, "Grøn":5, "Orange":6, "Hvid":7, "Pink":8}
        self.Talmap = {1: "Rød", 2: "Lilla", 3: "Blå", 4: "Gul", 5: "Grøn", 6: "Orange", 7: "Hvid", 8: "Pink"}

    def konverter(self, farve1):
       return (self.Farvemap[farve1])

    def talkonverter(self, tal1):
        return (self.Talmap[tal1])

    def match(self, code, guess):

        for i in range(len(code))
            codeconverted = self.konverter(code[i])
            guessconverted = self.konverter(guess[i])

        return self.check(codeconverted, guessconverted)

    def randomkode(self):
        kode = self.randomcode()

        return self.talkonverter(kode[0], kode[1], kode[2], kode[3])


