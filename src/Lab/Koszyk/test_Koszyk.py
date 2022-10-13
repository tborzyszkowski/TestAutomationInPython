import unittest
from Koszyk import Koszyk, NoProduktInKoszykException, EmptyKoszykException
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

    def test_remove_exiting_produkt_from_koszyk(self):
        produkt = Produkt()
        sut = Koszyk([produkt])
        sut.remove(produkt)
        self.assertFalse(produkt in sut.lista_produktow)

    def test_remove_nonexiting_produkt_from_koszyk(self):
        sut = Koszyk([Produkt()])
        with self.assertRaises(NoProduktInKoszykException):
            sut.remove(Produkt())

    def test_remove_produkt_from_empty_koszyk(self):
        sut = Koszyk()
        with self.assertRaises(EmptyKoszykException):
            sut.remove(Produkt())


if __name__ == '__main__':
    unittest.main()
