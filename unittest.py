import Logik
import unittest


class TestafLogikogdatalag(unittest.TestCase):

    def test1(self):
        xd = Logik.MastermindLogik()
        self.assertEqual(xd.talkonverter(1), "Rød")

    def test2(self):
        xd = Logik.MastermindLogik()
        self.assertEqual(xd.konverter("Rød"), 1)

    def test3(self):
        



if __name__ == "__main__":
    unittest.main()