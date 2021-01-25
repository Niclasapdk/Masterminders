import Logik


class test_GUI(Logik.MastermindLogik):
    def spil(self):
        print('Welkommen til mastermind')
        ting = int(input('hvor mange farver vil du have?: (4-8)'))
        code = self.randomkode(ting)
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
            if svar == ['check', 'check', 'check', 'check']:
                break


test_GUI().spil()


