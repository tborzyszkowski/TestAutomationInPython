import unittest
from Koszyk import Koszyk
from Produkt import Produkt

class MyTestCase(unittest.TestCase):
    def test_add_item_to_koszyk(self):
        # Arrange
        produkt = Produkt()
        sut = Koszyk()
        num_of_product_before = len(sut.lista_produktow)
        #Act
        sut.add(produkt)
        num_of_product_after = len(sut.lista_produktow)
        # Assert
        self.assertEqual(num_of_product_before+1, num_of_product_after)


if __name__ == '__main__':
    unittest.main()
