import unittest


def suma(x, y):
    return x + y


class CajaNegraTest(unittest.TestCase):

    def suma_numeros_positivos(self):
        x = 10
        y = 5

        self.assert_(suma(x, y), 15)


if __name__ == '__main__':
    unittest.main()
