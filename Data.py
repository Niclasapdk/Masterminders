import random

class MastermindData:

    def __init__(self):
        pass

    def check(self, code, guess):
        for i in range(len(code)):

            if code[i] == guess[i]:
                guess[i] = 'check'

            for j in range(len(code)):
                if guess[i] == code[j]:
                    guess[i] = 'half'

            if guess[i] != 'check' and guess[i] != 'half':
                guess[i] = 'wrong'
        return guess

    def randomcode(self, n):
        code = [1, 2, 3, 4, 5, 6, 7, 8]
        kode = []
        random.shuffle(code)
        for i in range(n):
            kode = kode + [code[i]]

        return kode


