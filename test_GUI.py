import Logik


class test_GUI(Logik.MastermindLogik):
    def spil(self):
        print('Velkommen til mastermind')
        ting = int(input('hvor mange farver vil du have?: (4-8)'))
        code = self.randomkode(int(ting))

        for i in range(10):
            print('''farver:
    Rød
    Lilla
    Blå
    Gul
    Grøn
    Orange
    Hvid
    Pink
            ''')
            guess = input(f'gæt nummer {i}:')
            guess = guess.split()
            print(guess)

            svar = self.match(code, guess)
            print(svar)
            liste = []
            for i in range(ting):
                liste = liste + ['check']
            if svar == liste:
                break


test_GUI().spil()


