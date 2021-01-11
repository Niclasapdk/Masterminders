import Logik


class test_GUI(Logik.MastermindLogik):
    def spil(self):
        print('Welkommen til mastermind')
        code = self.randomkode()
        for i in range(10):
            guess = input(f'gæt nummer {i}:')
            guess = guess.split()
            print(guess)
            svar = self.match(code, guess)
            print(svar)
            if svar == ['check', 'check', 'check', 'check']:
                break


test_GUI().spil()


