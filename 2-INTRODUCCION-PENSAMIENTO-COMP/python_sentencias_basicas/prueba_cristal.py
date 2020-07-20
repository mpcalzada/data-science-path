import unittest


def es_mayor_edad(edad):
    if edad >= 18:
        return True
    else:
        return False


class PruebaCristalTest(unittest.TestCase):

    def test_es_mayor_edad(self):
        self.assertTrue(es_mayor_edad(18))

    def test_no_es_mayor_edad(self):
        self.assertEqual(es_mayor_edad(17), False)


if __name__ == '__main__':
    unittest.main()
